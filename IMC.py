fAltura = 1.80
fPeso = 72.0

fImc = fPeso/(fAltura**2)
print("IMC: ", fImc)

print("DE ACORDO COM O ICM: ")  

print("=> Muito abaixo do peso: ", fImc < 17)
print("=> Peso abaixo do normal: ", fImc >= 17 and fImc < 18.5)
print("=> Parabéns, seu peso está normal: ", fImc >= 18.5 and fImc < 25.0)
print ("=> Acima do peso normal: ", fImc >= 25 and fImc <= 30)
print("=> Muito acima do peso:", fImc > 30)