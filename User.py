import json

class User:
    data = {}
    name = ""
    year = ""
    major = ""
    hobbies = []
    temp = ""
    numPpl = 0
    schedule = ""
    bio = ""
    catchphrase = ""
    def __init__(self, data):
        print(data)
        self.data = data
        self.name = data.get("firstName") + " " + data.get("lastName")
        self.year = data.get("year")
        self.major = data.get("major")
        self.hobbies = data.get("hobbies")
        self.temp = data.get("temp")
        self.numPpl = data.get("numPpl")
        self.wake = data.get("wake")
        self.sleep = data.get("sleep")
        self.bio = data.get("bio")
        self.catchphrase = data.get("catchphrase")

    def toString(self):
        string = ""
        for key, value in self.data.items():
            string += key + ": " + str(value) + "\n"
        return string
