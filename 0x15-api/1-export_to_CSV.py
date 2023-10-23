#!/usr/bin/python3
""" Export to CSV """

import csv
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
    with open("{}.csv".format(user_id), "w") as file:
        write = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            write.writerow([user_id, user.get("username"),
                            task.get("completed"), task.get("title")])
