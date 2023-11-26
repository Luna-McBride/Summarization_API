VERSION=v1
DOCKERUSER=lunarreign
PROJECT=fastapi-summarization

build:
	docker build -f Dockerfile -t $(PROJECT) .

run:
	docker-compose up -d

clean:
	docker-compose down

push:
	docker tag $(PROJECT) $(DOCKERUSER)/$(PROJECT):$(VERSION)
	docker push $(DOCKERUSER)/$(PROJECT):$(VERSION)
	docker tag $(PROJECT) $(DOCKERUSER)/$(PROJECT):latest
	docker push $(DOCKERUSER)/$(PROJECT):latest