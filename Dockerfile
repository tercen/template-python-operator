FROM tercen/runtime-python39:0.0.3

COPY . /operator
WORKDIR /operator

#RUN pip3 install --ignore-installed git+https://github.com/tercen/tercen_python_client
# pipreqs does not generate the requirement to install from github
# So the line below sets the requirement to install the client from the github repo
# RUN sed -i 's/tercen==[0-9].[0-9].[0-9]/git+https:\/\/raw.githubusercontent\/tercen\/tercen_python_client/master/dist/tercen-0.0.2-py3-none-any.whl/' requirements.txt

RUN sed -i 's/tercen==/https:\/\/raw.githubusercontent.com\/tercen\/tercen_python_client\/main\/dist\/tercen-/' requirements.txt
RUN sed -i 's/\(tercen-[0-9]\.[0-9]\.[0-9]\)/\1-py3-none-any.whl/' requirements.txt
RUN python3 -m pip install -r ./requirements.txt

ENV TERCEN_SERVICE_URI https://tercen.com

ENTRYPOINT [ "python3", "main.py"]
CMD [ "--taskId", "someid", "--serviceUri", "https://tercen.com", "--token", "sometoken"]