FROM python:3.9.7-slim
COPY ./src/requirements.txt ./
RUN pip install -r requirements.txt
