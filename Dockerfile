FROM python:3.8-slim-buster

RUN mkdir -p /opt/demo/g_inspect_api_sample_tests
RUN mkdir -p /opt/demo/g_inspect_api_sample_tests/builds
RUN mkdir $HOME/.pip

WORKDIR /opt/demo/g_inspect_api_sample_tests

COPY requirements.txt /opt/demo/g_inspect_api_sample_tests
COPY . /opt/demo/g_inspect_api_sample_tests

RUN pip install -r requirements.txt

ENTRYPOINT ["pytest"]
