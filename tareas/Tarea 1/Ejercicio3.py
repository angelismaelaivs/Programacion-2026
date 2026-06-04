print('Escribe una palabra para saber si es un palindromo')
palabra = input()
letras= list(palabra)

n=len(letras)

for i in range(n):
    if letras[i] != letras[n-1 -i]:
        palindromo = False
        print('La palabra', palabra, ' no es un palindromo. :(' )
        break
    elif letras[i] == letras[n-1 -i]:
        palindromo = True
        print('La palabra', palabra, 'sí es un palindromo. :)')
        break