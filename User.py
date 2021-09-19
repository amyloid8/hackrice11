import uuid


class User:

    def __init__(self, data):
        print(data)
        self.data = data
        self.name = data.get("Name")
        self.picture = data.get("picture")
        self.year = data.get("year")
        self.major = data.get("major")
        self.temp = data.get("temp")
        self.numPpl = data.get("numPpl")
        self.schedule = data.get("schedule")
        self.bio = data.get("bio")
        self.email = data.get("email")

    def setName(self, name2): self.name = name2
    def setPicture(self, pic2): self.picture = pic2
    def setYear(self, year2): self.year = year2
    def setMajor(self, major2): self.major = major2
    def setTemp(self, temp2): self.temp = temp2
    def setPpl(self, ppl2): self.numPpl = ppl2
    def setSchedule(self, s2): self.schedule = s2
    def setBio(self, bio2): self.bio = bio2
    def setEmail(self, email2): self.email = email2

    def toString(self):
        string = ""
        for key, value in self.data.items():
            string += key + ": " + str(value) + "\n"
        return string
