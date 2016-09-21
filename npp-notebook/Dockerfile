# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# Pin to version of notebook image that includes start-singleuser.sh script
FROM jupyter/scipy-notebook

# Install packages in default Python 3 environment
RUN pip install \
  matplotlib \
  PyQt5

# Install packages in Python 2 environment
#RUN $CONDA_DIR/envs/python2/bin/pip install \
#  beautifulsoup4==4.4.*

# Use custom startup script
USER root
COPY docker-entrypoint.sh /srv/docker-entrypoint.sh
ENTRYPOINT ["tini", "--", "/srv/docker-entrypoint.sh"]
CMD ["start-singleuser.sh"]

COPY npp-git/npp /opt/conda/lib/python3.5/site-packages/npp
USER jovyan
