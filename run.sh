#!/bin/sh

docker rm -f ical_filter
docker run -itd --name=ical_filter \
	--restart=always \
	-p 5001:80 \
	ical_filter

