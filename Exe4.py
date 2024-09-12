values = {
"SP" : 67836.43,
"RJ" : 36678.66,
"MG" : 29229.88,
"ES" : 27165.48,
"Outros" : 19849.53
}

totalmensal = sum(values.values())
valor_sp = (100 * values["SP"]) / totalmensal
valor_rj = (100 * values["RJ"]) / totalmensal
valor_mg = (100 * values["MG"]) / totalmensal
valor_es = (100 * values["ES"]) / totalmensal
valor_outros = (100 * values["Outros"]) / totalmensal



print(f"O percentual que corresponde ao estado de São Paulo é aproximadamente: {valor_sp:.2f}%")
print(f"O percentual que corresponde ao estado do Rio de Janeiro é aproximadamente: {valor_rj:.2f}%")
print(f"O percentual que corresponde ao estado de Minas Gerais é aproximadamente: {valor_mg:.2f}%")
print(f"O percentual que corresponde ao estado de Espírito Santo é aproximadamente: {valor_es:.2f}%")
print(f"O percentual que corresponde aos outros estados é aproximadamente: {valor_outros:.2f}%")
