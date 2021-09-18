import uuid


class User:

    def __init__(self, data):
        print(data)
        self.data = data
        self.uuid = uuid.uuid4()
        self.name = data.get("firstName") + " " + data.get("lastName")
        self.picture = data.get("picture")
        self.year = data.get("year")
        self.major = data.get("major")
        self.hobbies = data.get("hobbies")
        self.temp = data.get("temp")
        self.numPpl = data.get("numPpl")
        self.wake = data.get("wake")
        self.sleep = data.get("sleep")
        self.bio = data.get("bio")
        self.catchphrase = data.get("catchphrase")
        self.email = data.get("email")

    def getid(self): return self.uuid

    def setName(self, name2): self.name = name2
    def setPicture(self, pic2): self.picture = pic2
    def setYear(self, year2): self.year = year2
    def setMajor(self, major2): self.major = major2
    def setHobbies(self, hobbies2): self.hobbies = hobbies2
    def setTemp(self, temp2): self.temp = temp2
    def setPpl(self, ppl2): self.numPpl = ppl2
    def setWake(self, wake2): self.wake = wake2
    def setSleep(self, sleep2): self.sleep = sleep2
    def setBio(self, bio2): self.bio = bio2
    def setPhrase(self, phrase2): self.catchphrase = phrase2
    def setEmail(self, email2): self.email = email2

    def toString(self):
        string = ""
        for key, value in self.data.items():
            string += key + ": " + str(value) + "\n"
        return string
