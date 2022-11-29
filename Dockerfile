FROM tercen/runtime-python39:0.0.2
#FROM tercen/runtime-r40-slim:4.0.4-0

COPY . /operator
WORKDIR /operator

ENV TERCEN_SERVICE_URI https://tercen.com

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT [ "python3","main.py"]
CMD [ "--taskId", "someid", "--serviceUri", "https://tercen.com", "--token", "sometoken"]