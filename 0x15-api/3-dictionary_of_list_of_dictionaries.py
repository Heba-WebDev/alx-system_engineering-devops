#!/usr/bin/python3
""" Save data as a dictionary """

import json
import requests
from sys import argv


if __name__ == "__main__":
    """ Save data a dictionary """
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()
    all_data = {}

    for user in users:
        user_id = user.get('id')
        url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            user_id)
        tasks = requests.get(url).json()
        todo_list = []

        for task in tasks:
            task_dict = {}
            task_dict["username"] = user.get("username")
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            todo_list.append(task_dict)

        all_data[user_id] = todo_list

        with open("todo_all_employees.json", "w") as file:
            json.dump(all_data, file)
