# apt install openssl

# openssl genrsa -out server.key 2048
# openssl req -key server.key -new -out server.csr
# openssl x509 -signkey server.key -in server.csr -req -days 365 -out server.crt

# echo "
# events { }
# http {
#     server {
#         listen 443 ssl;

#         ssl_certificate /opt/certificates/server.crt;
#         ssl_certificate_key /opt/certificates/server.key;

#         location / {
#             proxy_pass http://backend:5000;
#         }
#     }
# }" > /etc/nginx/conf.d/default.conf

# echo "
# server {
#     listen 80;
#     server_name ${APP_DOMAIN};

#     location / {
#         return 301 https://$host$request_uri;
#     }

#     location /.well-known/acme-challenge/ {
#         root /var/www/certbot;
#     }
# }

# server {
#     listen 443 ssl;
#     server_name ${APP_DOMAIN};
#     server_tokens off;
#     client_max_body_size 20M;

#     ssl_certificate /etc/letsencrypt/live/${APP_DOMAIN}/fullchain.pem;
#     ssl_certificate_key /etc/letsencrypt/live/${APP_DOMAIN}/privkey.pem;
#     include /etc/letsencrypt/options-ssl-nginx.conf;
#     ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

#     location / {
#         proxy_set_header X-Forwarded-Proto https;
#         proxy_set_header X-Url-Scheme $scheme;
#         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#         proxy_set_header Host $http_host;
#         proxy_redirect off;
#         proxy_pass http://backend:5000; // Your app service name
#     }
# }" > /etc/nginx/conf.d/default.conf

# nginx -g 'daemon off;'

#!/bin/bash

# Source the .env file
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

if ! [ -x "$(command -v docker compose)" ]; then
    echo 'Error: docker compose is not installed.' >&2
    exit 1
fi

domains=(${APP_DOMAIN:-example.com})
rsa_key_size=4096
data_path="./nginx/certbot"
email="${SSL_EMAIL:-hello@example.com}" # Adding a valid address is strongly recommended
staging=0 # Set to 1 if you're testing your setup to avoid hitting request limits

if [ -d "$data_path" ]; then
    read -p "Existing data found for $domains. Continue and replace existing certificate? (y/N) " decision
    if [ "$decision" != "Y" ] && [ "$decision" != "y" ]; then
        exit
    fi
fi

if [ ! -e "$data_path/conf/options-ssl-nginx.conf" ] || [ ! -e "$data_path/conf/ssl-dhparams.pem" ]; then
    echo "### Downloading recommended TLS parameters ..."
    mkdir -p "$data_path/conf"
    curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/tls_configs/options-ssl-nginx.conf >"$data_path/conf/options-ssl-nginx.conf"
    curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/certbot/ssl-dhparams.pem >"$data_path/conf/ssl-dhparams.pem"
    echo
fi

echo "### Creating dummy certificate for $domains ..."
path="/etc/letsencrypt/live/$domains"
mkdir -p "$data_path/conf/live/$domains"
docker compose -f "docker-compose.yml" run --rm --entrypoint "\
  openssl req -x509 -nodes -newkey rsa:$rsa_key_size -days 1\
    -keyout '$path/privkey.pem' \
    -out '$path/fullchain.pem' \
    -subj '/CN=localhost'" certbot
echo

echo "### Starting nginx ..."
docker compose  -f "docker-compose.yml" up --force-recreate -d nginx
echo

echo "### Deleting dummy certificate for $domains ..."
docker compose  -f "docker-compose.yml" run --rm --entrypoint "\
  rm -Rf /etc/letsencrypt/live/$domains && \
  rm -Rf /etc/letsencrypt/archive/$domains && \
  rm -Rf /etc/letsencrypt/renewal/$domains.conf" certbot
echo

echo "### Requesting Let's Encrypt certificate for $domains ..."
#Join $domains to -d args
domain_args=""
for domain in "${domains[@]}"; do
    domain_args="$domain_args -d $domain"
done

# Select appropriate email arg
case "$email" in
"") email_arg="--register-unsafely-without-email" ;;
*) email_arg="--email $email" ;;
esac

# Enable staging mode if needed
if [ $staging != "0" ]; then staging_arg="--staging"; fi

docker compose -f "docker-compose.yml" run --rm --entrypoint "\
  certbot certonly --webroot -w /var/www/certbot \
    $staging_arg \
    $email_arg \
    $domain_args \
    --rsa-key-size $rsa_key_size \
    --agree-tos \
    --force-renewal" certbot
echo

