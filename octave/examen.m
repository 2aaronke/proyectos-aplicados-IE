clear
miArchivo= fopen('201701022.txt', 'w')
disp('********MENU DE OPCIONES********')

while(true)
 while(true)
   try
    disp('1. altura y pesos')
    disp('2. diferencia de suma de cuadrados')
    disp('3. factores primos')
    disp('4. sucesion fibonacci')
    disp('5. areas y volumen')
    disp('*******************')
    opcion = input( 'elegir el programa que desee ejecutar:  ');
    break
   catch
    disp('**ingrese una oopcion valida**')
    end_try_catch
 endwhile

 %primera opcion del menu
 if(opcion==1)
 alturaMujeres=0;
 alturaHombres=0;
 alturapromedioMujeres=0;
 alturapromedioHombres = 0;
 pesoMujeres = 0;
 pesoHombres = 0;
 pesopromedioMujeres = 0;
 pesopromedioHombres = 0;
 contadorhombres=0;
 contadormujeres=0;
 n = input ('numero de personas a evaluar:   ');
 for i=0 : n;
   disp('1. masculino')
   disp('2. femenino')
   genero = input ('seleccione la pocion de genero: ');
   altura = input ('altura en metros: ');
   peso =input('peso en libras: ');
   if (genero==1)
     alturaHombres=alturaHombres+altura;
     pesoHombres= pesoHombres+peso;
     contadorhombres=contadorhombres+1;
   endif
   if (genero==1)
     alturaMujeres=alturaMujeres+altura;
     pesoMujeres= pesoMujeres+peso;
     contadormujeres=contadormujeres+1;
   endif
   endfor
   pesopromedioHombres=(pesoHombres)/contadorhombres;
   pesopromedioMujeres=(pesoMujeres)/contadormujeres;
   alturapromedioHombres=(alturaHombres)/contadorhombres;
   alturapromedioMujeres=(alturaMujeres)/contadormujeres;
   disp(['el peso promedio de la poblacion masculina es de' , num2str(pesopromedioHombres)])
   disp(['el peso promedio de la poblacion femenina es de' , num2str(pesopromedioMujeres)])
   disp(['la altura promedio de la poblacion masculina es de ' , num2str(alturapromedioHombres)])
   disp(['la altura promedio de la poblacion femenina es de' , num2str(alturapromedioMujeres)])
  fprintf(miArchivo, '%i\n',pesopromedioHombres)
  fprintf(miArchivo, '%i\n',pesopromedioMujeres)
  fprintf(miArchivo, '%i\n',alturapromedioHombres)
  fprintf(miArchivo, '%i\n',alturapromedioMujeres)
 endif
 %segunda opcion del menu
 if (opcion==2)
   sumaDecuadrados=0;
   cuadradoDeSuma=0;
   suma=0;
   for i=0: 100
     sumaDecuadrados= sumaDecuadrados + (i+1)^2;
   endfor
   for i=0: 101
     suma=suma+i;
   endfor
   cuadradoDeSuma= suma^2;
   resultado = cuadradoDeSuma-sumaDecuadrados
   disp(['la diferencia entre el cuadrado de la suma y suma de cuadrados es: ' , num2str(resultado)])
   fprintf(miArchivo, '%i\n',resultado)
 endif
 %tercera opcion del menu
 if (opcion==3)
   disp('factores primos')
 endif
 %cuarta opcion del menu
 if (opcion==4)
   disp('serie de fibonacci')
   
 endif
 %quinta opcion del menu
  if (opcion==5)
   radio= input ('ingrese el radio del cono: ');
   generatriz = input ('ingrese la generatriz: ');
   alturacono= input ('ingrese altura: ');
   areabase = pi*(radio^2);
   disp(['el area de la base es>  ' , num2str(areabase)])
   fprintf(miArchivo, '%i\n',areabase)
   arealateral= pi*radio*generatriz;
   disp(['el area lateral es   ' , num2str(arealateral)])
   fprintf(miArchivo, '%i\n',arealateral)
   areaTotal= areabase+arealateral;
   disp(['el area total del cono es   ' , num2str(areaTotal)])
   fprintf(miArchivo, '%i\n',areaTotal)
    volumen= (1/3)*pi*(radio^2);
    disp(['el volumen del cono es    ' , num2str(volumen)])
   fprintf(miArchivo, '%i\n',volumen)
   
 endif
 
  while (true)
    try
      disp('1. SI')
      disp('2. NO')      
      disp('quiene continuuar?')  
      seguir = input( 'ingrese una opcion: ');
      break 
     catch
      disp('**ingrese una oopcion valida**')  
     end_try_catch
   endwhile  
  if(seguir==2)
    break
  endif
endwhile
disp('**gracias por su tiempo**')   

fclose(miArchivo);
