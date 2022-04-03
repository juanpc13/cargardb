import psycopg2
try:
    connection = psycopg2.connect(user = "user",
                                  password = "pass!",
                                  host = "192.168.1.251",
                                  port = "5432",
                                  database = "dbname")    

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)


# dataFile = open('test', 'r')
dataFile = open('prototipo2-db.sql', 'r')
query = 'INSERT INTO public.acelerometro VALUES'
count=0
startLine = 0

def modQuery(txtQuery):
    modQuery = 'INSERT INTO acelerometro(id_dispositivo, x, y, z, date_time) VALUES('
    txtQuery = txtQuery.split('(')
    txtQuery = txtQuery[1]
    txtQuery = txtQuery.split(')')
    txtQuery = txtQuery[0]
    txtQuery = txtQuery.split(',')
    i = 0
    for txtValue in txtQuery:
        if i != 0:
            modQuery += txtValue + ','
        i += 1
    modQuery = modQuery[:-1]
    modQuery += ');'
    return modQuery

with dataFile as f:
    for line in f:
        count+=1
        if query in line and count >= startLine:
            cursor = connection.cursor()
            line = modQuery(line)
            print('Count=', count, ' SQL', line)
            cursor.execute(line)
            connection.commit()            

dataFile.close()
