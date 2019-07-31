import csv
with open('output.csv' , newline='') as csvfile:
  fileContents = csv.reader(csvfile, delimiter=',',)
  for row in fileContents:
    print(f'{row[2]}\t{row[3]}')
    
def getReqAndRes(): 
  sources = []
  destinations = []
  info = []
  protocols = []
  with open('output.csv' , newline='') as csvfile:
    fileContents = csv.reader(csvfile, delimiter=',',)
    for row in fileContents:
      sources.append(row[2])
      destinations.append(row[3])
      info.append(row[6])
      protocols.append(row[4])

  for i in range(0,773):
    for j in range(0,773):
      if sources[i]==destinations[j] and info[i].find("GET") != -1 and i>j :
        print(f'{protocols[i]} \t {info[i]}')

getReqAndRes()


  

