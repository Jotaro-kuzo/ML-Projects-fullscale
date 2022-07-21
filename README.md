# ML-Projects-fullscale

Contains full scale ML projects from  zero to deployment.


## Software Requirements:

1. Git
2. Cloud account (heroku,AWS,Azure)
3. IDE (VS Code , Pycharm)
4. Git CLI

## Conda Environmnet:

```
    conda create -p <env name> python == 3.7 -y
```
## Now create requiremnets and insert the require libraries
```
    touch requiremnets.txt  
    pip install -r requirements.txt    <--   run this after you insert necessary libraries

```

To add files what we created,
```
git add <filename>
```
```
git add .  <-- to add all files at a time
```

To ignore the copying of files/folders , insert those names in .gitignore file

To check git status:
```
git status
```

To check the versions
```
git log
``` 

To commit/meaasge of version:

```
git commit -m "message"
```

To send version/changes:

```
git push origin main
```

to check remote url:

```
git remote -v
```

## To setup CI/CD pipeline to heroku:
    We need:
     1.Heroku_Email = sk6724486@gmial.com
     2.Heroku_app_key = d6d76f26-ff52-497b-91be-8d074115a71a
     3.Heroku_app_name = first-ci-cd-with-simple-messag


## Docker file:

    1.create a file with name "Dockerfile"

    ```
    FROM python:3.7
    COPY . /app
    WORKDIR /app
    RUN pip install -r requirements.txt
    EXPOSE $PORT
    CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
    ```

    ## docker image:

    ```
    docker build -t <image_name>:<tagname> .   (lower case only)
    ```

## To list docker images:
    ```
    docker images  
    ```