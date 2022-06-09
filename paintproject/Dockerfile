FROM python:3.9
ENV PYTHONUNBUFFERED = 1
WORKDIR paintproject
COPY paintproject/requirements.txt /paintproject/
RUN pip install -r requirements.txt
COPY paintproject/ /paintproject/