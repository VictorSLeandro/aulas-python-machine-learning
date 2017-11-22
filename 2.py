#operadores de condições 
idade = 18

if idade >= 18:
	print("Maior de idade")
else:
	print("menor de idade")

idade = 20

if idade>=18:
	if idade <=60:
		print("Adultor")
	else:
		print("idoso")
else:
	print("menor de idade")


#reptições
count = 1
print("")
print("\n WHILE")
while count<=10:
	print("%d" % count)
	count +=1
print("\n FOR")
for x in range(1,11):
	print("%d" % x)
i = 0
print("\n")
while True:
	print("%d" % i)
	if i == 10:
		break
	i += 1

