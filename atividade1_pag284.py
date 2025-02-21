tipo=("Deseja converte qual tipo de medida de temperatura? ")
if "Celcius" in tipo or "celcius" in tipo:
    celcius=input("Insira a temperatura: ")
    fahrenheit=(celcius^3)/5+32
    print(fahrenheit)
elif "fahrenheit" in tipo or "Fahrenheit" in tipo:
    fahrenheit=input("Insira a temperatura: ")
    celcius=(fahrenheit-32)/1.8
    print(celcius)