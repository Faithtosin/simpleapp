
# Go parameters
GOCMD=go
GOBUILD=$(GOCMD) build
GOCLEAN=$(GOCMD) clean
GOGET=$(GOCMD) get
REPO=public.ecr.aws/z1l0c6l7
BINARY_NAME=simpleapp
GIT_VERSION=$(shell git rev-parse HEAD)

all: clean build

docker-build:
	docker build -t $(REPO)/$(BINARY_NAME):$(GIT_VERSION) .
publish: docker-build
	docker push $(REPO)/$(BINARY_NAME):$(GIT_VERSION)

docker-buildx-build:
	docker buildx --load --platform linux/amd64 --progress plain -t $(REPO)/$(BINARY_NAME):$(GIT_VERSION) .

publish-buildx: docker-buildx-build
	docker push $(REPO)/$(BINARY_NAME):$(GIT_VERSION)
