# Use an official Node.js runtime as a parent image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the working directory
COPY package*.json ./

# Install project dependencies
RUN npm install

EXPOSE 3000

# Define the command to run the application
CMD ["npm", "run", "dev", "--", "--host"]