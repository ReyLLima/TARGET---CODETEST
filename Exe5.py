def inverter_string(s):
    inver_string = ""
    for i in range(len(s) - 1, -1, -1):
        inver_string += s[i]  # Adiciona o caractere atual ao resultado
    return inver_string

string_original = input("Entre com a palavra ou frase: ")

inver_string = inverter_string(string_original)
print(inver_string)
