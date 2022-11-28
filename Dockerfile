FROM tercen/runtime-python39:001
#FROM tercen/runtime-r40-slim:4.0.4-0

COPY . /operator
WORKDIR /operator

ENV TERCEN_SERVICE_URI https://tercen.com

ENTRYPOINT [ "python3","main.py"]
CMD [ "--taskId", "someid", "--serviceUri", "https://tercen.com", "--token", "sometoken"]