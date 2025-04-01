from functools import reduce

def main():
   
    while True:
        print("\nCALCULADORA")

        print("\n1- Sumar")
        print("2- Restar")
        print("3- Multiplicar")
        print("4- Dividir")
        print("5- Salir")
        option = input("Selecciona una opción: ").strip()

        if option == "1":
            print("\nSuma")
            sumar()
        elif option == "2":
            print("\nResta")
            restar()
        elif option == "3":
            print("\nMultiplicación")
            multiplicar()
        elif option == "4":
            print("\nDivisión")
            dividir()
        elif option == "5":
            print("\nSalir")
            break
        else:
            print("\nOpción no válida")   

def sumar():
    nums = []
    try:
        totalnum = int(input("Cuantos números vas a sumar?: ").strip())
        if totalnum <= 1:
            print("\nEl valor debe ser mayor a 1")
            return 
        if totalnum >= 5:
            print("\nEl valor debe ser menor a 6")
            return 

        for num in range(totalnum):
            inputnum = int(input("Ingresa un número: ").strip())
            nums.append(inputnum)
    except:
        print("\nIngresa un valor numérico")
        return

    suma = sum(nums)

    output = ""
    for i, n in enumerate(nums): 
        finishnum = len(nums) - 1
        if i == finishnum:
            output = output + f"{n} = {suma}"
        else:
            output = output + f"{n} + "

    print("\nSuma: "+ output)

def restar():
    nums = []
    try:
        totalnum = int(input("Cuantos números vas a restar?: ").strip())
        if totalnum <= 1:
            print("\nEl valor debe ser mayor a 1")
            return 
        if totalnum >= 5:
            print("\nEl valor debe ser menor a 6")
            return 
        
        for num in range(totalnum):
            inputnum = int(input("Ingresa un número: ").strip())
            nums.append(inputnum)
    except:
        print("\nIngresa un valor numérico")
        return
    
    rest = reduce(lambda x, y: x - y, nums)

    print("\nrest: "+ str(rest))

    output = ""
    for i, n in enumerate(nums): 
        finishnum = len(nums) - 1
        if i == finishnum:
            output = output + f"{n} = {rest}"
        else:
            output = output + f"{n} - "

    print("\nResta: "+ output)

def multiplicar():
    nums = []
    try:
        totalnum = int(input("Cuantos números vas a multiplicar?: ").strip())
        if totalnum <= 1:
            print("\nEl valor debe ser mayor a 1")
            return 
        if totalnum >= 5:
            print("\nEl valor debe ser menor a 6")
            return 
        
        for num in range(totalnum):
            inputnum = int(input("Ingresa un número: ").strip())
            nums.append(inputnum)
    except:
        print("\nIngresa un valor numérico")
        return
    
    mul = reduce(lambda x, y: x * y, nums)

    output = ""
    for i, n in enumerate(nums): 
        finishnum = len(nums) - 1
        if i == finishnum:
            output = output + f"{n} = {mul}"
        else:
            output = output + f"{n} * "

    print("\nMultiplicación: "+ output)

def dividir():
    try:
        print("\nIngresa los números que vas a dividir")
        numA = int(input("Ingresa un número: ").strip())
        numB = int(input("Ingresa un número: ").strip())
    except:
        print("\nIngresa un valor numérico")
        return
    
    div = numA / numB

    output = f"{numA} / {numB} = {div}"

    print("\nDivisión: "+ output)

if __name__ == "__main__":
    main()