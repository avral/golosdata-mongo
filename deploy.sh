#!/bin/bash

docker build -t golosdata-mongo .
docker tag golosdata-mongo avral/golosdata-mongo:latest
docker push avral/golosdata-mongo
