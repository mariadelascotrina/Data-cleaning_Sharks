import re 

def suma(a,b):
    return a +b



def convierteaint (x):
    return int(x)




def omiteceros(x):
    if x <  1700:
        return 1700
    else:
        return x


def homogeneizarfatal(x):
    if x == 'N' or x == ' N' or x == 'N ':
        return 'N'
    if  x == 'Y' or x == 'y':
        return 'Y'
    else:
        return 'Unkown'

def homogeneizarActivity(x): #hemos observado que los valores más comunes son los que aparecen al principio del value counts por eso nos quedamos solo con ellos. El resto van a other
    if x =='Surfing':
        return 'Surfing'
    if x == 'Swimming':
        return 'Swimming'
    if x == 'Fishing':
        return 'Fishing'
    if x == 'Spearfishing':
        return 'Spearfishing'
    if x == 'Bathing':
        return 'Bathing'
    else:
        return 'Other'

def homogeneizarpaises(x): 
    if x == 'USA':
        return 'USA'
    if x == 'AUSTRALIA':
        return 'AUSTRALIA'
    if x == 'SOUTH AFRICA':
        return 'SOUTH AFRICA'
    if x == 'PAPUA NEW GUINEA':
        return 'PAPUA NEW GUINEA'
    if x == 'NEW ZEALAND':
        return 'NEW ZEALAND'
    else:
        'OTHER'

def homogeneizarType(x):
    if x == 'Boating' or x == 'Unprovoked' or x == 'Sea Disaster' or x =='Boat' or x == 'Boatomg' :
        return 'Unprovoked'
    if x == 'Provoked':
        return 'Provoked'
    else:
        return 'Questionable'

def mesBea (x): #así conseguimos los meses
    X = str(x)
    for i in x:
        if "Jan" in x:
            return "January"
        elif "Feb" in x:
            return "February"
        elif "Mar" in x:
            return "March"
        elif "Apr" in x:
            return "April"
        elif "May" in x:
            return "May"
        elif "Jun" in x:
            return "Juny"
        elif "Jul" in x:
            return "July"
        elif "Aug" in x:
            return "August"
        elif "Sep" in x:
            return "September"
        elif "Oct" in x:
            return "October"
        elif "Nov" in x:
            return "November"
        elif "Dec" in x:
            return "December"
        else:
            return "Other"