# Ejemplos SQL - Cap 3
# funciones Escalares

1.	Ejemplo de funciones de conversion de tipos de datos numericos para manejar diferente cantidad de decimales 

	DECLARE @i FLOAT = 9.477756

	SELECT 
      ROUND(@i, 2)
    , FORMAT(@i, 'N2')
    , CAST(@i AS DECIMAL(18,2))
    , SUBSTRING(PARSENAME(CAST(@i AS VARCHAR(10)), 1), PATINDEX('%.%', CAST(@i AS VARCHAR(10))) - 1, 2)
    , FLOOR((@i - FLOOR(@i)) * 100)

	Resultado esperado:
	
	----------------------
	9,48
	9.48
	9.48
	94
	94