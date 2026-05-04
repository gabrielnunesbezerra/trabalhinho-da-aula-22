from veiculo import Veiculo, Carro, Moto

v1 = Carro("corsa", "sedan", 2021, 8)
v2 = Moto("ferrari", "812 Superfast", 2019, 800)
v3 = Carro("Fusca ", "volskvagem", 2018, 7)

garagem = [v1, v2, v3]

for v in garagem:
    print(v.descrever())

carros = [v for v in garagem if isinstance(v, Carro)]
motos = [v for v in garagem if isinstance(v, Moto)]

print(f"Carros: {len(carros)} | Motos: {len(motos)}")