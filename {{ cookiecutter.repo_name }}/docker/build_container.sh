#!/bin/bash
mydir=$(dirname "$0")
source $mydir/../.env

docker build -t $DOCKER_NAME $WORKSPACE_ROOT/docker

