# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# Pin to version of notebook image that includes start-singleuser.sh script
FROM jupyter/base-notebook

# Install packages in default Python 3 environment
RUN pip install \
  matplotlib sympy pandas scipy  && rm -r /home/jovyan/.cache/pip

# Use custom startup script
USER root
COPY docker-entrypoint.sh /srv/docker-entrypoint.sh
ENTRYPOINT ["tini", "--", "/srv/docker-entrypoint.sh"]
CMD ["start-singleuser.sh"]



RUN apt-get update && apt-get -y --no-install-recommends install git && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
#RUN apt-get remove -y locales
RUN rm -r /usr/share/locale /usr/share/man /usr/share/doc

COPY npp-git/npp /opt/conda/lib/python3.5/site-packages/npp

USER jovyan
COPY mpl /home/jovyan/.cache/matplotlib

