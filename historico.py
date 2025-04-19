def analisar_padroes(historico_str):
    cores = [cor.strip().lower() for cor in historico_str.split(",") if cor.strip()]
    
    if len(cores) < 5:
        return "Poucos dados para análise. Cole pelo menos 5 entradas."

    analise = ""
    vermelho = cores.count("vermelho")
    preto = cores.count("preto")
    branco = cores.count("branco")

    analise += f"Total de entradas: {len(cores)}\n"
    analise += f"Vermelhos: {vermelho} | Pretos: {preto} | Brancos: {branco}\n\n"

    if cores[-1] == "branco":
        analise += "Última cor foi BRANCO. Atenção: tendência de branco seguido pode ocorrer.\n"
    
    if len(cores) >= 2 and cores[-1] == cores[-2]:
        analise += "Últimas duas cores repetidas. Chance de repetição tripla aumentada.\n"

    if len(cores) >= 3 and cores[-1] != cores[-2] and cores[-2] != cores[-3]:
        analise += "Padrão alternado detectado. Próxima cor pode repetir uma das últimas.\n"

    return analise