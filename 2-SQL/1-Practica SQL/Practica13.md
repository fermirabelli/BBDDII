# Práctica SQL - Número 13 (Group by avanzado)

1. Escriba una consulta para mostrar lo siguiente para los empleados cuyos identificadores de director sean menores que 120: 
 *Identificador de director
 *Identificador de cargo y salario total para todos los identificadores de cargo para los empleados que informen el mismo director
 *Salario total de esos directores  
 *Salario total de los directores, independientemente de los identificadores de cargo  		  
	
2.	Observe el resultado de la pregunta 1. Escriba una consulta utilizando la función GROUPING para determinar 	si los valores NULL en las columnas correspondientes a las expresiones GROUP BY son causados por la operación ROLLUP. 
     
3. Escriba una consulta para mostrar lo siguiente para los empleados cuyos identificadores de director sean menores que 120: 
 *Identificador de director  
 *Cargo y salario total para todos los cargos de los empleados que informen al mismo director
 *Salario total de esos directores   
 *Valores de tabulación cruzada para mostrar el salario total para todos los cargos, independientemente del director
 *Salario total independientemente de todos los cargos 
	
4. 	Observe el resultado de la pregunta 3. Escriba una consulta utilizando la función GROUPING para determinar si los valores NULL de las columnas correspondientes a las expresiones GROUP BY están provocados por la operación CUBE. 

5. Utilizando GROUPING SETS, escriba una consulta para mostrar los siguientes agrupamientos: 
	*department_id, manager_id, job_id
	*department_id, job_id
	*manager_id, job_id
 La consulta debe calcular la suma de los salarios para cada uno de estos grupos. 

