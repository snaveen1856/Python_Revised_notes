#!/bin/bash

CONTAINER_NAME=$1
test_case=$2

if [ "$#" -ne 2 ]; then
        echo "error occured"
        echo "usage: deploy.sh <container_name> and <test_name>"
        exit -1
fi

sutas_deploy=$(docker exec -it ${CONTAINER_NAME} python ${test_case})
if [ $? -eq 0 ]
  then
    echo deployed successfully
    echo $sutas_deploy
    exit 0
  else
    echo fail to deploy
    exit 1
fi







############################################ sutas_log.sh ##################################################


#!/bin/bash

CONTAINER_NAME=$1
PATH1='/home/admin/GTA_logs'
if [ "$#" -ne 1 ]; then
        echo "error occured"
        echo "usage: deploy.sh <container_name>"
        exit -1
fi
#dir_create=$(mkdir ${PATH1})

sutas_deploy=$(docker cp ${CONTAINER_NAME}:/root/Sutas_Logs ${PATH1})
if [ $? -eq 0 ]
  then
    echo logs saved succesfully
    exit 0
  else
    echo fail to save logs
    exit 1
fi
