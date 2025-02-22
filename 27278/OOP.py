from math import radians, sin, cos, acos


class Point:
   def __init__(self, lat, lon):
       self.lat = lat
       self.lon = lon


   def distance(self, other):
       cos_d = sin(self.lat) * sin(other.lat) + cos(self.lat) * cos(other.lat) * cos(self.lon - other.lon)
       return 6371 * acos(cos_d)
      
class City:
    def __init__(self, lat, lon, name, population):
        self.point = Point(lat, lon)
        self.name = name
        self.population = population

    def city_distance(self, other_city):
        print(f'Расстояние между {self.name} и {other_city.name} -- {self.point.distance(other_city.point)}км')


moscow = City(55.755864, 37.617698, 'Москва', 12600000)
peter = City(59.938955, 30.315644, 'Санкт-Петербург', 5377503)
kazan = City(55.796127, 49.106414, 'Казань', 1259173)


moscow.city_distance(kazan)

