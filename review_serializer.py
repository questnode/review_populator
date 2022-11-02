#!/usr/bin/env python3

import os
import requests

def set_folder(folder):
  # If folder is found, start iteration function, if not, alert user.
  if os.path.isdir(folder):
    iterate_files(os.path.join(os.getcwd(), folder))
  else:
    print("Folder not found")

def iterate_files(path):
  # Set current working folder
  # Scan current working folder for a list of files to be worked on
  os.chdir(path)
  files = os.listdir(os.getcwd())
  print("working in:\n{}\nWill iterate through the following list of files\n{}".format(os.getcwd(),files))

  # Each file in the working folder is passed to operation function to be processed
  for file in files:
    # Expect to receive back a dictionary variable in the proper format: title, name, date, feedback
    # The returned dictionary is posted to the url previously entered by user
    response = requests.post(url, data=file_operation(file))

def file_operation(file):
  # Each file is parsed into a dictionary as title, name, date, feedback
  # dictionary is returned to function caller
  review = {}
  full_content = open(file, "r")
  review["title"] = full_content.readline()
  review["name"] = full_content.readline()
  review["date"] = full_content.readline()
  user_text = full_content.readlines()

  # Process the last block in the file content.
  # In case there are multiple lines or pure numbers, convert into a single string var
  text = ""
  if type(user_text) == list:
    for line in user_text:
      text = text + str(line)
  else:
    text = str(user_text)

  # Final single string var is stored in the dicionary
  review["feedback"] = text

  # for debugging:
  #print("Title is:\n{}\nSubmitted by {} on {}\nContent:\n{}".format(review["title"], review["name"], review["date"], review["feedback"]))
  full_content.close()
  return review


if __name__ == '__main__':
  # Ask for user input on posting url and working folder
  # Pass the folder variable into set_folder function for verification
  global url
  url = input("Enter the URL for posting data:\n")
  set_folder(input("Please enter folder location to be processed: \n(This can be either an absolute path or a relative path)\n"))
