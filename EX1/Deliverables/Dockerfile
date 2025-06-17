FROM python:3-alpine3.22

RUN adduser -D vinicius 

WORKDIR /app

COPY --chown=vinicius:vinicius requirements.txt .

RUN pip3 install -r requirements.txt

COPY --chown=vinicius:vinicius . .

USER vinicius

ENTRYPOINT ["python3", "main.py"]