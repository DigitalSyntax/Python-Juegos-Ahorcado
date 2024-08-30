import random

def obtener_palabra_secreta():
    
    palabra = ['Python', 'Java' , 'Selenium' , 'Git' , 'Angular'] 
    return random.choice(palabra)
    
    
    
    
    
    
def mostrar_avance(palabra_secreta , letras_adivinas):
    adivinado = ''
    
    for letra in palabra_secreta:
        if letra in letras_adivinas:
            adivinado += letra
        else:
            adivinado += "_"
    
    return adivinado
        
    
    
    
    
    
def juego_ahorcado():
    
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinas = []
    intentos = 7
    
    juego_terminado = False
    
    print("¡Bienvenido al juego del ahorcado!")
    print(f"Tenes {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_avance(palabra_secreta, letras_adivinas), "La cantidad de letras es:", len(palabra_secreta))
    
    
    while not juego_terminado and intentos > 0:
        
        adivinanza = input("Introduce una letra: ").lower()
        
        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Porfavor introduzca una letra valdia (Solo escribir una letra)")
            
            
        elif adivinanza in letras_adivinas:
            print("Ya has usado esa letra, intenta con otra")
            
        else:
            letras_adivinas.append(adivinanza)
            
            if adivinanza in palabra_secreta:
                print(f"Muy bien has acertado, la letra {adivinanza} está presente en la palabra")
                
            else:
                intentos -= 1
                print(f"Lo siento, la letra '{adivinanza}' no está dentro de la palabra")
                print(f"Te quedan {intentos} intentos")

        progreso_actual = mostrar_avance(palabra_secreta, letras_adivinas)
        print(progreso_actual)
        
        if "_" not in progreso_actual:
            juego_terminado = True
            print(f"Felicitaciones has ganado, la palbra completa es {palabra_secreta}")
            
            
    if intentos == 0:
        print(f"Haz perdido, la palabra secreta era: '{palabra_secreta}' ")        
            
    
    
    
    
                
        
juego_ahorcado()
        
        
        
        
        
        
        
    
    
    