#!/usr/bin/env python3

import os
import re
import json
import requests


def set_folder(folder):
  if os.path.isdir(folder):
    iterate_files(os.path.join(os.getcwd(), folder))
  else:
    print("Folder not found")

def iterate_files(path):
  os.chdir(path)
  files = os.listdir(os.getcwd())
  print("working in:\n{}\nWill iterate through the following list of files\n{}".format(os.getcwd(),files))

  reviews = []

  for file in files:
    reviews.append(file_operation(file).copy())

  print(reviews)

def file_operation(file):
  review = {}
  full_content = open(file, "r")
  review["title"] = full_content.readline()
  review["user"] = full_content.readline()
  review["date"] = full_content.readline()
  user_text = full_content.readlines()
  text = ""
  if type(user_text) == list:
    for line in user_text:
      text = text + str(line)
  else:
    text = str(user_text)
  review["review"] = text
  print("Title is:\n{}\nSubmitted by {} on {}\nContent:\n{}".format(review["title"], review["user"], review["date"], review["review"]))
  full_content.close()
  return review


if __name__ == '__main__':
  set_folder(input("Please enter folder location to be processed: \n(This can be either an absolute path or a relative path)\n"))
