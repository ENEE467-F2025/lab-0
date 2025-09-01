# ENEE 467 Fall 2025: Robotics Project Laboratory
## Lab 0: Introduction to Linux Operating Systems and Python Programming

This repository contains a Docker container for the first lab as well as the necessary code templates for completing the exercises.

## Overview

## Starting the container

The lab computers contain a prebuild image so you will not have to build the image.
* Clone this repo to get the lab-0 code
    ```
    cd
    git clone git@github.com:ENEE467-F2025/lab-0.git
    cd lab-0/docker
    ```
* Run the Docker container
    ```
    docker compose -f lab-0-compose.yml run --rm lab-0-docker
    ```
* Once inside the container, you should be greeted with the following prompt
    ```
    (lab-0) robot@docker-desktop:~$
    ```
indicating that the container is running
* Edit the lab-0 code `matrix.py` and `pendulum.py` from a VS Code editor on the host machine. This `lab-0` directory is mounted to the docker container so all changes will be reflected inside the container.
* To execute the Python script, use the following command
    ```
    python pendulum.py
    ```