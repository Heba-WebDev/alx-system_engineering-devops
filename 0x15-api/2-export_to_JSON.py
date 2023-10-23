#!/usr/bin/python3
""" Export to JSON """

import json
import requests
from sys import argv


if __name__ == "__main__":
    """Export to JSON """

    # Fetching the employee's name
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    tasks = requests.get(url + "todos", params={"userId": user_id}).json()

    # Saving data as a file
    with open("{}".format(user_id), "w") as file:
        json.dump({user_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
            } for task in tasks]}, file)
