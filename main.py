#Constantes de los colores, las constantes son como las variables pero no se pueden modificar despues, son fijos. Siempre en mayusculas

from Alternativas import pregunta1, pregunta2, pregunta3, pregunta4, pregunta5


GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RED = '\033[31m'
BIBlack= '\033[90m'
BGMAGENTA= '\033[45m'
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
 
            
  input("\nPresione Enter para continuar: ")
  print("Cargando...")
  time.sleep(1)   #Recordar que las funciones deben estar Dentro del While, osea 1 Tab a la derecha
  print(GREEN+"\nEste es tu intento numero"+RESET, intentos)
  print(CYAN+"Empezaras con un puntaje aleatorio de"+RESET, puntaje, CYAN+"puntos, ¿podras conseguir 1000 puntos?"+RESET)
  input("\nPresione Enter para continuar: ")
  print("Cargando...")
  time.sleep(1)


  
  #----------------La pregunta 1 nos daras puntos al azar--------------

  print(BLUE+"\n1.Las glándulas de Brunner, que se hallan en el duodeno, permiten:"+RESET)
  for i in range (len(pregunta1)):
    alter = pregunta1[i]
    print(YELLOW+ alter +RESET)

  respuesta_1 = input("Tu respuesta: ").lower()
  
  while respuesta_1 not in ("a","b","c","d","e","x"):
   respuesta_1 = input(BIBlack+"Esa clave no existe, por favor ingrese alguna nuevamente: "+RESET).lower()
  
  if respuesta_1 == "a":
     puntaje -= random.randint(10, 30)
     print(RED+"Incorrecto! \nLa digestion de las grasas lo hace la Bilis."+RESET)
     print(MAGENTA+"Perdistes puntos extra al azar"+RESET)
    
  elif respuesta_1 == "b":
    puntaje -= random.randint(10, 30)
    print(RED+"Incorrecto! \nEl HCI del estomago llega a activar una enzima inactiva, el Pepsinogeno."+RESET)
    print(MAGENTA+"Perdistes puntos al azar"+RESET)
    
  elif respuesta_1 == "c":
    puntaje -= random.randint(10, 30)
    print(RED+"Incorrecto! \nEl peristaltismo intestinal transforma el Quimo a Quilo en el intestino delgado,alli termina la Digestion de Alimentos."+RESET)
    print(MAGENTA+"Perdistes puntos al azar"+RESET)
    
  elif respuesta_1 == "e":
    puntaje -= random.randint(10, 30)
    print(RED+"Incorrecto! \nInhibir bacterias, por ejemplo, es la funcion de las Placas de Peyer en el Intestino Delgado."+RESET)
    print(MAGENTA+"Perdistes  puntos al azar"+RESET)
    
  elif respuesta_1 == "x":
    puntaje += 100
    print(GREEN+"Wow, distes a una letra secreta.") 
    print(MAGENTA+"De recompensa tome 100 puntos"+RESET)
    
  else:
   puntaje += random.randint(20, 50) #ganaras puntos al azar en ese rango
   print(GREEN+"Muy bien!!", nombre, "\nLas glandulas de Brunner se encuentran en la Mucosa Duodenal (Intestino delgado)"+RESET)
   print(MAGENTA+"Has ganado puntos extra al azar"+RESET)
    
  print("Tu puntaje ahora:",puntaje,"puntos")
  
  #Fin pregunta 1
  input("\nPresione Enter para continuar: ")
  print("Cargando...")
  time.sleep(1)


  

