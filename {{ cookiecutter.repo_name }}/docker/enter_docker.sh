#!/bin/bash
mydir=$(dirname "$0")
source $mydir/../.env

docker exec -it $DOCKER_NAME bash