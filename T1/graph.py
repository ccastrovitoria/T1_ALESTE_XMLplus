import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

# Dados
entradas = [3, 4, 864, 11401, 76390, 447942, 2591314, 8795004]
tempos = [0.0026, 0.0027, 0.1360, 1.5125, 8.8084, 158.4369, 848.8728, 3399.8475]
casos = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"]

# Cores
azul_pastel = "#D5E5FD"
azul_contorno = "#6F86A6"
texto = "#243754"
grade = "#E7EBF0"

fig, ax = plt.subplots(figsize=(10, 6))

# Linha principal
ax.plot(
    entradas,
    tempos,
    marker="o",
    linewidth=2.4,
    markersize=7.5,
    color=azul_contorno,
    markerfacecolor=azul_pastel,
    markeredgecolor=azul_contorno,
)

# Área preenchida
ax.fill_between(
    entradas,
    tempos,
    0,
    color=azul_pastel,
    alpha=0.28
)

# Título
ax.set_title(
    "Tempo de execução por número de entradas",
    fontsize=15,
    fontweight="bold",
    color=texto,
    pad=16
)

# Eixos
ax.set_xlabel("Número de entradas", fontsize=11, color=texto, labelpad=14)
ax.set_ylabel("Tempo de execução (ms)", fontsize=11, color=texto, labelpad=14)

# Grade
ax.grid(True, linewidth=0.8, color=grade)

# Remove bordas
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Formatação do eixo X
ax.xaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"{int(x):,}".replace(",", "."))
)

# Formatação do eixo Y
ax.yaxis.set_major_formatter(
    FuncFormatter(lambda y, pos: f"{y:,.0f}".replace(",", "."))
)

# Mais marcações no eixo X
xticks = np.linspace(0, 9000000, 10)
ax.set_xticks(xticks)

# Rótulos C1, C2, ..., C8
for x, y, nome in zip(entradas, tempos, casos):
    ax.annotate(
        nome,
        (x, y),
        textcoords="offset points",
        xytext=(0, 8),
        ha="center",
        fontsize=9,
        color=texto
    )

fig.tight_layout()

# Salvar
fig.savefig("grafico_complexidade_rotulos.pdf", bbox_inches="tight")
fig.savefig("grafico_complexidade_rotulos.png", dpi=300, bbox_inches="tight")

plt.show()