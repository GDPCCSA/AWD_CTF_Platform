#!/bin/sh
docker run -p 9090:8000  -d  -v `pwd`/webapps:/webapps --name AWD-flag_server -ti moxiaoxi/flag_server