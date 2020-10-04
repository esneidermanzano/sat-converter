import os
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
    print (comments)
    zincified = ""
    for i in range(0, len(clauses)):
        zincified += '\n' + " ".join(str(x) for x in clauses[i]) + " 0"

    writepath = 'X-SAT/' + str(filename[:-4]) + '.cnf'
    zincfile = open(writepath, "w")
    zincfile.write(zincified)
    zincfile.close
