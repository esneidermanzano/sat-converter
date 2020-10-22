import os
"""
for filename in os.listdir("InstanciasSAT/"):
    print('Translating file: ' + filename)

    comments = ''
    nvar = 0
    nclauses = 0
    clauses = []
    readpath = 'InstanciasSAT/' + filename
    enunciado = open(readpath, "r")
    
    for linea in enunciado:
        line = linea.lstrip()
        if line.strip():
            if line[0] == 'c':
                comments += line[0:]

            elif line[0] == 'p':
                words = line.split()
                if words[1] != 'cnf':
                    print('El archivo no es cnf!!')
                    exit()

                else:
                    nvar = int(words[2])
                    nclauses = int(words[3])

            else:
                clause = []
                words = line.split()
                for var in words:
                    variable = int(var)
                    clause.append(variable)
                clause.pop()
                clauses.append(clause)

                       
                
    enunciado.close()
    print (clauses)
    zincified = ""
    for i in range(0, len(clauses)):
        zincified += '\n' + " ".join(str(x) for x in clauses[i]) + " 0"

    writepath = 'X-SAT/' + str(filename[:-4]) + '.cnf'
    zincfile = open(writepath, "w")
    zincfile.write(zincified)
    zincfile.close
"""
sat = [
    [3,4],
    [1, -2, 3, 5, 6, 7, 8, 9, 10, 11],
    [1]
]

vares = 11
def sat_to_3sat(sat, vares):
    newCla = []
    for clausula in sat:
        lenght = len(clausula)
        if lenght==1: 
            newCla.append([clausula[0], vares+1, vares+2])
            newCla.append([clausula[0], vares+1, -1*(vares+2)])
            newCla.append([clausula[0], -1*(vares+1), vares+2])
            newCla.append([clausula[0], -1*(vares+1), -1*(vares+2)])
            vares+=2
        elif lenght==2:
            newCla.append([clausula[0], clausula[1], vares+1])
            newCla.append([clausula[0], clausula[1], -1*(vares+1)])
            vares+=1
        elif lenght==3:
            newCla.append(clausula)
        else:
            newCla.append([clausula[0], clausula[1], vares+1])
            for i in range(2, lenght-2):
                newCla.append([ -1*(vares+1), clausula[i], vares+2])
                vares+=1
            newCla.append([ -1*(vares+1), clausula[lenght-2], clausula[lenght-1]])
            vares+=1
          
    print(newCla)
            
sat_to_3sat(sat, vares)

