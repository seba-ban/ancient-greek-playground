#!/bin/bash

set -e

IMAGE_NAME="ancientgreekplayground/existdb:latest"

dockerfile_path=${1:?"dockerfile path is required"}
context_dir=${2:?"context dir is required"}

docker image build -t ${IMAGE_NAME} -f "${dockerfile_path}" "${context_dir}"
docker container run -d -p 18080:8080 -p 18443:8443 --name existdb-ancient-greek-playground ${IMAGE_NAME}
