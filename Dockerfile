FROM fastapi-summarization:latest
LABEL MAINTANIER="Luna McBride <luna.mcbride24@gmail.com>"

WORKDIR /srv
COPY . /srv
ENV PYTHONPATH = "${PYTHONPATH}:/srv/"

EXPOSE 80

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "-m", "uvicorn",  "summFast:app", "--host", "0.0.0.0", "--port", "80"]