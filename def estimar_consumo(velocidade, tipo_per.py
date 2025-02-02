def estimar_consumo(velocidade, tipo_percurso, distancia=None, combustivel_inicial=None):
    """
    Estima o consumo de combustível.

    Args:
        velocidade (int): Velocidade do carro em km/h.
        tipo_percurso (str): "cidade" ou "estrada".
        distancia (float, optional): Distância a ser percorrida em km.
        combustivel_inicial (float, optional): Quantidade inicial de combustível em litros.

    Returns:
        float: Consumo estimado em litros por 100 km.
        float (opcional): Quantidade de combustível restante ou necessário.
    """

    # Eficiência média aproximada (litros/100km):
    eficiencia_cidade = 10  # Ajuste conforme necessário
    eficiencia_estrada = 8  # Ajuste conforme necessário

    # Ajuste da eficiência com a velocidade (simplificado):
    # Aumentar o consumo em 10% a cada 10 km/h acima de 60 km/h
    fator_velocidade = 1 + (max(velocidade - 60, 0) // 10) * 0.1

    if tipo_percurso.lower() == "cidade":
        consumo = eficiencia_cidade * fator_velocidade
    else:
        consumo = eficiencia_estrada * fator_velocidade

    if distancia is not None:
        consumo_total = (consumo / 100) * distancia
        if combustivel_inicial is not None:
            restante = combustivel_inicial - consumo_total
            return consumo, restante
        else:
            return consumo, consumo_total

    return consumo

# Exemplo de uso:
velocidade = 80
tipo_percurso = "estrada"

distancia = 200
combustivel_inicial = 50

consumo, restante = estimar_consumo(velocidade, tipo_percurso, distancia, combustivel_inicial)

print(f"Consumo estimado: {consumo:.2f} L/100km")
print(f"Combustível restante: {restante:.2f} L")