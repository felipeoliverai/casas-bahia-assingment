# Usando a imagem base Python
FROM python:3.9-slim

# Definindo a pasta de trabalho como /app
WORKDIR /app

# Copiando o código da aplicação para o contêiner
COPY src/ .

# Copiando os arquivos .pkl para o contêiner
COPY *.pkl ./

# Instalando as dependências
RUN pip install --no-cache-dir fastapi uvicorn pandas scikit-learn requests

# Expondo a porta 8000
EXPOSE 8000

# Definindo variáveis de ambiente para os caminhos dos modelos
ENV MODEL_PATH="/app/random_forest_model.pkl"
ENV PREPROCESSOR_PATH="/app/preprocessor.pkl"
ENV LABEL_ENCODER_PATH="/app/label_encoder.pkl"

# Comando para executar a aplicação quando o contêiner for iniciado
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
