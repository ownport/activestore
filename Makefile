#
#	variables
#

SHELL := /bin/bash
DOCKER_VOLUMES_PATH := `cat local_settings.yml | grep DOCKER_VOLUMES_PATH | cut -d : -f 2`

#
#	actions
#

create-dev-env:
	@ docker build -t 'ownport/activestore:dev' docker/dev-env/

run-dev-env: 
	@ mkdir -p $$(pwd)/deploy/data/activestore/
	@ docker run -ti --rm --name=activestore-dev \
		-v $$(pwd)/activestore/:/app/activestore/activestore/ \
		-v $$(pwd)/deploy/data/activestore/:/data/activestore/ \
		ownport/activestore:dev

test-all-with-coverage: 
	@ nosetests --with-coverage --cover-package=activestore  --verbosity=1 --cover-erase

