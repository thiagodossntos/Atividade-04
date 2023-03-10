print('gostaria de saber quantos segundos se passaram deste a meia-noite? digite o que se pede!')
horas = int(input('digite as horas: '))
minutos = int(input('digite os minutos: '))
segundos = int(input('dogoye os segundos: '))

hora_segundo = horas * 60 * 60
minuto_segundo = minutos * 60

calculo = hora_segundo + minuto_segundo + segundos

print(f'essa é  resposta toda em segundos {calculo}')