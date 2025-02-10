peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = "Abaixo do peso"
elif 18.5 <= imc < 25:
    categoria = "Peso normal"
elif 25 <= imc < 30:
    categoria = "Sobrepeso"
elif 30 <= imc < 35:
    categoria = "Obesidade Grau I"
elif 35 <= imc < 40:
    categoria = "Obesidade Grau II"
else:
    categoria = "Obesidade Grau III"

print(f'\nSeu IMC: {imc:.1f}')
print(f'Classificação: {categoria}')