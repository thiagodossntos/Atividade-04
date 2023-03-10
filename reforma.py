altura = float(input('digite a altura: '))
comprimento = float(input('agora digite o comprimento: '))
largura = float(input('agora a largura: '))
area_piso = largura * comprimento
volume_sala = largura * comprimento * altura
area_parede = 2 * altura * largura + 2 * altura * comprimento

print(f'essa é a area do piso {area_piso:.2f}')
print(f'o volume da sala é {volume_sala:.2f}')
print(f'a aréa da parede é {area_parede:.2f}')
