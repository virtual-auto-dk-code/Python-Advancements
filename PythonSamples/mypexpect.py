import sys

import pexpect

try:
    print("Hello")
    file = open('mylog.txt', 'a')
    child = pexpect.spawn("ls", encoding='utf8')
    child.logfile = file
    print(child.read())
    child.expect(pexpect.EOF, timeout=None)

    child = pexpect.spawn("pwd", encoding='utf8')
    child.logfile = file
    print(child.read())
    child.expect(pexpect.EOF, timeout=None)

    child.logfile.close()
    status = True  # If serial number of Cert retrieved then True else False
except Exception as e:
    print(str(e))
    raise
