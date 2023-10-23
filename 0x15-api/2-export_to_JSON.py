#!/usr/bin/python3
""" Export to CSV """

import json
import requests
from sys import argv


if __name__ == "__main__":
    """Export to CSV """

    # Fetching the employee's name
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    tasks = requests.get(url + "todos", params={"userId": user_id}).json()
    res = requests.get(url)

    # Saving data as a file
    with open("{}.json".format(user_id), "w") as file:
        for task in tasks:
            json.dump({user_id: [{
             "task": task.get('title'),
             "completed": task.get('completed'),
             "username": task.get('username')
            }]}, file)
