
#importar as bibliotecas
import requests
from dotenv import load_dotenv
load_dotenv()
from geopy.distance import geodesic
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
    url_geocoding = "https://geocoding-api.open-meteo.com/v1/search"#endereco da api que estamos cosultando
    parametros = {"name":cidade,"count":1} # parametros informacoes que mandamos para a api para informar oque buscamos.
    resposta = requests.get(url_geocoding,params=parametros)#pedimos o acesso a api e guardamos o resultado
    dados = resposta.json()# converte a resposta jsom em python como listas e dicionarios
    #print(dados)
    local = dados["results"][0] #acessando a chave results de um dicionario, o indice 0 indica qual elemento da lista queremos acessar. 
    codigo_pais = local["country_code"] #acessamos a chave country_cody do dicionario local onde esta informacoes do codigo do pais 
    #jprint("country_code:", local["country_code"])
    print("=========INFORMACOES DA CIDADE=========")

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
    #print("latidude:", local["latitude"])
    #print(local)
    #print("longitide:", local["longitude"])
    url_clima = "https://api.open-meteo.com/v1/forecast"
    params_clima = {
    "latitude": lat, 
    "longitude":lon,
    "current": "temperature_2m"
    }
    parametros_horas = {"timezone":fuso_horario}
    url_hora = "https://timeapi.io/api/v1/time/current/zone"
    resposta = requests.get(url_hora,params=parametros_horas)
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
    local_destino = dados_destino["results"][0]
    codigo_pais_destino = local_destino["country_code"]
    latitude_destino = dados_destino["results"][0]["latitude"]
    longitude_destino = dados_destino["results"][0]["longitude"]   
    print("=========INFORMACOES DA CIDADE=========") 
    print(f"cidade de destino: {local_destino["name"]}")
    #print(local_destino.keys())
    fuso_destino = local_destino['timezone']
    print(fuso_destino)
    parametros_horas_destino = {"timezone":fuso_destino}
    url_hora_destino = "https://timeapi.io/api/v1/time/current/zone"
    respota_hora_destino = requests.get(url_hora_destino,params=parametros_horas_destino)
    dados_horas_destino = respota_hora_destino.json()
    print("Hora local do desstino:",dados_horas_destino["time"][:5])
    url_clima_destino = "https://api.open-meteo.com/v1/forecast"
    url_clima = "https://api.open-meteo.com/v1/forecast"
    params_clima_destino = {
        "latitude": latitude_destino,
        "longitude":longitude_destino,
        "current": "temperature_2m"
    }
    resposta_clima_destino = requests.get(url_clima_destino,params=params_clima_destino)
    dados_clima_destino = resposta_clima_destino.json()
    temperatura_destino = dados_clima_destino["current"]["temperature_2m"]
    print("temperature", temperatura_destino, "graus c")
    url_moeda_destino = "https://countries.dev/alpha/" + codigo_pais_destino
    resposta_moeda_destino = requests.get(url_moeda_destino)
    dados_moeda_destino = resposta_moeda_destino.json()
   #print(dados_moeda_destino.keys())
    #print(dados_moeda_destino["currencies"])
    moeda_destino = dados_moeda_destino["currencies"][0]
    simbolo_moeda_destino = moeda_destino["symbol"]
    nome_moeda_destino = moeda_destino["name"]
    print(f"moeda local: {nome_moeda_destino} { simbolo_moeda_destino}")


    #print(dados_destino["results"][0])
   
    #print("latitude_origem:", latitude_origem)
    #print("longitude_origem:", longitude_origem)
    #print("latitude_destino:", latitude_destino)
    #print("longitude_destino:", longitude_destino)
    origem_cordenadas = (latitude_origem,longitude_origem)
    destino_cordenadas = (latitude_destino,longitude_destino)
    print("=========INFORMACOES DA VIAGEM=========")
    distancia = geodesic(origem_cordenadas, destino_cordenadas)
    distancia_km = distancia.kilometers
    print(f"distancia da viajem: {distancia_km:.2f} km")
    distancia_mlh = distancia.miles
    print(f"distancia da viagem: {distancia_mlh:.2f} mille")
    tempo_voo = distancia_km / 850
    horas_de_voo = int(tempo_voo)
    minutos_de_voo =round((tempo_voo-horas_de_voo)*60)
    if minutos_de_voo == 60:
        horas_de_voo = horas_de_voo +1
        minutos_de_voo = 0
    print(f"tempo estimado de voo:{horas_de_voo} horas e {minutos_de_voo} minutos")
else:
    print("opcao invalida.")





