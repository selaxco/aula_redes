import random

def funcao_objetivo_CB(individuo): #computa uma métrica do objetivo; nesse caso, é computado a soma dos valores de cada gene
    '''computa a função objetivo no problema das caixas binárias
    
    Args: 
        indivíduos: lista contendo os genes das caixas binárias
        
    Return valor que representa a soma dos genes de cada indivíduo '''
    return sum(individuo) + 1 # o + 1 foi adicinado para não dar erro na hora de considerar um peso igual a zero

# criar uma lista para representar os indivíduos
# cada elemento da lista é um gene
# cada gene pode ser 1 ou 0

def funcao_objetivo_pop_cb(populacao):
    '''Calcula a função objetivo para cada indivíduo da população.
    
    Args:
        populacao: lista com todos os individuos da população
    
    Returns: 
        '''
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_CB(individuo)
        fitness.append(fobj)
    
    return fitness

def gene_CB():
    '''gera um gene válido para o problema das caixas binárias
    Return 0 ou 1'''
    lista = [0, 1]
    gene = random.choice(lista)
    return gene

def individuo_CB(n):
    '''gera um indivíduo para o problema das caixas binárias
    
    Args: 
        n: número de genes do indivíduo
        
    Return lista com n genes. cada gene é um valor 0 ou 1'''
    
    individuo = []
    for i in range(n):
        gene = gene_CB()
        individuo.append(gene)
    
    return individuo

def população_cb(tamanho, n):
    '''Cria uma população no problema das caixas binárias. 
    
    Args:
    tamanho: tamanho da população
    n = quantidade de genes
    
    return Uma lista onde cada item é um indivíduo. Um indivíduo é uma lista com n genes.'''
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_CB(n))
        
    return populacao






def selecao_roleta_max(populacao, fitness):
    '''Seleciona indivpiduos d euma população usando o método da roleta. 
    
    Nota: apenas funciona para problemas de maximização.
    
    Args:
        populacao: lista com todos os indivpiduos da população
        fitness: lista com o valor da funcao objetivo dos individuos da população
        
    Returns:
    População dos indivíduos selecionados.
    '''
    populacao_selecionada = random.choices(populacao, weights = fitness, k = len(populacao))
    
    return populacao_selecionada

def cruzamento_ponto_simples(pai, mae):
    '''Operador de cruzamento de ponto simples.
    
    Args:
        pai: uma lista representando indivíduo
        mae: um lista representando indivíduo
    
    Returns:
        Retorna duas listas, de forma que cada um representa um filho dos pais que foram argumentos'''
    ponto_de_corte = random.randint(1, len(pai) - 1) # não pode começar do zero e nem pode terminar no último valor da lista
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2

def mutacao_cb(individuo):
    '''Realiza a mutação de um gene no problema das caixas binárias.
    
    Args:
        Indivíduo: uma lista representando um indivíduo no problema das caixas binárias
    
    Returns:
        Um indivíduo com um gene mutado.'''
    
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_CB()
    return individuo