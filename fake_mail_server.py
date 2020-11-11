#!/usr/bin/python3 

import argparse
import smtpd
import asyncore

parser = argparse.ArgumentParser()
parser.add_argument('port', type=int, help="PORT (1587 is recomended)")
parser.add_argument('-b', '--bind', help="Host address",
                    action='store', default='localhost')


class FakeSMTPServer(smtpd.SMTPServer):
    """A Fake smtp server"""

    def __init__(*args, **kwargs):
        print("Running fake smtp server on port 1587")
        smtpd.SMTPServer.__init__(*args, **kwargs)

    def process_message(*args, **kwargs):
        pass

if __name__ == "__main__":
    args = parser.parse_args()
    smtp_server = FakeSMTPServer((args.bind, args.port), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        smtp_server.close()
