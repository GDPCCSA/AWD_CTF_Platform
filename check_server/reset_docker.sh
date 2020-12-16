#!/bin/sh
docker stop check_server
docker rm check_server
docker run -d -v `pwd`/webapps:/webapps  --name AWD-check_server -ti moxiaoxi/check_server