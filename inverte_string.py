def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

# Definindo a string para inverter
string_original = "Exemplo"
string_invertida = inverter_string(string_original)

print(f"Original: {string_original}")
print(f"Invertida: {string_invertida}")
