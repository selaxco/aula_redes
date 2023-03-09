def funcao_objetivo_CB(individuo): #computa uma métrica do objetivo; nesse caso, é computado a soma dos valores de cada gene
    '''computa a função objetivo no problema das caixas binárias
    
    Args: 
        indivíduos: lista contendo os genes das caixas binárias
        
    Return valor que representa a soma dos genes de cada indivíduo '''
    return sum(individuo) 
