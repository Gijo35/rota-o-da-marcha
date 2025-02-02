def rotacao_ideal(rotacao_atual, marcha_atual):
  """
  Determina se a rotação atual está dentro da faixa ideal para a marcha atual.

  Args:
    rotacao_atual: Rotação atual do motor em RPM.
    marcha_atual: Marcha engatada.

  Returns:
    True se a rotação estiver dentro da faixa ideal, False caso contrário.
  """

  # Faixas de rotação ideais (exemplo simplificado)
  faixas_ideais = {
    1: (1500, 2500),
    2: (2000, 3000),
    3: (2500, 3500),
    4: (3000, 4000),
    5: (3500, 4500)
  }

  faixa_ideal = faixas_ideais.get(marcha_atual, None)
  if faixa_ideal:
    return faixa_ideal[0] <= rotacao_atual <= faixa_ideal[1]
  else:
    return False

# Exemplo de uso
rotacao_atual = 2200
marcha_atual = 2

if rotacao_ideal(rotacao_atual, marcha_atual):
  print("A rotação está dentro da faixa ideal.")
else:
  print("A rotação está fora da faixa ideal. Considere trocar de marcha.")
