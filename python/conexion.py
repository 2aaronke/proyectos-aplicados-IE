import psycopg2

try:
    conn= psycopg2.connect(database= 'prueba1', user = 'admin', password='brasil', host='localhost', port='5432')
    print('se ha conectado con base de datos')
except:
    print('no se pudo conectar')

conectar= conn.cursor()
try:

