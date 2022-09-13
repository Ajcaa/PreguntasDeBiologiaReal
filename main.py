#Constantes de los colores, las constantes son como las variables pero no se pueden modificar despues, son fijos. Siempre en mayusculas

GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RED = '\033[31m'
RESET = '\033[39m'


import time #

import random # Importamos la librería random


iniciar_trivia = True 
intentos = 0

nombre = input("Antes de seguir necesito que coloques su nombre: ")

print(CYAN+"\nHola", nombre,"espero que estes preparado para responder 5 preguntas de Biologia, presione Enter para enviar cada alternativa."+RESET)


input("\nPresione Enter para iniciar: ")

numero = 5
for i in range(numero):
  print(numero)
  time.sleep(1)
  numero -= 1
if numero == 0:
  print(GREEN+"Empezemos!"+RESET)


#EMPIEZA LA TRIVIA

while iniciar_trivia == True:
  intentos += 1 #
  puntaje = random.randint(0, 50) 
  #print(GREEN+"Este es tu intento numero"+RESET, intentos)
            

  input("\nPresione Enter para continuar: ")
  print("Cargando...")
  time.sleep(1)   #Recordar que las funciones deben estar Dentro del While, osea 1 Tab a la derecha
  print(GREEN+"Este es tu intento numero"+RESET, intentos)
  print(CYAN+"Empezaras con un puntaje aleatorio de"+RESET, puntaje, CYAN+"puntos, ¿podras conseguir 1000 puntos?"+RESET)
  input("\nPresione Enter para continuar: ")
  print("Cargando...")
  time.sleep(1)


  
  #La pregunta 1 nos daras puntos al azar
  print(BLUE+"\n1.Las glándulas de Brunner, que se hallan en el duodeno, permiten:"+RESET)
  print(YELLOW+"a)Realizar la digestión de las grasas.")
  print("b)Permitir la activación de las diferentes enzimas.")
  print("c)Estimular el peristaltismo intestinal.")
  print("d)Neutralizar la acidez del contenido gástrico.")
  print("e)Ser una sustancia que inhibe a las bacterias."+RESET)

  respuesta_1 = input("Tu respuesta: ").lower()
  
  while respuesta_1 not in ("a","b","c","d","e","x"):
   respuesta_1 = input(RED+"Esa clave no existe, por favor ingrese alguna nuevamente: "+RESET).lower()
  
  if respuesta_1 == "a":
     puntaje -= random.randint(10, 30)
     print(MAGENTA+"Incorrecto! \nLa digestion de las grasas lo hace la Bilis.\nPerdistes puntos extra al azar"+RESET)
  elif respuesta_1 == "b":
    puntaje -= random.randint(10, 30)
    print(MAGENTA+"Incorrecto! \nEl HCI del estomago llega a activar una enzima inactiva, el Pepsinogeno.\nPerdistes puntos al azar"+RESET)
  elif respuesta_1 == "c":
    puntaje -= random.randint(10, 30)
    print(MAGENTA+"Incorrecto! \nEl peristaltismo intestinal transforma el Quimo a Quilo en el intestino delgado,alli termina la Digestion de Alimentos.\nPerdistes puntos al azar"+RESET)
  elif respuesta_1 == "e":
    puntaje -= random.randint(10, 30)
    print(MAGENTA+"Incorrecto! \nInhibir bacterias, por ejemplo, es la funcion de las Placas de Peyer en el Intestino Delgado.\nPerdistes  puntos al azar"+RESET)
  elif respuesta_1 == "x":
    puntaje += 100
    print(GREEN+"Wow, distes a una letra secreta. \nDe recompensa tome 100 puntos"+RESET)
    
  else:
   puntaje += random.randint(20, 50) #ganaras puntos al azar en ese rango
   print(GREEN+"Muy bien!!", nombre, "\nLas glandulas de Brunner se encuentran en la Mucosa Duodenal (Intestino delgado).\nHas ganado puntos extra al azar"+RESET)
    
  print("Tu puntaje ahora:",puntaje,"puntos")
  
  #Fin pregunta 1
  input("\nPresione Enter para continuar: ")
  print("Cargando...")
  time.sleep(1)


