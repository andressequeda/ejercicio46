numero  =  int ( input ( "Ingrese el primer número:" ))
numero_mayor  =  int ( input ( "Ingrese un número mayor al primer número:" ))
para  x  en  rango ( numero , numero_mayor  +  1 ):
    if  numero_mayor  >  numero :
        print ( x , "" , end = "" )
    otra cosa :
        print ( "Error. El segundo número es menor o igual que el primero" )