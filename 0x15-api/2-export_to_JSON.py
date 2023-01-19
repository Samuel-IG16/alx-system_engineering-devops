#!/usr/bin/python3
"""Script that uses REST API"""
import json
import requests
import sys


def make_json(users=None, todos=None, u=None):
    """Turns payloads into CSV format"""
    all_list = []
    with open(sys.argv[1] + ".json", "w") as f:
        for i in todos:
            all_list.append({"task": i.get("title"),
                             "completed": i.get("completed"),
                             "username": users[0].get("username")})
        alljson = {str(u): all_list}
        json.dump(alljson, f)


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        args_id = {"id": sys.argv[1]}
        users = requests.get("https://jsonplaceholder.typicode.com/users",
                             params=args_id).json()
        args_userid = {"userId": sys.argv[1]}
        todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                             params=args_userid).json()

        make_json(users, todos, sys.argv[1])
