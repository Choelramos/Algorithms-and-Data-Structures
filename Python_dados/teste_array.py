# Cada corte depois do comentário é um teste

nomes = ["Joel", "Julia", "Matias"]
print(nomes)

x = nomes[2]
print(x)
# =============================================================
y = len(nomes)
print(f'O tamanho da lista é: {y}')
# =============================================================
for x in nomes:
    print(x)
# =============================================================
nomes.append('Pandora')
print(nomes)
# =============================================================
nomes.remove('Pandora')
print(nomes)
# =============================================================
nomes.pop(1)
print(nomes)
