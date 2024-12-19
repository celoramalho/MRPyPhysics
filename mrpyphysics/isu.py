class Isu: #conversion unit to International System of Units
    def __init__(self):
        pass

    #length
    def milimeters(self, value):
        return value / 1000
    def centimeters(self, value):
        return value / 100
    def decimeters(self, value):
        return value / 10
    def meters(self, value):
        return value
    def decameters(self, value):
        return value * 10
    def hectometers(self, value):
        return value * 100
    def kilometers(self, value):
        return value * 1000
    
    #time
    def seconds(self, value):
        return value
    def minutes(self, value):
        return value * 60
    def hours(self, value):
        return value * 3600
    def days(self, value):
        return value * 86400
    def months(self, value):
        return value * 2592000
    def years(self, value):
        return value * 31536000
    def decades(self, value):
        return value * 3155673600
    def centuries(self, value):
        return value * 31556736000
    
    #mass
    def grams(self, value):
        return value / 1000
    def kilograms(self, value):
        return value
    
