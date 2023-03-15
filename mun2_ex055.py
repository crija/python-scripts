#Criar QR code:

import qrcode

imagem = qrcode.make('github.com/crija')

imagem.save('qrcode-github.png')
