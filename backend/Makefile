restart:
	docker restart backend_dictionnaire

interact:
	docker exec -it backend_dictionnaire bash

log:
	docker logs -f --tail 100 backend_dictionnaire
	
rlog: restart
	docker logs -f --tail 100 backend_dictionnaire
	
migrate:
	flask --app srcs/main.py db migrate
	flask  --app srcs/main.py db upgrade