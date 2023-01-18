#Faça um cadastro em python
#Pass.1 [Crie uma string pedindo o nome, idade e gmail:]
#Pass.2 [Crie uma string confirmando os dados enviados:]
#Pass.3 [Peça para o usuario confirmar se está certo ou não:]

nome = input('Qual é seu nome? ')
idade = input('Qual é sua idade? ')
gmail = input('Qual é seu gmail? ')
print('O seu cadastro foi confirmado! Seu nome é: ' +nome+ ', voce tem: ' +idade+ ' anos, seu gmail é: ' +gmail+ '.')
cad = input('O seu cadastro está correto? ')
if cad =='sim':
    print('Tudo certo!')
else:
    print('Reenvie seus dados!')
