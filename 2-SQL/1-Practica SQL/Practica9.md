# Práctica SQL - Número 9
1.	Agregue una restricción PRIMARY KEY de nivel de tabla a la tabla EMP en la columna ID. Debe asignar el nombre my_emp_id_pk a la restricción en el momento de su creación. 
	Indicación: La restricción se activa tan pronto como se ejecuta el comando ALTER TABLE
	correctamente.
	
2.	Cree una restricción PRIMARY KEY en la tabla DEPT utilizando la columna ID. Debe asignar el nombre my_dept_id_pk a la restricción en el momento de su creación. 
	Indicación: La restricción se activa tan pronto como se ejecuta el comando ALTER TABLE	correctamente.
	
3.	Agregue una columna DEPT_ID a la tabla EMP. Agregue una referencia de clave ajena en la tabla EMP que asegure que no se asigna el empleado a un departamento no existente. Llame a la restricción my_emp_dept_id_fk.

4.	Confirme que se agregaron las restricciones consultando la vista USER_CONSTRAINTS. Anote los tipos y los nombres de las restricciones. Guarde el texto de sentencias en un archivo llamado BBDDIILab10_4.sql.
