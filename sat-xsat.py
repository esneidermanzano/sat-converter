entrada = [
    (0, -2, 3),
    (2, -4, 5),
    (3, 6, 7),
    (3, 6, -7),
]

newvars = []


  

def three_sat_to_xsat(self, entrada, nvars, x):
    """This function get a 3-sat problem and return a x-sat instance"""
    # Esta variable, retornara la instancia x-sat
    salida = []
    # agrega las variables.
    ciclos = (x - 3)
    iterador = nvars
    for i in range(ciclos):    
        """ """
        for clausule in entrada:
            """ """
            iterador += 1
            newC = clausule.copy()
            clausule.append(iterador)
            newC = -iterador
            salida.append(clausule, newC)
    return salida
