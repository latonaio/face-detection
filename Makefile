docker-build:
	bash builders/docker-build.sh

docker-push:
	bash builders/docker-build.sh push

.PHONY: docker-build-clean
docker-build-clean: docker-build
	sudo /bin/bash -c "echo 3 > /proc/sys/vm/drop_caches"

.PHONY: docker-push-clean
docker-push-clean: docker-push
	sudo /bin/bash -c "echo 3 > /proc/sys/vm/drop_caches"
