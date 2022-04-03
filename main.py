import psycopg2

# Datos del servidor
conn = psycopg2.connect(host="servicio.ca", database="principal", user="postgres", password="abc123", port="5433", connect_timeout=4)

def getCursor():
  try:
    cur = conn.cursor()
    return cur
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    return None

# Archivo TXT
dataFile = open('DATALOG.TXT', 'r')

# Iteracion de linea
count=0
startLine = 0

# Datos del SQL
idInvestigacion = 3

## METODOS
def makeQuery(line):
    newQuery = 'INSERT INTO humedad_relativa(id_investigacion, rh, fecha_registrado) VALUES ($, $, $);'
    arrayData = line.split(',')
    timestamp = arrayData[0].split('/')
    timestamp = "'20" + timestamp[2] + '-' + timestamp[1] + '-' + timestamp[0] + ' ' + arrayData[1] + "'"
    # Asignado idInvestigacion
    newQuery = newQuery.replace('$', str(idInvestigacion), 1)
    # Asignado temperatura
    newQuery = newQuery.replace('$', str(arrayData[6]), 1)
    # Asignado la fecha
    newQuery = newQuery.replace('$', timestamp, 1)
    return newQuery

with dataFile as f:
    cursor = conn.cursor()
    for line in f:
        count += 1
        query = makeQuery(line)        
        cursor.execute(query)
        print('Count=', count, ' SQL', query)
    conn.commit()
    cursor.close()

dataFile.close()

