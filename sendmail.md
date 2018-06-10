## Send any email using python

For mail server, we use python's mail server which display any received emails on commandline.
```bash
python -m smtpd -n -c DebuggingServer localhost:8025
```

## Result

Client: 
```bash
$ python sendmail.py
```

Server:
```bash
$ python -m smtpd -n -c DebuggingServer localhost:8025
---------- MESSAGE FOLLOWS ----------
X-Peer: 127.0.0.1

FROM: admin@fake.host
TO: admin@localhost
SUBJECT: Test

A text sent with Python's smtplib
------------ END MESSAGE ------------

```

## [<< Back to main page](https://github.com/jockerz/Koleksi) 

