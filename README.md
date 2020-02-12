# qsub_HelloWorld
## quick setup tutorial

Step0:
Log in your ntugrid5 account, find a working directory, and then execute the command:
```
$ git clone git@github.com:ywkao/qsub_HelloWorld.git
```

Step1:
In submitJOB.py, set up the directories for output messages well.
i.e. change the user name to yours and ensure the corresponding directories exist.

```
defaultStorageFolder='/home/ykao/qjob/qSubResult/'
defaultMessageFolder='/home/ykao/qjob/qSubMessage/'
defaultErrorFolder  ='/home/ykao/qjob/qSubMessage/'
USER='ykao'
```

Step2:
Simply type the command below for submission test.
```
$ ./qsubMultiJob.py 2017
```
