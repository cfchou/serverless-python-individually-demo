
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
    "body": "{\"input\": {}, \"message\": \"requests 2.12.3, bcrypt 3.1.1 installed. hash generated: $2b$12$gnCAOWLOJzx5Z4pudIv.9e2wkpJiTG/.P7cWc6y882QfS6IHLe7Ii\"}",
    "statusCode": 200
}

// This function is placed under a subdirectory and has a platform dependent package subprocess32.
$ sls invoke -f world -l
{
    "body": "{\"input\": {}, \"message\": \"subprocess32 checks openssl version OpenSSL 1.0.1k-fips 8 Jan 2015\\n installed.\"}",
    "statusCode": 200
}

// This function is not handled by this plugin.
$ sls invoke -f vanilla -l
{
    "body": "{\"input\": {}, \"message\": \"is not touched by serverless-python-individually plugin\"}",
    "statusCode": 200
}
```

