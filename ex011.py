#crie um programa que leia quanto dinheiro (real) o usuario quer converter e para qual moeda :


real = float(input('Digite o valor em (real) que voce quer converter: R$'))

converter = input('Para qual dessas moedas voce deseja converter: (dólar, euro ou iene)? ')

dólar = real / 5.16
euro = real / 5.57
iene = real / 0.040

if converter == 'dólar':
    print('US${:.2f}'.format(dólar))

elif converter == 'euro':
    print('£{:.2f}'.format(euro))

elif converter == 'iene':
    print('¥{:.2f}'.format(iene))
    
else:
    print('Moeda não identificada')
