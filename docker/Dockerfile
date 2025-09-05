FROM continuumio/miniconda3

SHELL ["/bin/bash", "-c"]

WORKDIR ${HOME}

ENV DEBIAN_FRONTEND=noninteractive

# Basic setup
RUN apt-get update && apt-get install -y --no-install-recommends --allow-unauthenticated \
    autoconf \
    automake \
    bash-completion \
    build-essential \
    ca-certificates \
    cmake \
    curl \
    g++ \
    git \
    iproute2 \
    iputils-ping \
    libxext-dev \
    libx11-dev \
    make \
    mc \
    mesa-utils \
    nano \
    vim \
    tree \
    pkg-config \
    software-properties-common \
    sudo \
    tmux \
    tzdata \
    xclip \
    x11proto-gl-dev && \
    rm -rf /var/lib/apt/lists/*

# Set datetime and timezone correctly
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo '$TZ' | sudo tee -a /etc/timezone

ENV DEBIAN_FRONTEND=dialog

# Setup conda env
RUN groupadd -g 1002 robot
RUN useradd -ms "/bin/bash -i" --uid 1002 -g 1002 robot
USER robot
WORKDIR /home/robot
RUN mkdir Desktop

COPY docker/environment.yml /tmp/environment.yml

RUN conda env create -f /tmp/environment.yml
RUN echo "source activate lab-0" >> ~/.bashrc
ENV PATH /opt/conda/envs/lab-0/bin:$PATH

RUN mkdir -p lab-0/src

ENTRYPOINT ["/bin/bash", "-i"]