from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import pickle
import numpy as np
import pandas as pd 
import os

# Inicializando a aplicação FastAPI
app = FastAPI()

# Definindo o esquema do payload para a entrada
class InputData(BaseModel):
    N_Days: int
    Age: int
    Bilirubin: float
    Cholesterol: float
    Albumin: float
    Copper: float
    Prothrombin: float
    Stage: int
    Drug: str
    Sex: str
    Ascites: str
    Hepatomegaly: str
    Spiders: str
    Edema: str

# Carregando o modelo, o pré-processador e o LabelEncoder
MODEL_PATH = os.getenv("MODEL_PATH")
PREPROCESSOR_PATH = os.getenv("PREPROCESSOR_PATH")
LABEL_ENCODER_PATH = os.getenv("LABEL_ENCODER_PATH")

with open(MODEL_PATH, 'rb') as model_file:
    model = pickle.load(model_file)

with open(PREPROCESSOR_PATH, 'rb') as preprocessor_file:
    preprocessor = pickle.load(preprocessor_file)

with open(LABEL_ENCODER_PATH, 'rb') as le_file:
    label_encoder = pickle.load(le_file)

# Definindo a rota POST para previsões
@app.post("/predict")
def predict(data: List[InputData]):
    try:
        # Convertendo o payload para um DataFrame
        df = pd.DataFrame([d.dict() for d in data])

        # Pré-processamento dos dados
        X_preprocessed = preprocess_data(df)

        # Fazendo a previsão
        y_pred = model.predict(X_preprocessed)

        # Convertendo previsões para os rótulos especificados
        predictions = []
        for pred in y_pred:
            if pred == 0:
                predictions.append("C")
            elif pred == 1:
                predictions.append("D")
            elif pred == 2:
                predictions.append("CL")

        # Retornando as previsões
        return {"predictions": predictions}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Função para pré-processar os dados
def preprocess_data(df):
    # Certificar-se de que todas as variáveis categóricas estejam presentes
    df['Drug'] = df['Drug'].astype('category')
    df['Sex'] = df['Sex'].astype('category')
    df['Ascites'] = df['Ascites'].astype('category')
    df['Hepatomegaly'] = df['Hepatomegaly'].astype('category')
    df['Spiders'] = df['Spiders'].astype('category')
    df['Edema'] = df['Edema'].astype('category')

    # Reordenar as colunas para corresponder ao modelo
    df = df[['N_Days', 'Age', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Prothrombin', 
             'Stage', 'Drug', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema']]
    
    # Transformar as variáveis categóricas em dummy
    df = pd.get_dummies(df)

    # Reordenar as colunas para corresponder à ordem esperada pelo modelo
    df = df.reindex(columns=[
        'N_Days', 'Age', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Prothrombin', 'Stage',
        'Drug_Azathioprine', 'Drug_D-penicillamine', 'Drug_Placebo', 'Sex_F', 'Sex_M',
        'Ascites_no', 'Ascites_yes', 'Hepatomegaly_no', 'Hepatomegaly_yes', 'Spiders_no', 'Spiders_yes',
        'Edema_no', 'Edema_yes'
    ], fill_value=0)  # Preencher com 0 se alguma variável não estiver presente
    
    return df.values  # Convertendo para um array NumPy


# Endpoint para verificar se a API está no ar
@app.get("/")
def read_root():
    return {"message": "API de previsão de Random Forest está no ar!"}
