# aojcli
AOJ submission tools on CLI  
[AIZU ONLINE JUDGE](http://judge.u-aizu.ac.jp/)

## System requirements
- Python 2.7

## Setup
aojcli get credential from environment variables.  
You need to set your user id and password to environment variables.
```
$ git clone https://github.com/kamaboko123/aojcli.git
$ cd aojcli
$ echo 'export AOJCLI_ID=your_user_id_of_AOJ' >> ~/.bachrc
$ echo 'export AOJCLI_PASSWORD=your_password_of_AOJ' >> ~/.bachrc
```

### Command

#### submit
example :
```
$ ./aojcli.py submit ITP1_1_A C ITP1_1_A.c
```

