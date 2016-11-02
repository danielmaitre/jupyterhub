# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# Pin to version of notebook image that includes start-singleuser.sh script
FROM jupyter/base-notebook

# Install packages in default Python 3 environment
RUN pip install \
  matplotlib sympy  && rm -r /home/jovyan/.cache/pip

# Install packages in Python 2 environment
#RUN $CONDA_DIR/envs/python2/bin/pip install \
#  beautifulsoup4==4.4.*

# Use custom startup script
USER root
COPY docker-entrypoint.sh /srv/docker-entrypoint.sh
ENTRYPOINT ["tini", "--", "/srv/docker-entrypoint.sh"]
CMD ["start-singleuser.sh"]

COPY npp-git/npp /opt/conda/lib/python3.5/site-packages/npp

RUN apt-get update && apt-get -y install git && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
#RUN apt-get remove -y locales
RUN rm -r /usr/share/locale /usr/share/man /usr/share/doc
USER jovyan
COPY mpl /home/jovyan/.cache/matplotlib

