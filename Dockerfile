FROM python:3.9

EXPOSE 9999

WORKDIR /src
COPY ./src/* .
RUN python3 -m pip install -r requirements.txt

CMD ["python3", "main.py" ]