# affiche heure, minute, seconde
from datetime import datetime
import time
now = datetime.now()
t = now.strftime('%H:%M:%S')
print('Il est : ',t)

# actualise toutes les secondes et sur la même ligne avec \r
def displaysec():
    while True:
        localtime = time.localtime()
        result = time.strftime('%H:%M:%S', localtime)
        print(f'{result}', end='\r')
        time.sleep(1)

# choisit l'heure et l'affiche
def afficher_heure():
    global hour, minute, second
    hour = int(input("Entrez l'heure: "))
    minute = int(input("Entrez les minutes: "))
    second = int(input("Entrez les secondes: "))
    
# permet de choisir soit d'avancer, soit de reculer l'heure
#from datetime import timedelta
#now = datetime.now()
#now_plus_4_hours_12_minutes = now + timedelta(hours= +4, minutes = +12)
#print(now)
#print(now_plus_4_hours_12_minutes)

# alarme et message
# en cas d'erreur, définit si le format rempli est valide
def validate_time(alarm_time): # alarm_time est l'entrée de l'utilisateur
    if len(alarm_time) != 11:
        return "Format temps invalide! Recommencez..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Format HEURE invalide! Recommencez..."
        elif int(alarm_time[3:5]) > 59:
            return "Format MINUTE invalide! Recommencez..."
        elif int(alarm_time[6:8]) > 59:
            return "Format SECONDE invalide! Recommencez..."
        else:
            return "ok"
# appelle la fonction
while True:
# demande l'heure de l'alarme
    alarm_time = input("Entrez l_heure dans le format 'HH:MM:SS AM/PM': ")
    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f'Alarme pour {alarm_time}...')
        break
# stocke séparément les valeurs dans des variables spécifiques
alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()
# définit l'heure actuelle
while True:
    now = datetime.now()
    current_hour = now.strftime('%I') # les données sont en 12h
    current_min = now.strftime('%M')
    current_sec = now.strftime('%S')
    current_period = now.strftime('%p') # avec AM/PM
# si les données de l'utilisateur et celles actuelles correspondent
# alors mon message "C'est l'heure!" s'affiche
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("C'est l'heure!")
                    break

def pause():
# met en pause l'horloge et reprend après 10 secondes
    #time.sleep(10)
    #print("La pause est finie!")

# l'horloge ne reprend que si la touche entrée est appuyée
    i = input("Tapez Enter pour continuer: ")
    print(i)
afficher_heure()
pause()
displaysec()