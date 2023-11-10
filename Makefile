build:
	docker build -t vra1-image .

run:
	docker run -it -p 5000:5000 vra1-image

test:
	curl --output /dev/stderr --write-out "%{http_code}" -X GET -u $$KDDEPPRD_ARTIFACTORY_USERNAME:“$$KDDEPPRD_ARTIFACTORY_API_KEY” “http://artifactory-uw2.adobeitc.com/artifactory/generic-ethos-kd-release/$(KD_VERSION)/k8s-director-$(KD_VERSION)” > text1.html