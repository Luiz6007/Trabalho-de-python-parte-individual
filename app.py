import matplotlib.pyplot as plt
import pandas as pd

# Dados ilustrativos (em milhões de mulheres)
dados = {
    "Região": [
        "Norte",
        "Nordeste",
        "Sudeste",
        'Sul',
        "Centro-Oeste"
    ],
    "Mulheres empregadas": [
        3.5,
        9.2,
        15.8,
        6.2,
        3.1
    ]
}

df = pd.DataFrame(dados)

# Criando o gráfico
plt.figure(figsize=(10, 6))

barras = plt.bar(
df["Região"],
df["Mulheres empregadas"],
color="mediumpurple",
edgecolor="black",
)

# Valores acima das barras
for barra in barras:
    altura = barra.get_height()
    plt.text(
        barra.get_x() +
     barra.get_width() / 2,
        altura,
        f"{altura:.1f} milhões",
        ha="center",
        va="bottom",
        fontsize=10,
    )

# Personalização

plt.title(
    "Mulheres no Mercado de Trabalho por Região",
    fontsize=15,
)

plt.xlabel("Regiões do Brasil", fontsize=12)
plt.ylabel("Quantidade de Mulheres Empregadas (em milhões)", fontsize=11)

plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.show()