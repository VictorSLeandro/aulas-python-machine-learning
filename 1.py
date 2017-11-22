nome = "victor"
nome2 = nome
print(id(nome))
print(id(nome2))
print(type(nome2))# função utilizada para retornar o tipo da variavel

x = 2.0
type(x)
y = 3
print(type(y))
print(type(x))

mult = x * y # multiplicação
print("%f x %d = %f" % (x,y,mult))
div = x / y # divisão - float
print("%f / %d = %f" % (x,y,div))
div2 = x // y # divisão - int 
print("%f // %d = %d" % (x,y,div2))
soma = x + y #soma
print("%f + %d = %d" % (x,y,soma))
sub = x - y #subtração
print("%f - %d = %d" % (x,y,sub))


