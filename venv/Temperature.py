import Distributions
import random

#dicionario com a média de temperatura de cada mês
avgTemperatureByMonth = {
    "january" : 28,
    "february" : 29,
    "march" : 28,
    "april" : 26,
    "may" : 23,
    "june" : 23,
    "july" : 23,
    "august" : 24,
    "september" : 24,
    "october" : 26,
    "november" : 27,
    "december" : 28
}


class Temperature:
    def __init__(self, month):
        self.avgTemperature = avgTemperatureByMonth[month]
        self.popsicleByTemperature = []

        x = 0

        for i in range(0,51):
            x = Distributions.normal(i,self.avgTemperature,4)
            self.popsicleByTemperature.append(x)


        print(self.popsicleByTemperature[28])


    def randomTemperature(self):
        x = random.randint(0, 10000000000) / 10000000000
        print(x)

        for i in range(0, len(self.popsicleByTemperature)):
            if(x < self.popsicleByTemperature[i]):
                print("temperatura: ", i)
                return i
            else:
                x -= self.popsicleByTemperature[i]
