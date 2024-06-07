# Desafio Casas Bahia 
<br>
<hr>
<br>
<br>


### Estrutura do Projeto


- `Dockerfile`: Arquivo de configuração para criar a imagem Docker.
- `data/`: Diretório contendo os dados do projeto.
- `label_encoder.pkl`: Arquivo do LabelEncoder.
- `random_forest_model.pkl`: Arquivo do modelo Random Forest.
- `test_api.py`: Script para teste da API.
- `README.md`: Documentação do projeto.
- `exploratory.ipynb`: Notebook Jupyter com análise exploratória.
- `preprocessor.pkl`: Arquivo do pré-processador.
- `src/`: Diretório contendo o código-fonte da aplicação.
- `venv/`: Ambiente virtual Python.

<br>

### Como usar a API

Requisitos Prévios
Docker instalado na sua máquina Docker Installation Guide

* Passo 1: Construindo a Imagem Docker

```bash
docker build -t casas-bahia-api .
```

* Passo 2: Executando o Contêiner

```bash
docker run -it --rm -p 8000:8000 casas-bahia-api:latest
```


* Passo 3: Testando a API
Você pode testar a API usando ferramentas como cURL, Postman ou qualquer biblioteca de requisições HTTP. Aqui está um exemplo de como fazer isso usando cURL:

```bash
curl -X POST -H "Content-Type: application/json"
-d '{"N_Days": 10, "Age": 50, "Bilirubin": 1.2, "Cholesterol": 200, "Albumin": 4.5, "Copper": 100, "Prothrombin": 80, "Stage": 1, "Drug": "Azathioprine", "Sex": "F", "Ascites": "yes", "Hepatomegaly": "no", "Spiders": "yes", "Edema": "no"}' http://localhost:8000/predict
```

* Passo 4: Parando e Removendo o Contêiner (Opcional)
Quando terminar de usar a API, você pode parar e remover o contêiner usando os seguintes comandos:

```bash
docker stop casas-bahia-api-container
docker rm casas-bahia-api-container
```

No script **test_api** tem a possibilidade de testar a API diretamente com o Python com duas opções de payload. 

<br>
<hr>
<br>
<br>

### Arquitetura de Deployment

Nessa secção contém um desenho de uma arquitetura de deployment que eu criei pensando nesse case, e também respondendo umas das perguntas feitas no documento do projeto. 
abaixo um diagrama com a arquitetura e a justificativa do uso de cada serviço escolhido. 


