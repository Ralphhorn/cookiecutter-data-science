{% raw %}#!/bin/bash
mydir=$(dirname "$0")
source $mydir/../.env

[[ $(docker ps -f "name=$DOCKER_NAME" --format '{{.Names}}') == $DOCKER_NAME ]] || \
docker run -d -it --rm --shm-size=1g --name $DOCKER_NAME -p 8888:8888 -p 6006:6006 \
-v $WORKSPACE_ROOT:/workspace/ $DOCKER_NAME /bin/bash \
-c "pip install --editable . && jupyter lab --ip=0.0.0.0 --notebook-dir=/workspace --allow-root --no-browser --NotebookApp.token='$DOCKER_PASSWORD'"
{% endraw %}