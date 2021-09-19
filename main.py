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
    for person in people:
        print(person.toString())
        response = input("Yes or no >>> ")
        if response == "yes":
            yes.append(person)
    me["yes"] = yes
    return yes

def match(me, people):
    return



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    people = init(r"C:\Users\amyda\Documents\Rice University\hackrice11\config.json")

    me = r"C:\Users\amyda\Documents\Rice University\hackrice11\config_template.json"
    with open(me) as file:
        me = json.load(file)
    for key in me:
        me[key] = input(key + "? >>> ")
    print(me)

    yesPeople = selection(people)
    for _ in yesPeople:
        print(_.toString())




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
