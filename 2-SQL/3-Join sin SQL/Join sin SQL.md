# Ejemplo join sin SQL con codigo en Python para ser ejecutado segun el modelo Map-Reduce de Big Data

-Se proveen dos archivos de texto countries.txt y customers.txt, sobre los cuales se debe generar un reporte en el que se debem mostrar los datos juntos de nombre del cliente y nombre dle pais al que pertenece.

-Para ejecutar este ejemplo sin tener instalados los componentes mínimos de Hadoop podemos correr los siguientes comandos en Linea de comando en Linuxresultados

- Map 
	- Primero asignar permisos de ejecución sobre el archivo Python de Map
		
		chmod a+x map4join.py

	- Luego con el comando cat podemos ejecutar el codigo de map sobre los archivos fuentes y ver por consola el resultado

		cat customers.txt countries.txt|./map4join.py|sort
		
	- Nos deberia mostrar algo así 
		
			CA^-1^-1^Canada
			CA^not so good^Yo Yo Ma^-1
			CA^valued^Jon Sneed^-1
			CA^valued^Jon York^-1
			CA^valued^Sam Sneed^-1
			IT^-1^-1^Italy
			JA^not so bad^Jim Davis^-1
			UK^-1^-1^United Kingdom
			UK^not so good^Arnold Wesise^-1
			UK^valued^Alex Ball^-1
			US^-1^-1^United States
			US^not bad^Alice Bob^-1
			US^not bad^Henry Bob^-1
		
- Reduce 
	
	- Asignar de neuvo permisos de ejcución sobre el archivo Python de Reduce
	
		chmod a+x reduce4join.py

	 - Y luego ejecutar 
	 
		cat customers.txt countries.txt|./map4join.py|sort|./reduce4join.py

	- Nos deberia mostrar algo asi
	
		Canada  not so good 1
		Canada  valued  3
		JA - Unkown Country not so bad  1
		United Kingdom  not so good 1
		United Kingdom  valued  1
		United States   not bad 2