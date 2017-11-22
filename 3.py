d = {'marcos':28,'maria':20,'pedro':18}
print(d)
print(d['marcos'])
#d['marcos'] = 25 dicinario e imutavel
print(d['marcos'])
d['felipe'] = 30
print(d)

for k in d:
	print(d[k],end= ' ')
print(d.items())#mostra os itens do dicionario
print(d.keys())#mostra as chaves do dicionario
print(d.values())#mostra os valos do dicionario
print('maria' in d)
print('python' in d)
