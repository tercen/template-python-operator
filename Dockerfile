FROM tercen/runtime-python39:0.0.2

COPY . /operator
WORKDIR /operator

ENV TERCEN_SERVICE_URI https://tercen.com

#RUN pip3 install --ignore-installed git+https://github.com/tercen/tercen_python_client
# pipreqs does not generate the requirement to install from github
# So the line below sets the requirement to install the client from the github repo
RUN sed -i 's/tercen==[0-9].[0-9].[0-9]/git+https:\/\/github.com\/tercen\/tercen_python_client/' requirements.txt
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT [ "python3","main.py"]
CMD [ "--taskId", "someid", "--serviceUri", "https://tercen.com", "--token", "sometoken"]