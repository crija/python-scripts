#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Brasileirão, na ordem mostre:
#Apenas os 5 primeiros colocados;
#Os últimos 4 colocados da tabela;
#Uma lista com os times em ordem alfabetica
#Em que posiçao na tabela está o time d Botafogo

times = ('Palmeiras', 'Internacional', 'Fluminence', 'Corinthians', 'Flamengo', 'Athetico-PR',
'Athetico-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino'
'Cuiabá', 'Ceará SC', 'Athetico-GO', 'Avaí', 'Juventude')

print(f'Os 5 primeiros colocados do Brasileirão:{times[0:6]}')
print(f'Os últimos 4 colocados da tabela:{times[-4:]}')
print(f'Os times do Brasileirão em ordem alfabetica:{sorted(times)}')
print(f'Botafogo está na posição: {(times.index("Botafogo")+1)}')
