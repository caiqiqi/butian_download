#coding=utf-8
import os
import re


pwd = os.getcwd()
PATTERN = ur"(.*?)漏洞"
pattern = re.compile(PATTERN)

try:
    for root, dirs, result in os.walk(pwd):
        for i in result:
             with open(i, 'r')as f:
                 content = f.read()
                 matched = pattern.search(content)
                 #matched = re.findall(pattern, content)
                 if matched:
                     print matched.group(1)
except KeyboardInterrupt:
    pass