#La pregunta 2 nos dara Puntos exactos
  print(BLUE+"\n2.Respecto a las glándulas gástricas, en cual de ellas se elabora la hormona gastrina:"+RESET)
  
  print(YELLOW+"a)Glándulas del cardias.")
  print("b)Glándulas del fondo y cuerpo.")
  print("c)Glándulas fúndicas.")
  print("d)Glándulas pilóricas.")
  print("e)Glándulas de Brúnner"+RESET)
  
  respuesta_2 = input("Tu respuesta: ").lower()
  
  while respuesta_2 not in ("a","b","c","d","e","x"):
   respuesta_2 = input(RED+"Esa clave no existe, por favor ingrese alguna nuevamente: "+RESET).lower()
  
  if respuesta_2 == "a":
    puntaje -= 10
    print(MAGENTA+"Incorrecto! \nLas Glandulas cardias secretan Mucus en el Estomago.\nPerdistes 10 puntos"+RESET)
  elif respuesta_2 == "b":
    puntaje -= 10
    print(MAGENTA+"Incorrecto! \nLas Glandulas del fondo y cuerpo (del estomago) vienen a ser las glandulas fundicas. \nPerdistes 10 puntos"+RESET)
  elif respuesta_2 == "c":
    puntaje -= 10
    print(MAGENTA+"Incorrecto! \nLas glandulas fundicas tienen diversas celulas,las celulas principales secretan Pepsinogeno y Lipasa gastrica. \nPerdistes 10 puntos"+RESET)
  elif respuesta_2 == "e":
    puntaje -= 10
    print(MAGENTA+"Incorrecto! \nLas Glandulas de Brunner estan en el Intestino Delgado. \nPerdistes 10 puntos"+RESET)
  elif respuesta_2 == "x":
    puntaje += 100
    print(GREEN+"Solo por presionar x, has ganado 100 puntos extra"+RESET)
  else:
    puntaje += 20
    print(GREEN+"Muy bien", nombre,"\nEstas estimulan el HCI del estomago y genera el Peristaltismo. \nHas ganado 20 puntos"+RESET)
  
  print("Tu puntaje ahora:",puntaje,"puntos")  
  
  input("\nPresione Enter para continuar: ")
  print("Cargando...")
  time.sleep(1)

  
  #Pregunta 3 usara signos aritmeticos para dar o quitarnos puntos de acuerdo a la respuesta
  print(BLUE+"\n3.Es un tipo de célula que se encuentra dentro de las glándulas gástricas; excepto:"+RESET)
  print(YELLOW+"a)Mucosas")
  print("b)Oxínticas o parietales")
  print("c)Paneth")
  print("d)Principales") 
  print("e)Argentafines"+RESET)#Siempre el print dejando un espacio aqui
  
  respuesta_3 = input("Tu respuesta: ").lower()
  
  while respuesta_3 not in ("a", "b", "c", "d", "e", "x"):
    respuesta_3 = input(RED+"Esa clave no existe, por favor ingrese alguna nuevamente: "+RESET).lower()
  
  if respuesta_3 == "a":
    print(MAGENTA+"Incorrecto!!", nombre,"\nLas celulas mucosas son tambien llamadas celulas mucigenas.Estan en las Glandulas Fundicas.\nPierdes 5 puntos"+RESET)
    puntaje = puntaje - 5 #recuerda solo usar un = no dos
    
  elif respuesta_3 == "b":
    print(MAGENTA+"Incorrecto!! \nLas celulas parietales de las Glandulas Fundicas secretan HCI y el Factor intrinseco.\nPierdes 2 puntos"+RESET)
    puntaje = puntaje - 2
  
  elif respuesta_3 == "c": #una forma diferente de colocar la respuesta correcta en lugar de usar ELSE
    print(GREEN+"Muy bien!! \nSon Celulas Intestinales que se encuentran en las Glándulas de Lieberkuhn.\nTu puntaje se multiplicara por Dos como recompensa", nombre+RESET)
    puntaje = puntaje * 2
  
  elif respuesta_3 == "d":
    print(MAGENTA+"Muy mal!! \nLas células principales, parte de las Glandulas Fundicas, secretan Pepsinogeno y Lipasa Gastrica.\nPierdes 15 puntos."+RESET)
    puntaje = puntaje - 15
  
  elif respuesta_3 == "e":
    print(MAGENTA+"Pesimo!! \nLas celulas Argentafines estan presentes en el tracto gastrointestinal, secretan Serotonina.\nTu puntaje se reduce en la mitad (Se redondeara el numero si es necesario)."+RESET)
    puntaje = puntaje // 2

  elif respuesta_3 == "x":
    puntaje += random.randint(10, 100)
    print(GREEN+"Clave Secreta.\nPuntos al azar para usted"+RESET)
  
  
  
  
  print("Tu puntaje ahora:", puntaje, "puntos")
  
  input("\nEn la siguiente pregunta podrias ganar puntos extras respondiendo x. Intentalo!\nPresione Enter para continuar: ")
  print("Cargando...")
  time.sleep(1)


  #La pregunta 4 nos daras puntos al azar
  print(BLUE+"\n4.Estructura respiratoria que no tiene cartílago "+RESET)
  print(YELLOW+"a)Laringe")
  print("b)Nariz")
  print("c)Bronquiolos.")
  print("d)Traquea")
  print("e)Bronquios"+RESET)

  respuesta_4 = input("Tu respuesta: ").lower()
  
  while respuesta_4 not in ("a","b","c","d","e", "x"):
   respuesta_4 = input(RED+"Esa clave no existe, por favor ingrese alguna nuevamente: "+RESET).lower()
  
  if respuesta_4 == "a":
     puntaje -= random.randint(40, 70)
     print(MAGENTA+"Incorrecto! \nLa Laringe esta constituida por cartilagos impares (epiglotis, tiroides, cricoides) y cartilagos pares (aritenoides, corniculados, cuneiformes.\nPerdistes puntos al azar"+RESET)
  elif respuesta_4 == "b":
    puntaje -= random.randint(10, 30)
    print(MAGENTA+"Incorrecto! \nLa nariz tiene cartílago en su parte delantera.\nPerdistes puntos al azar"+RESET)
  elif respuesta_4 == "d":
    puntaje -= random.randint(10, 30)
    print(MAGENTA+"Incorrecto! \nEn la Tráquea encontramos al cartílago hialino.\nPerdistes puntos al azar"+RESET)
  elif respuesta_4 == "e":
    puntaje -= random.randint(10, 30)
    print(MAGENTA+"Incorrecto! \nEn los bronquios encontramos el cartílago hialino.\nPerdistes puntos al azar"+RESET)
  elif respuesta_4 == "x":
    puntaje += 200
    print(GREEN+"Presionastes una tecla secreta. \nDe recompensa tome 200 puntos"+RESET)
  else:
    puntaje += random.randint(50, 70) #ganaras puntos al azar en ese rango
    print(GREEN+"Muy bien!!", nombre, "\nLos bronquiolos no tienen cartilago.\nHas ganado puntos al azar"+RESET)
    
  print("Tu puntaje ahora:",puntaje,"puntos")
  
  #Fin pregunta 4
  input("\nPresione Enter para continuar: ")
  print("Cargando...")
  time.sleep(1)


  #Pregunta 5 usara multiplicacion y restas para dar o quitarnos puntos de acuerdo a la respuesta
  print(BLUE+"\n5.Son conformantes del pedículo pulmonar; excepto:"+RESET)
  print(YELLOW+"a)Vena pulmonar")
  print("b)Bronquios principales")
  print("c)Arteria pulmonar")
  print("d)Sacos alveolares") 
  print("e)Arteria bronquial"+RESET)#Siempre el print dejando un espacio aqui
  
  respuesta_5 = input("Tu respuesta: ").lower()
  while respuesta_5 not in ("a", "b", "c", "d", "e", "x"):
    respuesta_5 = input(RED+"Esa clave no existe, por favor ingrese alguna nuevamente: "+RESET).lower()
  
  if respuesta_5 == "a":
    print(MAGENTA+"Incorrecto!!\nLa vena pulmonar lleva sangre con oxígeno de los pulmones al corazón.\nPierdes 50 puntos"+RESET)
    puntaje = puntaje - 50 #recuerda solo usar un = no dos
    
  elif respuesta_5 == "b":
    print(MAGENTA+"Incorrecto!!\nLos bronquios principales se dirigen desde el final de la tráquea hasta los hilios pulmonares por donde penetran en los pulmones.\nPierdes 25 puntos"+RESET)
    puntaje = puntaje - 25
  
  elif respuesta_5 == "c": #una forma diferente de colocar la respuesta correcta en lugar de usar ELSE
    print(MAGENTA+"Muy mal!! \nLa arteria pulmonar transporta la sangre del ventrículo derecho del corazon a los pulmones.\nPierdes 75 puntos"+RESET)
    puntaje = puntaje - 75
  
  elif respuesta_5 == "e":
    print(MAGENTA+"Muy mal!! \nLa arteria bronquial llevan sangre oxigenada a los pulmones.\nPierdes 15 puntos"+RESET)
    puntaje = puntaje - 15
  
  elif respuesta_5 == "d":
    print(GREEN+"Muy bien!! \nAdemas, los sacos alveolares poseen numerosos alvéolos donde se realiza el intercambio de oxigeno\nSe te duplicara tu puntaje."+RESET)
    puntaje = puntaje * 2

  elif respuesta_5 == "x":
    puntaje += random.randint(25, 75)
    print(GREEN+"Pulsastes una tecla con opción secreta.\nRecibiras puntos al azar."+RESET)
  
  #fin de las preguntas, ahora ejercicios
  
  
  print("Tu puntaje ahora", puntaje, "puntos")
  
  input("\nPresione Enter para continuar: ")
  print("Cargando...")
  time.sleep(1)

