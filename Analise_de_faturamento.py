import json

faturamento_json = '''
{
    "faturamento_diario": [1000, 2000, 0, 3000, 0, 1500, 0, 2500, 100, 4000]
}
'''

faturamento = json.loads(faturamento_json)['faturamento_diario']

faturamento = [valor for valor in faturamento if valor > 0]

menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)
dias_acima_da_media = len([valor for valor in faturamento if valor > media_mensal])

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