#-----------------La pregunta 2 nos dara Puntos exactos--------------------
  print(BLUE+"\n2.Respecto a las glándulas gástricas, en cual de ellas se elabora la hormona gastrina:"+RESET)
  for i in range (len(pregunta2)): #La longitud (len) es 5, el range tomara los indices 0,1,2,3,4
    alter = pregunta2[i]
    print(YELLOW+ alter +RESET)

  
  respuesta_2 = input("Tu respuesta: ").lower()
  
  while respuesta_2 not in ("a","b","c","d","e","x"):
   respuesta_2 = input(BIBlack+"Esa clave no existe, por favor ingrese alguna nuevamente: "+RESET).lower()
  
  if respuesta_2 == "a":
    puntaje -= 10
    print(RED+"Incorrecto! \nLas Glandulas cardias secretan Mucus en el Estomago."+RESET)
    print(MAGENTA+"Perdistes 10 puntos"+RESET)
    
  elif respuesta_2 == "b":
    puntaje -= 10
    print(RED+"Incorrecto! \nLas Glandulas del fondo y cuerpo (del estomago) vienen a ser las glandulas fundicas."+RESET) 
    print(MAGENTA+"Perdistes 10 puntos"+RESET)
    
  elif respuesta_2 == "c":
    puntaje -= 10
    print(RED+"Incorrecto! \nLas glandulas fundicas tienen diversas celulas,las celulas principales secretan Pepsinogeno y Lipasa gastrica."+RESET) 
    print(MAGENTA+"Perdistes 10 puntos"+RESET)
    
  elif respuesta_2 == "e":
    puntaje -= 10
    print(RED+"Incorrecto! \nLas Glandulas de Brunner estan en el Intestino Delgado."+RESET) 
    print(MAGENTA+"Perdistes 10 puntos"+RESET)
    
  elif respuesta_2 == "x":
    puntaje += 100
    print(GREEN+"Solo por presionar x has conseguido puntos extra."+RESET) 
    print(MAGENTA+"Has ganado 100 puntos"+RESET)
  else:
    puntaje += 20
    print(GREEN+"Muy bien", nombre,"\nEstas estimulan el HCI del estomago y genera el Peristaltismo.") 
    print(MAGENTA+"Has ganado 20 puntos"+RESET)
  
  print("Tu puntaje ahora:",puntaje,"puntos")  
  
  input("\nPresione Enter para continuar: ")
  print("Cargando...")
  time.sleep(1)



  
  #--------------------Pregunta 3 usara signos aritmeticos para dar o quitarnos puntos de acuerdo a la respuesta-------------------
  print(BLUE+"\n3.Es un tipo de célula que se encuentra dentro de las glándulas gástricas; excepto:"+RESET)
  for i in range (len(pregunta3)):
    alter = pregunta3[i]
    print(YELLOW+ alter +RESET)
  
  respuesta_3 = input("Tu respuesta: ").lower()
  
  while respuesta_3 not in ("a", "b", "c", "d", "e", "x"):
    respuesta_3 = input(BIBlack+"Esa clave no existe, por favor ingrese alguna nuevamente: "+RESET).lower()
  
  if respuesta_3 == "a":
    print(RED+"Incorrecto!!", nombre,"\nLas celulas mucosas son tambien llamadas celulas mucigenas.Estan en las Glandulas Fundicas."+RESET)
    print(MAGENTA+"Pierdes 5 puntos"+RESET)
    puntaje = puntaje - 5 #recuerda solo usar un = no dos
    
  elif respuesta_3 == "b":
    print(RED+"Incorrecto!! \nLas celulas parietales de las Glandulas Fundicas secretan HCI y el Factor intrinseco."+RESET)
    print(MAGENTA+"Pierdes 2 puntos"+RESET)
    puntaje = puntaje - 2
  
  elif respuesta_3 == "c": #una forma diferente de colocar la respuesta correcta en lugar de usar ELSE
    print(GREEN+"Muy bien!! \nSon Celulas Intestinales que se encuentran en las Glándulas de Lieberkuhn.")
    print(MAGENTA+"Tu puntaje se multiplicara por Dos como recompensa"+RESET)
    puntaje = puntaje * 2
  
  elif respuesta_3 == "d":
    print(RED+"Muy mal!! \nLas células principales, parte de las Glandulas Fundicas, secretan Pepsinogeno y Lipasa Gastrica."+RESET)
    print(MAGENTA+"Pierdes 15 puntos."+RESET)
    puntaje = puntaje - 15
  
  elif respuesta_3 == "e":
    print(RED+"Pesimo!! \nLas celulas Argentafines estan presentes en el tracto gastrointestinal, secretan Serotonina."+RESET)
    print(MAGENTA+"Tu puntaje se reduce en la mitad (Se redondeara el numero si es necesario)."+RESET)
    puntaje = puntaje // 2

  elif respuesta_3 == "x":
    puntaje += random.randint(10, 100)
    print(GREEN+"Clave Secreta."+RESET)
    print(MAGENTA+"Puntos al azar para usted"+RESET)
  
  
  print("Tu puntaje ahora:", puntaje, "puntos")
  
  input("\nEn la siguiente pregunta podrias ganar puntos extras respondiendo x. Intentalo!\nPresione Enter para continuar: ")
  print("Cargando...")
  time.sleep(1)



  

  #-----------La pregunta 4 nos daras puntos al azar------------
  print(BLUE+"\n4.Estructura respiratoria que no tiene cartílago "+RESET)
  for i in range (len(pregunta4)):
    alter = pregunta4[i]
    print(YELLOW+ alter +RESET)

  respuesta_4 = input("Tu respuesta: ").lower()
  
  while respuesta_4 not in ("a","b","c","d","e", "x"):
   respuesta_4 = input(BIBlack+"Esa clave no existe, por favor ingrese alguna nuevamente: "+RESET).lower()
  
  if respuesta_4 == "a":
     puntaje -= random.randint(40, 70)
     print(RED+"Incorrecto! \nLa Laringe esta constituida por cartilagos impares (epiglotis, tiroides, cricoides) y cartilagos pares (aritenoides, corniculados, cuneiformes."+RESET)
     print(MAGENTA+"Perdistes puntos al azar"+RESET)
    
  elif respuesta_4 == "b":
    puntaje -= random.randint(10, 30)
    print(RED+"Incorrecto! \nLa nariz tiene cartílago en su parte delantera."+RESET)
    print(MAGENTA+"Perdistes puntos al azar"+RESET)
    
  elif respuesta_4 == "d":
    puntaje -= random.randint(10, 30)
    print(RED+"Incorrecto! \nEn la Tráquea encontramos al cartílago hialino."+RESET)
    print(MAGENTA+"Perdistes puntos al azar"+RESET)
    
  elif respuesta_4 == "e":
    puntaje -= random.randint(10, 30)
    print(RED+"Incorrecto! \nEn los bronquios encontramos el cartílago hialino."+RESET)
    print(MAGENTA+"Perdistes puntos al azar"+RESET)
    
  elif respuesta_4 == "x":
    puntaje += 200
    print(GREEN+"Presionastes una tecla secreta."+RESET)
    print(MAGENTA+"De recompensa tome 200 puntos"+RESET)
    
  else:
    puntaje += random.randint(50, 70) #ganaras puntos al azar en ese rango
    print(GREEN+"Muy bien!!", nombre, "\nLos bronquiolos no tienen cartilago."+RESET)
    print(MAGENTA+"Has ganado puntos al azar"+RESET)
    
  print("Tu puntaje ahora:",puntaje,"puntos")
  
  #Fin pregunta 4
  input("\nPresione Enter para continuar: ")
  print("Cargando...")
  time.sleep(1)



  

  #---------------------Pregunta 5 usara multiplicacion y restas para dar o quitarnos puntos de acuerdo a la respuesta--------------------------
  print(BLUE+"\n5.Son conformantes del pedículo pulmonar; excepto:"+RESET)
  for i in range (len(pregunta5)):
    alter = pregunta5[i]
    print(YELLOW+ alter +RESET)
  
  respuesta_5 = input("Tu respuesta: ").lower()
  while respuesta_5 not in ("a", "b", "c", "d", "e", "x"):
    respuesta_5 = input(BIBlack+"Esa clave no existe, por favor ingrese alguna nuevamente: "+RESET).lower()
  
  if respuesta_5 == "a":
    print(RED+"Incorrecto!!\nLa vena pulmonar lleva sangre con oxígeno de los pulmones al corazón."+RESET)
    print(MAGENTA+"Pierdes 50 puntos"+RESET)
    puntaje = puntaje - 50 #recuerda solo usar un = no dos
    
  elif respuesta_5 == "b":
    print(RED+"Incorrecto!!\nLos bronquios principales se dirigen desde el final de la tráquea hasta los hilios pulmonares por donde penetran en los pulmones."+RESET)
    print(MAGENTA+"Pierdes 25 puntos"+RESET)
    puntaje = puntaje - 25
  
  elif respuesta_5 == "c": #una forma diferente de colocar la respuesta correcta en lugar de usar ELSE
    print(RED+"Muy mal!! \nLa arteria pulmonar transporta la sangre del ventrículo derecho del corazon a los pulmones."+RESET)
    print(MAGENTA+"Pierdes 75 puntos"+RESET)
    puntaje = puntaje - 75
  
  elif respuesta_5 == "e":
    print(RED+"Muy mal!! \nLa arteria bronquial llevan sangre oxigenada a los pulmones."+RESET)
    print(MAGENTA+"Pierdes 15 puntos"+RESET)
    puntaje = puntaje - 15
  
  elif respuesta_5 == "d":
    print(GREEN+"Muy bien!! \nAdemas, los sacos alveolares poseen numerosos alvéolos donde se realiza el intercambio de oxigeno."+RESET)
    print(MAGENTA+"Se te duplicara tu puntaje."+RESET)
    puntaje = puntaje * 2

  elif respuesta_5 == "x":
    puntaje += random.randint(25, 75)
    print(GREEN+"Pulsastes una tecla con opción secreta."+RESET)
    print(MAGENTA+"Recibiras puntos al azar."+RESET)
  
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
                     