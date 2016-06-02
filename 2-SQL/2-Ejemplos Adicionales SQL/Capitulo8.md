# Ejemplo SQL Transacciones y niveles de aislamiento 

Dado que existen los siguientes niveles de aislamiento en SQL Server:

    *Read uncommitted
    *Read committed
    *RepeaTabla read
    *Serializable
    *Snapshot

##Probar para cada uno de los siguientes casos

1. serializable
```
update Tabla set Campo=1	
set transaction isolation level serializable;

            begin tran                        
                update Tabla set Campo=2
                waitfor delay '00:00:30'                
            commit
```
2. read commited
```
update Tabla set Campo=1
set transaction isolation level read commited;

            begin tran                        
                update Tabla set Campo=2
                waitfor delay '00:00:30'                
            commit
```
3. repeaTabla read
```update Tabla set Campo=1
set transaction isolation level repeaTabla read;

            begin tran                        
                update Tabla set Campo=2
                waitfor delay '00:00:30'                
            commit
```
4. read committed
```
update Tabla set Campo=1
set transaction isolation level read committed;

            begin tran                        
                update Tabla set Campo=2
                waitfor delay '00:00:30'                
            commit
```
5. read uncommitted
```
update Tabla set Campo=1
set transaction isolation level read uncommitted;

            begin tran                        
                update Tabla set Campo=2
                waitfor delay '00:00:30'                
            commit
```
6. snapshot
```
update Tabla set Campo=1
set transaction isolation level snapshot;

            begin tran                        
                update Tabla set Campo=2
                waitfor delay '00:00:30'                
            commit
```

##Siempre en paralelo ejecutar la siguientes sentencias y verificar que sucede en cada caso 

```
select * from Tabla
delete from Tabla where Campo=1
insert into Tabla (Campo) values ('Data')
update from Tabla where Campo =3
```
Luego agregando diferentes niveles de bloqueo a las tablas a traves de los "hints" tratar de modificar el comportamiento de las sentencias ejecutadas

###Para consultar

*[Referencia sobre Hints](https://msdn.microsoft.com/es-AR/library/ms187373.aspx)

*[Articulo explicando el uso de locks y los niveles de aislamiento](http://www.sql-server-performance.com/2013/transactions-locking/)
