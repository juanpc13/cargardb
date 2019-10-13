# dataFile = open('test', 'r')
dataFile = open('prototipo2-db.sql', 'r')
query = 'INSERT INTO public.acelerometro VALUES'
count=0

with dataFile as f:
    for line in f:        
        if query in line:
            count+=1      
                  
print(count)
dataFile.close()
