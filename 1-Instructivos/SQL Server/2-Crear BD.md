# BBDDII

## Instructivos para realizar las prácticas de la materia 

## Creacion de una nueva Base de Datos en SQL Server

Ejecutar el Siguiente comando en una nueva ventana del Management Studio para crear la Basa llamada "NuevaDB"

USE master ;
GO
CREATE DATABASE NuevaDB
ON 
( NAME = NuevaDB_dat,
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL12.MSSQLSERVER\MSSQL\DATA\NuevaDBdat.mdf',
    SIZE = 10,
    MAXSIZE = 50,
    FILEGROWTH = 5 )
LOG ON
( NAME = NuevaDB_log,
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL12.MSSQLSERVER\MSSQL\DATA\NuevaDBelog.ldf',
    SIZE = 5MB,
    MAXSIZE = 25MB,
    FILEGROWTH = 5MB ) ;
GO

fuente : https://msdn.microsoft.com/es-es/library/ms186312(v=sql.120).aspx

