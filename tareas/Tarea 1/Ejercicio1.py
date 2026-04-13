a=float(input('Da tu coeficiente a: '))
b=float(input('Da tu coeficiente b: '))
c=float(input('Da tu coeficiente c: '))

dis=b**2-4*a*c #Discriminante
img= ((-1)*dis)**0.5 #Parte imaginaria  

if a!=0:
  if dis<0:
    print('Las soluciones estan en los números complejos:')
    preal= (-b)/ (2*a)
    pimg = img / (2*a)
    print('Solución 1:', preal, " + ", pimg, "i") 
    print('Solución 2:', preal, " - ", pimg, "i") 
  elif dis>0:
    print("Hay dos soluciones reales")
    x1=(-b + (dis**(0.5))) / (2*a)
    x2=(-b - (dis**(0.5))) / (2*a)
    print("x1= ", x1)
    print("x2= ", x2)
  elif dis==0:
    print("La solución real es unica")
    x=-b/(2*a)
    print("x= ",x)
elif a == 0:  # Si a es 0, la ecuación se vuelve lineal: bx + c = 0
    if b != 0:
        print("La ecuación es lineal y tiene una solución")
        x = -c/b
        print("x = ", x)
    else: #a = 0 y b = 0
        if c == 0:
            print("Soluciones infinitas")
        else:
            print("Contradicción")