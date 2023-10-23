#!/usr/bin/python3
"""Gather data from an API"""

import requests
from sys import argv


if __name__ == "__main__":
    """Gather data from an API"""

    # Fetching the employee's name
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    res = requests.get(url)

    name = res.json().get('name')

    # Fetching the todos
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            argv[1]
    )
    res = requests.get(url)

    tasks = res.json()
    total = len(tasks)
    done = [task for task in tasks if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(name, len(done),
                                                          total))
    for task in done:
        print("\t {}".format(task.get('title')))
