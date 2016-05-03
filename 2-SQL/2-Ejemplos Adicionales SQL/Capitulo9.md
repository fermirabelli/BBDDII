# Ejemplo SQL

-- Desactivar todas las restricciones en SQL Server
EXEC sp_msforeachtable "ALTER TABLE ? NOCHECK CONSTRAINT all"

-- Activar Todas las restricciones en SQL Server
EXEC sp_msforeachtable "ALTER TABLE ? WITH CHECK CHECK CONSTRAINT all"