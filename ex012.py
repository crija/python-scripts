real = float(input('Digite quanto voce tem na carteira: R$'))
dolar = real / 5.16
print('Com R${:.2f} voce pode comprar US${:.2f}'.format(real, dolar))
euro = float(input('Digite quanto voce tem na carteira: £'))
euro = real / 5.57
print('Com R${:.2f} voce pode comprar US${:.2f}'.format(real, euro))
