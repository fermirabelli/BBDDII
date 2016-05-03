# Práctica SQL - Númer0 3

1.	Escriba una consulta para mostrar la fecha actual. Etiquete la columna como Date.

2.	Para cada empleado, visualice su número, apellido, salario y salario incrementado en el 15% y expresado como número entero. Etiquete la columna como New Salary. Ponga la sentencia SQL en un archivo de texto llamado BBDDII_Lab3_2.sql.

3.	Ejecute la consulta en el archivo BBDDII_Lab3_2.sql.        

4.	Modifique la consulta lab3_2.sql para agregar una columna que reste el salario antiguo del nuevo. Etiquete la columna como "Aumento". Guarde el contenido del archivo como BBDDII_Lab3_4.sql. Ejecute la consulta revisada.

5. Escriba una consulta que muestre los apellidos de los empleados con la primera letra en mayúsculas y todas las demás en minúsculas, así como la longitud de los nombres, para todos los empleados cuyos nombres comienzan por J, A o M. Asigne a cada columna la etiqueta correspondiente. Ordene los resultados según los apellidos de los empleados.

6. Para cada empleado, muestre su apellido y calcule el número de meses entre el día de hoy y la fecha de contratación. Etiquete la columna como "MESES_TRABAJADOS". Ordene los resultados según el número de meses trabajados. Redondee el número de meses hacia arriba hasta el número entero más próximo.

7.	Escriba una consulta que produzca lo siguiente para cada empleado:	<employee last name> earns <salary> monthly but wants <3 times salary>. Etiquete la columna como Dream Salaries.

8.	Cree una consulta para mostrar el apellido y el salario de todos los empleados. Formatee el salario para que tenga 15 caracteres, rellenando a la izquierda con $. Etiquete la columna como SALARY.

9.	Muestre el apellido, la fecha de contratación y el día de la semana en el que comenzó el empleado. Etiquete la columna DAY. Ordene los resultados por día de la semana, comenzando 	por el lunes.

10.Cree una consulta que muestre el apellido y las comisiones de los empleados. Si un empleado 	no gana comisión, ponga “No Commission”. Etiquete la columna COMM.

11.	Cree una consulta que muestre el apellido de los empleados y que indique las cantidades de sus salarios anuales con asteriscos. Cada asterisco significa mil dólares. Ordene los datos por salario en orden descendente. Etiquete la columna EMPLOYEES_AND_THEIR_SALARIES.

12. Utilizando la función DECODE, escriba una consulta que muestre el grado de todos los empleados basándose en el valor de la columna JOB_ID, según los datos siguientes:
	Cargo						Grado 	
	AD_PRES						A	
	ST_MAN						B	
	IT_PROG						C	
	SA_REP						D	
	ST_CLERK					E	
	Ninguno de los anteriores	0	

13. Vuelva a escribir la sentencia de la pregunta anterior utilizando la sintaxis CASE.
