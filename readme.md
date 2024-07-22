# icanhazip-clone

A simple Flask-based web application that returns the client's IP address in plain text, mimicking the functionality of icanhazip.com. Easily deployable with Docker.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Docker Image

You can run the Docker image directly using the following command:

```bash
docker run -d -p 80:80 thejordanprice/icanhazip-clone
```

This will start the web application on port 80.

### Running with Docker Compose

Alternatively, you can use Docker Compose to run the application. First, create a `docker-compose.yml` file with the following content:

```yaml
version: '3'
services:
  icanhazip-clone:
    image: thejordanprice/icanhazip-clone
    ports:
      - "80:80"
```

Then, run the following command to start the application:

```bash
docker-compose up -d
```

## Accessing the Application

Once the application is running, you can access it by navigating to `http://localhost` in your web browser. The application will display your IP address in plain text.

## Repository

You can find the source code and contribute to the project at [GitHub](https://github.com/thejordanprice/icanhazip-clone).

## Docker Hub

The Docker image is available on Docker Hub at [thejordanprice/icanhazip-clone](https://hub.docker.com/repository/docker/thejordanprice/icanhazip-clone).
