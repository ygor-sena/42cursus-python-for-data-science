DOCKER_IMG_NAME = d02-py-for-dt
DOCKER_COMPOSE = docker-compose -f srcs/docker-compose.yml

up:
	$(DOCKER_COMPOSE) up -d --build

down:
	$(DOCKER_COMPOSE) down

exec:
	docker exec -it $(DOCKER_IMG_NAME) bash

start:
	$(DOCKER_COMPOSE) start

stop:
	$(DOCKER_COMPOSE) stop

ps:
	$(DOCKER_COMPOSE) ps

clean:
	$(DOCKER_COMPOSE) down --rmi all --volumes

fclean:

prune: fclean
	docker system prune --all --force --volumes

.PHONY: up down exec start stop ps clean fclean prune
