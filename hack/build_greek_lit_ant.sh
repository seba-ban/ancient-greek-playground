#!/bin/bash

# build greek lit to use in exist-db, I didn't manage to load the file to exist-db yet...
# cf. https://github.com/PerseusDL/canonical-greekLit#installing-on-exist-db

set -e

repo_dir=$(realpath "${1:?"repo dir is required"}")
output_dir=$(realpath "${2:?"output dir is required"}")
container_script=$(cat "${3:?"container script path is required"}")

docker container run --rm --user "$(id -u)" -v "$repo_dir":/data -v "$output_dir":/output adoptopenjdk/openjdk14 bash -c "$container_script"
echo "files are in $output_dir"