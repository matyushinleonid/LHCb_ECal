build:
	docker build -t calorbuild .

push:
	docker tag calorbuild registry.gitlab.com/lambda-hse/registry/calorbuild
	docker push registry.gitlab.com/lambda-hse/registry/calorbuild

run:
	docker run -it -h dev --privileged -v <local-folder>:/home/nb_user/logs calorbuild