FROM continuumio/miniconda3

RUN useradd -ms /bin/bash robot
USER robot
WORKDIR /home/robot

SHELL ["/bin/bash", "-c"]

COPY docker/environment.yml /tmp/environment.yml

# RUN conda create -n lab-0 python=3.10
RUN conda env create -f /tmp/environment.yml
RUN echo "source activate lab-0" > ~/.bashrc
ENV PATH /opt/conda/envs/lab-0/bin:$PATH

RUN mkdir lab-0
#COPY matrix.py lab-0/
#COPY pendulum.py lab-0/

ENTRYPOINT ["/bin/bash"]