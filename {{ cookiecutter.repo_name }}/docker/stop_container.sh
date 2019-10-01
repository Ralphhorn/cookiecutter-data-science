#!/bin/bash
mydir=$(dirname "$0")
source $mydir/../.env
docker stop $DOCKER_NAME