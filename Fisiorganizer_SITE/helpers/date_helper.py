import datetime

# retrieve named day of the week
def getDayOfWeek():
    today = datetime.date.today()
    days = ["segunda-feira", 
            "terça-feira", 
            "quarta-feira", 
            "quinta-feira", 
            "sexta-feira", 
            "sábado", 
            "domingo"
            ]   
    dayNumber = today.weekday()
    dayOfWeek = days[dayNumber]

    return dayOfWeek