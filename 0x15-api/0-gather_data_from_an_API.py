#!/usr/bin/python3
"""Script that uses REST API"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        args = {"id": sys.argv[1]}
        users = requests.get("https://jsonplaceholder.typicode.com/users",
                             params=args).json()
        args = {"userId": sys.argv[1]}
        todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                             params=args).json()
        todos_len = 0
        todos_arr = []
        for i in todos:
            if i.get("completed"):
                todos_arr.append(i)
                todos_len += 1

        print("Employee {} is done with tasks({}/{}):".format(
              users[0].get("name"), todos_len, len(todos)))

        for i in todos_arr:
            print("\t {}".format(i.get("title")))
