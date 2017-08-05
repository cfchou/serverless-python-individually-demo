
# serverless-python-individually-demo

## What's it?
A demo showcasing [serverless-python-individually](https://github.com/cfchou/serverless-python-individually).


## Install and deploy
- `pip install virtualenv`
- `npm install -g serverless`
- `npm install serverless-python-individually`

### If you are on a Mac:

- Make sure [docker](https://docs.docker.com/engine/installation/mac/) is installed and properly set up. I.e. when running `docker version` you should see information about client and server.
- `docker pull lambci/lambda:build-python2.7` to pull the image in advance.

Make sure **dockerizedPip** in **serverless.yml** is set to **True** and then run:
> sls deploy -v

Or run explicitly:
> sls deploy -v --pi-dockerizedPip

### If you are on a Linux x86_64:
No need to use docker to install packages. So set **dockerizedPip: False** in **serverless.yml** and then run:
> sls deploy -v

Or explicitly run:
> sls deploy -v --pi-no-dockerizedPip


## Verify
```
// This function has a platform dependent package bcrypt
$ sls invoke -f hello -l
{
    "body": "{\"input\": {}, \"message\": \"2.7.12 (default, Sep  1 2016, 22:14:00) \\n[GCC 4.8.3 20140911 (Red Hat 4.8.3-9)], requests 2.18.3, bcrypt 3.1.3 installed. hash generated: $2b$12$gq9jQ1.Qz/S27ZZ6lRdAPemv86sajA2CIQS05oMUocBblQ2JA2UbS\"}",
    "statusCode": 200
}

// This function is placed under a subdirectory.
$ sls invoke -f world -l
{
    "body": "{\"input\": {}, \"message\": \"2.7.12 (default, Sep  1 2016, 22:14:00) \\n[GCC 4.8.3 20140911 (Red Hat 4.8.3-9)], requests 2.18.3 install ed.\"}",
    "statusCode": 200
}

// This function is not handled by this plugin.
$ sls invoke -f vanilla -l
{
    "body": "{\"input\": {}, \"message\": \"is not touched by serverless-python-individually plugin\"}",
    "statusCode": 200
}
```

