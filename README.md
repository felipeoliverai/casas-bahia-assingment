# Desafio Casas Bahia 
<br>
<hr>
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

<br>

* Passo 2: Executando o Contêiner

```bash
docker run -it --rm -p 8000:8000 casas-bahia-api:latest
```

<br>

* Passo 3: Testando a API
Você pode testar a API usando ferramentas como cURL, Postman ou qualquer biblioteca de requisições HTTP. Aqui está um exemplo de como fazer isso usando cURL:

```bash
curl -X POST -H "Content-Type: application/json" -d '[
    {
        "N_Days": 10,
        "Age": 50,
        "Bilirubin": 1.2,
        "Cholesterol": 200,
        "Albumin": 4.5,
        "Copper": 100,
        "Prothrombin": 80,
        "Stage": 1,
        "Drug": "Azathioprine",
        "Sex": "F",
        "Ascites": "yes",
        "Hepatomegaly": "no",
        "Spiders": "yes",
        "Edema": "no"
    }
]' http://localhost:8000/predict

```
<br>


* Passo 4: Parando e Removendo o Contêiner (Opcional)
Quando terminar de usar a API, você pode parar e remover o contêiner usando os seguintes comandos:

```bash
docker stop casas-bahia-api-container
docker rm casas-bahia-api-container
```
<br>

No script **test_api** tem a possibilidade de testar a API diretamente com o Python com duas opções de payload, dessa forma: 

```bash
python test_api.py
```

<br>
<hr>
<br>
<br>

### Arquitetura de Deployment

Nessa secção contém um desenho de uma arquitetura de deployment que eu criei pensando nesse case, e também respondendo umas das perguntas feitas no documento do projeto. 
abaixo um diagrama com a arquitetura e a justificativa do uso de cada serviço escolhido. 

<br>

![alt text](https://github.com/felipeoliverai/casas-bahia-assingment/blob/main/images/gcp-arquitetura.png)

<br>

Quando decidi escolher as ferramentas para deployar meus modelos na Google Cloud Platform (GCP), levei em consideração a eficiência, escalabilidade e integração entre os serviços. Cada serviço na arquitetura desempenha um papel crucial no processo de deployment e inferência dos modelos de machine learning:

- BigQuery (ML Feature): Optei pelo BigQuery para armazenar as features utilizadas no treinamento dos modelos. Sua capacidade de processar grandes volumes de dados de forma eficiente e oferecer recursos avançados de consulta foi fundamental para lidar com nossas necessidades de dados.

- Vertex Pipelines (Train model): Escolhi o Vertex Pipelines para orquestrar e executar nossos pipelines de machine learning. Ele simplifica o processo de treinamento, permitindo a criação de pipelines reproduzíveis e escaláveis, o que é essencial para garantir a qualidade e eficiência do treinamento dos modelos.

- Cloud Storage (Trained model): Para armazenar os modelos treinados, o Cloud Storage foi a escolha ideal. Sua confiabilidade e escalabilidade garantem que nossos modelos estejam sempre disponíveis para implantação e inferência.

- Vertex Pipelines (Batch predict): Utilizei novamente o Vertex Pipelines, desta vez para executar pipelines de previsão em lote. Sua capacidade de coordenação e escalabilidade é essencial para lidar com grandes volumes de dados durante o processo de inferência.

- Datastore (predictions): Optei pelo Datastore para armazenar as previsões geradas pelos modelos. Sua capacidade de escalabilidade e recuperação rápida de dados semiestruturados é ideal para armazenar e recuperar os resultados das previsões.

- BigQuery (predictions): Embora o Datastore seja utilizado para armazenar as previsões, optei pelo BigQuery para análises mais complexas sobre esses dados. Suas poderosas capacidades de análise e consulta SQL são ideais para explorar e extrair insights dos resultados das previsões.

- Cloud Run (serving API): Escolhi o Cloud Run para hospedar a API de serviço dos modelos, permitindo inferências em tempo real. Sua escalabilidade automática e gerenciamento de contêineres tornam a implantação e o dimensionamento da API simples e eficientes."

Essa abordagem foi planejada para garantir que cada componente da arquitetura contribua para um processo de deployment robusto e eficaz de modelos de machine learning na GCP.

<br>
<br>




