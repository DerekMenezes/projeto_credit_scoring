# projeto_credit_scoring

Acesse em: <https://credit-scoring-mfxn.onrender.com/>

## Visualização da Aplicação



## Credit Scoring

Este repositório contém a implementação de um sistema de Credit Scoring, que inclui análise exploratória de dados, pré-processamento, treinamento de modelo e uma aplicação para escoragem utilizando Streamlit.

## 📌 Estrutura do Projeto

data/ - Diretório contendo a base de dados utilizada no projeto.

notebooks/ - Contém os Jupyter Notebooks com as análises exploratórias:

analise_univariada.ipynb - Análise de variáveis individuais (também disponível com ydata-profiling).

analise_bivariada.ipynb - Análise entre pares de variáveis.

scripts/ - Contém os scripts Python para processamento e modelagem:

preprocessamento.py - Pipeline de pré-processamento dos dados.

model_training.py - Treinamento do modelo utilizando PyCaret.

model_final.pkl - Modelo treinado.

streamlit_app.py - Aplicação para escoragem no Streamlit.

README.md - Este arquivo.

video_demo.mp4 - Vídeo demonstrando o funcionamento da aplicação.

## 🔧 Instalação

Clone este repositório e instale as dependências:

 git clone https://github.com/seuusuario/credit_scoring.git
 cd credit_scoring
 pip install -r requirements.txt

## 🏗️ Uso

1️⃣ Pré-processamento dos Dados

Execute o pipeline de pré-processamento:

python scripts/preprocessamento.py

2️⃣ Treinamento do Modelo

Para treinar um novo modelo com PyCaret:

python scripts/model_training.py

3️⃣ Rodando o Streamlit

Para iniciar a aplicação de escoragem:

streamlit run scripts/streamlit_app.py

A interface permitirá o upload de um arquivo Excell para ser escorado com o modelo treinado.

## 📤 Submissão

Todos os códigos desenvolvidos foram enviados para o GitHub. O link do repositório foi enviado para o tutor para correção.

