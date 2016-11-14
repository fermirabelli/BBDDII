import urllib.request
import csv
import pypyodbc as pyodbc
import sys
from datetime import datetime
from bs4 import BeautifulSoup


user='sa'
password='-'
database='statebike'
port='1433'
TDS_Version='8.0'
server='BBDDII'
driver='{SQL Server Native Client 11.0}'

con_string='Uid=%s;Pwd=%s;Database=%s;Server=%s;driver=%s' % (user,password,database,server,driver)
cnxn=pyodbc.connect(con_string)
cursor=cnxn.cursor()

sqltext =("INSERT INTO estado ([estacionid],[bicicletasdisponibles],[numero],[anclajedisponible]) VALUES (%s,%s,%s,%s)" %('0','0','0','0'))
cursor.execute(sqltext)
cnxn.commit()
print ('Error HTTP')
sys.exit(0)
