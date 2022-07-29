from datetime import datetime
import pytz

guatemala_timezone = pytz.timezone("America/Guatemala")
guatemala_date = datetime.now(guatemala_timezone)
print("Guatemala: ", guatemala_date.strftime("%d/%m/%Y, %H:%M:%S"))



mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
print("Mexico: ", mexico_date.strftime("%d/%m/%Y, %H:%M:%S"))



espania_timezone = pytz.timezone("Europe/Madrid")
espania_date = datetime.now(espania_timezone)
print("Madrid: ", espania_date.strftime("%d/%m/%Y, %H:%M:%S"))
