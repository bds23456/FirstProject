import pyowm
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('7a9a9583a439e56a2c6a0148d88a2e56', config_dict)
mgr = owm.weather_manager()
reg = owm.city_id_registry()

print(str(reg["CityIDRegistry"]))

place = input("В каком городе?: ")
id_of_city = int(reg.ids_for(place))
print(id_of_city)

#observation = mgr.weather_at_place(place)
#w = observation.weather

#print("В городе " + place + " сейчас " + w.detailed_status)
#print("И целых " + str(w.temperature('celsius')["temp"]) + " градусов")
