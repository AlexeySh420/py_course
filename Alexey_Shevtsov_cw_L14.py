# Lecture 14 04.29.2026

import json
import requests

url_api_comments = "https://dummyjson.com/comments"
result = requests.get(url_api_comments)
comments = result.json()
print(comments.get("comments")[7])


# Logging
import logging

my_logger = logging.getLogger()
log_handler = logging.FileHandler("my_logs.txt", "w", "utf-8")
log_handler.setLevel(logging.ERROR)
my_logger.addHandler(log_handler)

try:
    1 / 0
except ZeroDivisionError as e:
    my_logger.error(f"{e.args} Division by zero")
except:
    my_logger.critical("Something else")


# Config parser

import configparser

cfg = configparser.ConfigParser()
cfg.read("configs.txt")

for sec in cfg.keys():
    print(sec)

print()
print()

for sec, a in cfg.items():
    print(sec, a)
for pos in a.keys():
    print(" ", pos)
    print(" " * 8, cfg[sec][pos])
