import os
for filename in os.listdir("InstanciasSAT/"):
    print('Translating file: ' + filename)

    zincified = ''
    variables = []
    readpath = 'InstanciasSAT/' + filename
    enunciado = open(readpath, "r")

    for linea in enunciado:
        line = linea.lstrip()
        
        if line.strip():
            if line[0] == 'c':
                zincified += '%' + line[1:]
            elif line[0] == 'p':
                words = line.split()
                if words[1] != 'cnf':
                    print('Error en el formato del archivo (no es cnf)')
                    exit()
                else:
                    numvar = int(words[2])
                    numclause = int(words[3])
                    for x in range(numvar):
                        variables.append('X' + str(x))
                    for var in variables:
                        zincified += 'var 0..1: ' + var + '; var 0..1: n_' + var + ';\n'
                    zincified += '\n'
                    for var in variables:
                        zincified += 'constraint ' + var + ' + ' +  'n_' + var + ' = 1;\n'
            else:
                try:
                    clause = []
                    words = line.split()
                    for var in words:
                        variable = int(var)
                        literal = variables[abs(variable) - 1]
                        if variable < 0:
                            clause.append('n_' + str(literal))
                        elif variable > 0:
                            clause.append(str(literal))
                    zincified += '\nconstraint ' + str(clause[0])
                    for element in clause[1:]:
                        zincified += ' + ' + str(element)
                    zincified += '>= 1;'
                except:
                    continue
    enunciado.close()
    zincified += '\n\nsolve satisfy;\n\noutput ['
    for i in range(0, len(variables), 2):
        zincified += '"\\n' + str(variables[i]) + '=", show(' + str(variables[i]) + '), "\\t -' + str(variables[i]) + '=", show(n_' + str(variables[i]) + '), '
    zincified += '];'
    writepath = 'InstanciasMiniZinc/' + str(filename[:-4]) + '.mzn'
    zincfile = open(writepath, "w")
    zincfile.write(zincified)
    zincfile.close
