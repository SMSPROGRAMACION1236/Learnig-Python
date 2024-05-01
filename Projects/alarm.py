import os

import time
from playsound import playsound
def alarm(minutes, seconds):
  sound_path =os.path.join( os.path.dirname(__file__),"serious-dark-ambient-atmosphere.mp3")
  total_seconds= minutes * 60 + seconds
  print(f"La alarma sonara en {minutes} y {seconds} segundos")
  time.sleep(total_seconds)
  playsound(sound_path)
  
minutes = int(input("Ingresa los minutos de la alarma: "))

seconds = int(input("Ingresa los segundos de la alarma: "))
alarm(minutes, seconds)