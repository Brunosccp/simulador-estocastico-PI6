from Temperature import Temperature
import Distributions
import random

class PopsicleCompany:
    def __init__(self, popsicles):
        self.profit = popsicles * -1
        self.popsiclesLeft = popsicles
        self.popsiclesSold = 0
        self.popsiclesNotSold = 0

    def simulateMonth(self, month):
        temperature = Temperature(month)

        for i in range(0,30):
            self.simulateDay(temperature.randomTemperature())


        print("""
        END OF MONTH:
        
        """,
        "\nTotal popsicles sold: ", self.popsiclesSold,
        "\nTotal popsicles left: ", self.popsiclesLeft,
        "\nTotal popsicles not sold: ", self.popsiclesNotSold,
        "\nProfit: ", self.profit)



    def simulateDay(self, temperature):
        avgPopsicle = self.avgPopsicleByTemperature(temperature)

        popsicleListPoisson = []

        for i in range(0, 145):
            popsiclesProb = Distributions.poisson(i, avgPopsicle)
            popsicleListPoisson.append(popsiclesProb)

        popsiclesDemand = self.randomPopsicles(popsicleListPoisson)
        self.sellPopsicles(popsiclesDemand)

    def randomPopsicles(self, popsicleListPoisson):
        x = random.randint(0, 10000000000) / 10000000000
        print(x)

        for i in range(0, len(popsicleListPoisson)):
            if(x < popsicleListPoisson[i]):
                print("quantidade de picoles: ", i)
                return i
            else:
                x -= popsicleListPoisson[i]

    def sellPopsicles(self, quantity):
        if(self.popsiclesLeft >= quantity):
            self.profit += quantity * 3
            self.popsiclesLeft -= quantity
            self.popsiclesSold += quantity
        elif(self.popsiclesLeft < quantity):
            self.profit += self.popsiclesLeft * 3
            self.popsiclesSold += self.popsiclesLeft
            self.popsiclesNotSold += quantity - self.popsiclesLeft
            self.popsiclesLeft = 0
        elif(self.popsiclesLeft == 0):
            self.popsiclesNotSold += quantity


    def avgPopsicleByTemperature(self, temperature):
        if(temperature >= 35):
            return 120
        elif(temperature == 34):
            return 110
        elif(temperature == 33):
            return 105
        elif(temperature == 32):
            return 100
        elif(temperature == 31):
            return 95
        elif(temperature == 30):
            return 90
        elif(temperature == 29):
            return 85
        elif(temperature == 28):
            return 80
        elif(temperature == 27):
            return 75
        elif(temperature == 26):
            return 70
        elif(temperature == 25):
            return 60
        elif(temperature == 24):
            return 50
        elif(temperature == 23):
            return 40
        elif(temperature == 22):
            return 35
        elif(temperature == 21):
            return 30
        elif(temperature == 20):
            return 25
        elif(temperature == 19):
            return 20
        elif(temperature == 18):
            return 17
        elif(temperature == 17):
            return 15
        elif(temperature == 16):
            return 13
        elif(temperature <= 15):
            return 10

