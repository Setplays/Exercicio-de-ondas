# 🌊 Simulador de Ondas 3D

## 📖 Sobre o Projeto
Este é um simulador visual de ondas desenvolvido em Python. O projeto utiliza matemática para criar a ilusão de um plano 3D afetado por perturbações físicas. Focado em ser leve e visualmente relaxante, o simulador renderiza a superfície da onda não como uma malha sólida, mas como uma nuvem de partículas flutuando em um ambiente escuro.

Nesta versão específica, uma única onda suave e de baixa amplitude se origina da extremidade esquerda do plano e se propaga para a direita, criando um efeito de marola em câmera lenta.

## ✨ Funcionalidades
* **Renderização Otimizada:** Utiliza `ax.scatter` do Matplotlib ao invés de superfícies sólidas, garantindo que o programa seja incrivelmente leve.
* **Atualização Dinâmica:** O loop de animação atualiza apenas as coordenadas de altura, economizando processamento (CPU/GPU).
* **Física Aplicada:** Utiliza a função senoidal combinada com um fator de decaimento exponencial para simular o amortecimento natural da onda.
* **Estética Minimalista:** Fundo 100% preto e partículas em verde-claro para máximo contraste.

## 🚀 Como Executar o Simulador
Para visualizar a simulação, você não precisa ter o Python instalado ou configurar nenhum ambiente complexo:
1. Faça o download do arquivo executável (`.exe`) fornecido nos *Releases* deste projeto.
2. Dê um duplo clique no arquivo baixado.
3. A janela de simulação se abrirá automaticamente!

## 📦 Como Compilar o Executável (Para Desenvolvedores)
Caso você queira modificar o código e gerar a sua própria versão do executável, utilize o **PyInstaller**. 

Se estiver enfrentando o erro `No module named pyinstaller` no Windows (muito comum em instalações isoladas), você deve utilizar o caminho absoluto para o executável do PyInstaller localizado dentro da pasta `Scripts` da sua instalação do Python. 

Exemplo de uso com o caminho absoluto (altere o diretório conforme a sua máquina):
```bash
C:\Caminho\Para\Seu\Python\Scripts\pyinstaller.exe --clean --onefile --windowed --icon=caveira.ico onda_cmd.py
```
