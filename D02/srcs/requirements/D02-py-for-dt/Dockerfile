# syntax=docker/dockerfile:1
FROM python:3.11.9-slim-bullseye

# Install dependencies
RUN --mount=target=/var/lib/apt/lists,type=cache,sharing=locked \
		--mount=target=/var/cache/apt,type=cache,sharing=locked \
		rm -f /etc/apt/apt.conf.d/docker-clean \
		apt-get update && \
		apt-get upgrade -y && \
		apt-get install -y \
			libx11-dev \
			python3-tk && \
		apt-get clean

WORKDIR /home/D02-python-for-data-science

# Copy and install Python dependencies
COPY conf/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy exercise files after dependencies to leverage Docker cache
COPY /exercises ./exercises

CMD [ "tail", "-f", "/dev/null" ]
