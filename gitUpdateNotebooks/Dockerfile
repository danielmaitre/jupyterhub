# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# Pin to version of notebook image that includes start-singleuser.sh script
FROM alpine

# Install packages in default Python 3 environment
RUN apk update && apk upgrade && apk add --no-cache bash git openssh


USER root
COPY docker-entrypoint.sh /srv/docker-entrypoint.sh
RUN chmod a+r /srv/docker-entrypoint.sh
RUN adduser -s /bin/bash -D -G users -u 1000 jovyan 

USER jovyan

ENTRYPOINT ["sh","/srv/docker-entrypoint.sh"]



