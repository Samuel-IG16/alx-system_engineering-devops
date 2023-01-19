#!/usr/bin/python3
"""Script that uses REST API"""
import json
import requests


def make_all(users=None, todos=None):
    """Turns all payloads into JSON format"""
    all_list = []
    alljson = {}
    with open("todo_all_employees.json", "w") as f:
        for i in users:
            u = i.get("id")
            for i in todos:
                if u == i.get("userId"):
                    all_list.append({"username": users[0].get("username"),
                                     "task": i.get("title"),
                                     "completed": i.get("completed")})
            alljson[u] = all_list
        json.dump(alljson, f)


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    make_all(users, todos)
