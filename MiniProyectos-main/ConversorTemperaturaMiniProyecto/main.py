def main():

    while True:
        print("\nCONVERSOR DE TEMPERATURA")

        print("\n1- Convertir de Celsius a Fahrenheit")
        print("2- Convertir de Fahrenheit a Celsius")
        print("3- Salir")
        option = input("Selecciona una opción: ").strip()

        if option == "1":
            ctof()
        elif option == "2":
            ftoc() 
        elif option == "3":
            print("\nSalir")
            break
        else:
            print("\nOpción no válida") 

def ctof():
    print("\nConvertir de Celsius a Fahrenheit")
    try:
        celsius = int(input("Ingresa la temperatura en grados celsius: ").strip())
    except:
        print("\nIngresa un valor numérico")
        return
    
    fahrenheit = (celsius * 9/5)+32

    print(f"{celsius}°C = {fahrenheit}°F")

def ftoc():
    print("\nConvertir de Fahrenheit a Celsius")
    try:
        fahrenheit = int(input("Ingresa la temperatura en grados fahrenheit: ").strip())
    except:
        print("\nIngresa un valor numérico")
        return
    
    celsius = (fahrenheit - 32)*(5/9)

    print(f"{fahrenheit}°F = {celsius}°C")

if __name__ == "__main__": 
    main()