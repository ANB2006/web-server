#!/usr/bin/python3
from time import sleep
import cgitb
cgitb.enable()

print("Content-Type: text/html;charset=utf-8")
print()
while True:
    sleep(4)
    print("Hello World!")
