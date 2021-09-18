# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
from User import User

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("test")

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



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    init(r"C:\Users\amyda\Documents\Rice University\hackrice11\config.json")
    something = input("Hi, say something! >>> ")
    print(something)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
