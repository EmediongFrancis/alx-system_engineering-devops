#!/usr/bin/python3

'''
    Exports data from an API and stores as a JSON file.
'''

if __name__ == "__main__":
    import json
    from requests import get

    User = "https://jsonplaceholder.typicode.com/users?id={}".format(id)
    Todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(id)

    user = get(User)
    todo = get(Todo)

    try:
        Employee = user.json()
        Tasks = todo.json()
    except ValueError:
        print("Not a valid JSON.")

    if Employee and Tasks:
        data = {}
        userNames = {}
        for user in userNames:
            userID = user.get("id")
            userName = user.get("username")
            data[userID] = []
            userNames[userID] = userName

        for task in Tasks:
            TaskStatus = task.get("completed")
            TaskTitle = task.get("title")
            uID = task.get("userId")
            dictInfo = {
                "task": TaskTitle,
                "completed": TaskStatus,
                "username": userNames.get(uID)
            }
            if data.get(uID):
                data.get(uID).append(dictInfo)

        with open("todo_all_employees.json", "w", newline='') as jsonfile:
            json.dump(data, jsonfile)
