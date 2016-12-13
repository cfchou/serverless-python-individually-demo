
#serverless-python-individually-demo

##What's it?
A demo showcasing [serverless-python-individually](https://github.com/cfchou/serverless-python-individually).


##Install
- pip install virtualenv
- `npm install -g serverless`
- `npm install --save serverless-python-individually`

#####If you are on a Mac:

- Make sure [docker](https://docs.docker.com/engine/installation/mac/) is installed and properly set up. I.e. when running `docker version` you should see information about client and server.
- `docker pull lambci/lambda:build-python2.7` to pull the image in advance.

####If you are on a Linux x86_64:
No need to use docker to install packages. So set **dockerizedPip: False** in **serverless.yml**.


##Run
> sls deploy -v

##Verify
```
$ sls invoke -f hello
{
    "body": "{\"input\": {}, \"message\": \"requests 2.12.3, bcrypt 3.1.1 installed. hash generated: $2b$12$gnCAOWLOJzx5Z4pudIv.9e2wkpJiTG/.P7cWc6y882QfS6IHLe7Ii\"}",
    "statusCode": 200
}

$ sls invoke -f world
{
    "body": "{\"input\": {}, \"message\": \"subprocess32 checks openssl version OpenSSL 1.0.1k-fips 8 Jan 2015\\n installed.\"}",
    "statusCode": 200
}
$ sls invoke -f vanilla
{
    "body": "{\"input\": {}, \"message\": \"is not touched by serverless-python-individually plugin\"}",
    "statusCode": 200
}
```

