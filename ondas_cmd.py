import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Configuração da figura com fundo totalmente preto
cor_fundo = 'black'
fig = plt.figure(figsize=(12, 8), facecolor=cor_fundo)
fig.canvas.manager.set_window_title('Simulador de Onda - Esquerda')

ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor(cor_fundo)
ax.axis('off') # Remove eixos e linhas de grade

# 2. Malha otimizada para ser muito leve (70x70 pontos)
x = np.linspace(-15, 15, 70)
y = np.linspace(-15, 15, 70)
X, Y = np.meshgrid(x, y)

# 3. Origem da onda na borda esquerda (x = -15, centro em y = 0)
x0, y0 = -15, 0
R = np.sqrt((X - x0)**2 + (Y - y0)**2)

# Z inicial no tempo 0 (Amplitude bem pequena: 0.2)
Z = 0.2 * np.sin(R) * np.exp(-0.03 * R)

# Desenha os pontinhos iniciais (verde claro, tamanho 3)
scatter_plot = ax.scatter(X.flatten(), Y.flatten(), Z.flatten(), color='lightgreen', s=3)

# Fixa o limite de altura para a câmera não pular
ax.set_zlim(-1.5, 1.5)

# 4. Função de atualização (extremamente leve)
def update(frame):
    # O tempo passa bem devagar (frame * 0.05)
    t = frame * 0.05
    
    # Única onda suave vindo da esquerda, sem superposições
    Z_new = 0.2 * np.sin(R - t * 2.0) * np.exp(-0.03 * R)
    
    # Atualiza apenas as coordenadas Z dos pontos existentes
    scatter_plot._offsets3d = (X.flatten(), Y.flatten(), Z_new.flatten())
    
    return scatter_plot,

# 5. Execução da animação
ani = FuncAnimation(fig, update, frames=300, interval=40, blit=False)

plt.show()