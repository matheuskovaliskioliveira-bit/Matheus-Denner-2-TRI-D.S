class Sensor:
    def __init__(self):
        self.__temperatura = 0

    def set_temperatura(self, temperatura):
        if -50 <= temperatura <= 150:
            self.__temperatura = temperatura
        else:
            print("Temperatura inválida!")

    def get_temperatura(self):
        return self.__temperatura

    def status(self):
        if self.__temperatura <= 80:
            return "Normal"
        elif self.__temperatura <= 120:
            return "Alerta"
        else:
            return "Critico"

sensor = Sensor()

temperaturas = [25, 85, 121, -10]

for t in temperaturas:
    sensor.set_temperatura(t)
    print("Temperatura:", sensor.get_temperatura(), "-", sensor.status())