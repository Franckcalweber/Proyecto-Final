#testando como e faser uma solicitacao API
#importar as bibliotecas
import requests
from dotenv import load_dotenv
load_dotenv()
import os
chave_api = os.getenv("ORS_API_KEY")
#print(chave_api is not None)
"""fazendo a pergunta para indentificar a intencao do usuario. """
pergunta = input("voce gostaria de apenas informacoes? ou prentende fazer uma viagem ?").strip().lower()
"""condicionais, se apenas informacoes vai mostras apenas as informacoes da cidade."""
if pergunta == "informacoes":
    print("entendido, me informe informe a cidade. ")
    cidade = input("qual a cidade?")
    #print(cidade)
    #print(type(cidade))
    #print("biblioteca carregada!")
    """criar a variavel para guarda o endereco da API"""
    url = "https://geocoding-api.open-meteo.com/v1/search"#endereco da api que estamos cosultando
    parametros = {"name":cidade,"count":1} # parametros informacoes que mandamos para a api para informar oque buscamos.
    resposta = requests.get(url,params=parametros)#pedimos o acesso a api e guardamos o resultado
    dados = resposta.json()# converte a resposta jsom em python como listas e dicionarios
    #print(dados)
    local = dados["results"][0] #acessando a chave results de um dicionario, o indice 0 indica qual elemento da lista queremos acessar. 
    codigo_pais = local["country_code"] #acessamos a chave country_cody do dicionario local onde esta informacoes do codigo do pais 
    #jprint("country_code:", local["country_code"])
    print("cidade:",local["name"])
    fuso_horario = local["timezone"] # aqui acessamos a cheve timezone do dicionario local onde esta a informacao do fuso horario da cidade
    print("fuso_horario:",fuso_horario)
    url_moeda = "https://countries.dev/alpha/" + codigo_pais #aqui e um edereco de uma api que conten informacao da moeda do pais e buscamos isso acrescentando o codigo do pais no final 
    #print(url_moeda)
    # aqui para baixo os comando sao os mesmos,, guarda informacoes, acessar chaves em dicinarios, requisitar acessos, converter dados
    resposta_moeda = requests.get(url_moeda)
    dados_moeda = resposta_moeda.json()
    #print(dados_moeda.keys())
    #print(dados_moeda["currencies"])
    simbolo_moeda = dados_moeda["currencies"][0]["symbol"]
    moeda_local = dados_moeda["currencies"][0]["name"]
    print(f"moeda local: {moeda_local} { simbolo_moeda}")
    lon = local ["longitude"]
    lat = local ["latitude"]
    print("latidude:", local["latitude"])
    #print(local)
    print("longitide:", local["longitude"])
    url_clima = "https://api.open-meteo.com/v1/forecast"
    params_clima = {
    "latitude": lat, 
    "longitude":lon,
    "current": "temperature_2m"
    }
    parametros_horas = {"timezone":fuso_horario}
    url = "https://timeapi.io/api/v1/time/current/zone"
    resposta = requests.get(url,params=parametros_horas)
    #print(resposta.json())
    dados_horas = resposta.json()
    print("Hora local:", dados_horas["time"][:5])

    resposta_clima = requests.get(url_clima,params=params_clima)
    dados_clima = resposta_clima.json()
    #print(dados_clima)
    temperatura = dados_clima["current"]["temperature_2m"]
    print("temperatura", temperatura, "graus c")


elif pergunta == "viagem":
    print("perfeito, vamos viajar!")
    cidade_destino = input("Para qual cidade de destino?").strip().lower()
    cidade_origem = input("Qual cidade de origem ?").strip().lower()
    url = "https://geocoding-api.open-meteo.com/v1/search"
    parametros_origem = {"name":cidade_origem, "count":1}
    resposta_origem = requests.get(url,params=parametros_origem)
    dados_origem = resposta_origem.json()
    #print(dados_origem["results"][0]["latitude"])
    latitude_origem = dados_origem["results"][0]["latitude"]
    longitude_origem = dados_origem["results"][0]["longitude"]
    parametros_destino = {"name":cidade_destino, "count":1}
    resposta_destino = requests.get(url,params=parametros_destino)
    dados_destino = resposta_destino.json()
    #print(dados_destino["results"][0])
    latitude_destino = dados_destino["results"][0]["latitude"]
    longitude_destino = dados_destino["results"][0]["longitude"]
    #print("latitude_origem:", latitude_origem)
    #print("longitude_origem:", longitude_origem)
    #print("latitude_destino:", latitude_destino)
    #print("longitude_destino:", longitude_destino)
    transporte = input("como deseja viajar? aviao, carro ou a pe?").strip().lower()
    if transporte == "carro":
        print("voce optou por viajar de carro. Curta sua viagem com seguranca.")
    elif transporte == "aviao":
        print("voce optou por viajar de aviao. relaxe e aproveite para descansa.")
    elif transporte == "a pe ":
        print("voce optou por viajar a pe, sera um grande desafio.")
    else:
        print("opcao invalida.")

else:
    print("opcao invalida.")





