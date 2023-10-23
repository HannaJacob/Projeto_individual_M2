# Dicionário para armazenar os resultados dos candidatos
resultados = {
    'Hanna Jacob': {'entrevista': 5, 'teste_teórico': 10, 'teste_prático': 8, 'soft_skills': 8},
    'Jon Snow': {'entrevista': 10, 'teste_teórico': 7, 'teste_prático': 7, 'soft_skills': 8},
    'Olivia Pope': {'entrevista': 8, 'teste_teórico': 5, 'teste_prático': 4, 'soft_skills': 9},
    'Daenerys Targaryen': {'entrevista': 2, 'teste_teórico': 2, 'teste_prático': 2, 'soft_skills': 1},
    'Cosima Niehaus': {'entrevista': 10, 'teste_teórico': 10, 'teste_prático': 8, 'soft_skills': 9},
}

# Função para buscar candidatos com base nos critérios digitados pelo usuário
def buscar_candidatos(criterio_e, criterio_t, criterio_p, criterio_s):
    candidatos_atendendo_criterio = []
    for candidato, avaliacoes in resultados.items():
        if (avaliacoes['entrevista'] >= criterio_e and
            avaliacoes['teste_teórico'] >= criterio_t and
            avaliacoes['teste_prático'] >= criterio_p and
            avaliacoes['soft_skills'] >= criterio_s):
            candidatos_atendendo_criterio.append(candidato)
    
    return candidatos_atendendo_criterio

# Solicitar critérios ao usuário
criterio_e = int(input('Informe a nota mínima de entrevista: '))
criterio_t = int(input('Informe a nota mínima do teste teórico: '))
criterio_p = int(input('Informe a nota mínima do teste prático: '))
criterio_s = int(input('Informe a nota mínima de avaliação de soft skills: '))

# Buscar candidatos que atendem aos critérios
candidatos_atendendo_criterio = buscar_candidatos(criterio_e, criterio_t, criterio_p, criterio_s)

if candidatos_atendendo_criterio:
    print(f'Os candidatos {candidatos_atendendo_criterio} atendem aos critérios')
else:
    print('Nenhum candidato atende aos critérios especificados.')
