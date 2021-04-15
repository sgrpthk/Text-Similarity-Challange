## Fetch-Rewards-Data-Engineer-Coding-Challenge
# Fetch Rewards Data Engineer Coding Challenge text similarity

## I used cosine similiraty to compare two texts. 
I created a web form for useser to enter texts and calles POST API to get the result
coding_challenge.py will have all the code of the API
Dockerfile: This will have docker installation data
 
## To run the code locally: run it on the IDE and you will get link, copy and past it in the browser.

## To run Docker please fellow below instraction.
```python 

    build -t fetch-rewards-coding:latest .

```

```python

    docker run -it -d -p 127.0.0.1:5002:5002 fetch-rewards-coding
    
```
To build and run Docker image

## You can type the below to access REST API

```python

        http://127.0.0.1:5002

```
## If you don't want to clone the code from github and you want to run Docker use below code to pull the image from docker hub the to run it
```python

        docker pull mrhazim/fetch-rewards-coding:latest
        docker run -it -d -p 127.0.0.1:5002:5002 mrhazim/fetch-rewards-coding
        
```

## Docker commands

```bash
    
        // List all running container
        docker ps

        // list all containers
        docker ps -a


        // list all docker images
        docker images

        // build a docker image
        docker build -t <imageName:version> dockerFilePath

        
        // run a docker container in daemon mode with ports exposed
        docker run -it -d -p <outsidePort>:<dockerInsidePort> <imageName:version>

```
