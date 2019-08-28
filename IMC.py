fAltura = float(input("Digite a altura: "))
fPeso = float(input("Digite o peso: "))

fImc = fPeso/(fAltura**2)
print("IMC: ", fImc)

print("DE ACORDO COM O ICM: ")  

if fImc < 17:
    print("=> Muito abaixo do peso!")
elif fImc >= 17 and fImc < 18.5:
    print("=> Peso abaixo do normal!")
elif fImc >= 18.5 and fImc < 25.0:
    print("=> Peso normal!")
elif fImc >= 25 and fImc < 30:
    print ("=> Acima do peso normal!")
else:
    print("=> Muito acima do peso!")