#LISTA DE PUNTOS EXTRAS
  
  print(YELLOW+"\nAhora recibiras puntos extra, hay 5 opciones: 10, 40, 50, 100, 500"+RESET)
  puntitos = [10, 40, 50, 100, 500]
  def selectrandom(puntitos):
    return random.choice(puntitos)

  v = selectrandom(puntitos)  

  input(YELLOW+"Pulse Enter para probar su suerte: "+RESET)

  print("Cargando...")
  time.sleep(1)
  
  
  print(YELLOW+"\nFelicidades!, has ganado", v, "puntos"+RESET)  

  puntaje += v

  input("\nPresione Enter para continuar: ")
  print("Cargando...")
  time.sleep(1)

  #DESPEDIDA DE PREGUNTAS
  print(GREEN+"\nGracias por jugar", 
nombre,"su puntaje final es de", 
puntaje,"puntos."+RESET) 

  print(BLUE+"\nDeseas realizar la Trivia otra vez?"+RESET)
  repetir_trivia = input(BLUE+"Envie un si para repetir o cualquier tecla para finalizar la Trivia: "+RESET).lower() #para forzar minuscula
  
  if repetir_trivia != "si": #!= significa desigual
   print(GREEN+"\nGracias por jugar la Trivia", nombre, "tenga un buen dia."+RESET)#No me funciona con el nombre al final
   iniciar_trivia = False #MUY IMPORTANTE para que al presionar cualquier letra no vuelva a repetir las preguntas de Biologia
                     