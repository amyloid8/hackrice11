# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
from User import User

yes = []

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("test")
    print("test2")

def init(config):

    with open(config, "r") as file:
        data = json.load(file)
    print(data)
    people = []
    for _ in data:
        person = User(data.get(_))
        people.append(person)
    for p in people:
        print(p.toString())

    return people

def selection(people):
    yes = []
    for person in people:
        response = input("Yes or no >>> ")
        if response == "yes":
            yes.append(person)
    return yes


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    people = init(r"C:\Users\amyda\Documents\Rice University\hackrice11\config.json")
    yesPeople = selection(people)
    for _ in yesPeople:
        print(_.toString())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
