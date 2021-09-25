docker-build-image :
	docker build --no-cache -t diegoasencio96/portafolio:$(version) .
# use: make docker-push-image version=x.x.x
docker-push-image: docker-build-image
	docker push diegoasencio96/portafolio:$(version)
