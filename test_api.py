import requests
import json


def main():
    # URL da API FastAPI
    url = "http://localhost:8000/predict"

    # Payload JSON
    payload_1 = [
        {
            "N_Days": 2221,
            "Age": 25,
            "Bilirubin": 0.5,
            "Cholesterol": 149.0,
            "Albumin": 1.5,
            "Copper": 105.0,
            "Prothrombin": 9.9,
            "Stage": 2,
            "Drug": "Placebo",
            "Sex": "F",
            "Ascites": "yes",
            "Hepatomegaly": "yes",
            "Spiders": "no",
            "Edema": "no"
        }
    ]
    
    
    payload_2 = [
        {
            "N_Days": 1500,
            "Age": 45,
            "Bilirubin": 1.2,
            "Cholesterol": 220.0,
            "Albumin": 3.5,
            "Copper": 105.0,
            "Prothrombin": 12.5,
            "Stage": 2,
            "Drug": "D-penicillamine",
            "Sex": "M",
            "Ascites": "no",
            "Hepatomegaly": "yes",
            "Spiders": "no",
            "Edema": "no"
        }
    ]


    # Cabeçalhos HTTP
    headers = {
        "Content-Type": "application/json"
    }

    # Enviando a requisição POST
    response = requests.post(url, headers=headers, data=json.dumps(payload_1))

    # Verificando o status e imprimindo a resposta
    if response.status_code == 200:
        print("Predição bem-sucedida!")
        print("Resposta:", response.json())
    else:
        print("Erro na predição:", response.status_code)
        print("Detalhes:", response.json())


if __name__ == "__main__":
    main()
