lista = []
for n in range(4):
    n = int(input(f'Entre com o valor para N{n+1}: '))   
    lista.append(n)
    print (lista)

print("\nmaior valor: {}".format(max(lista)))
print("\nmenor valor: {}".format(min(lista)))
print("\nmédia dos valores: {}".format(sum(lista) / len(lista)))
input("\nPressione qualquer tecla para finalizar")