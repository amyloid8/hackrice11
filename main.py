# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("test")

def init(config):
    data = {}
    with open(config) as file:
        data = json.load(file)
    print(data)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    init(r"C:\Users\amyda\Documents\Rice University\hackrice11\config.json")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
