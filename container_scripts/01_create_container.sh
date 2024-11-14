#!/bin/bash

# Define the container name as a variable
CONTAINER_NAME="u22_gui"

# Check if the container already exists
if [ "$(docker ps -a -q -f name=$CONTAINER_NAME)" ]; then
  echo "Container '$CONTAINER_NAME' already exists. Delete the container..."
  docker stop $CONTAINER_NAME
  docker rm $CONTAINER_NAME
fi

echo "Container '$CONTAINER_NAME' does not exist. Creating and starting the container..."
docker run -it -p 1922:22 --privileged \
-v /share/CACHEDEV1_DATA/homes/admin/container_storage/root:/root 
-v /share/CACHEDEV1_DATA/homes/admin/container_storage:/mount \
-e LANG=C.UTF-8 \
--name $CONTAINER_NAME ubuntu:22.04 \
/bin/bash -c '/mount/start.sh && /bin/bash'


# -v /share/CACHEDEV1_DATA/homes/admin/conteiner_storage/root:/root \

