from openai import OpenAI
from flask import Flask, jsonify
from sugestoesPesquisa import sugestoes_aleatorio, pesquisa_pelo_id, todos_assuntos, pesquisa_pelo_assunto
import json

app = Flask(__name__)


# Setando API Key
with open("configKey.json") as config_file:
    config = json.load(config_file)

client = OpenAI(api_key=config["openai_api_key"])

messages = [
    {"role": "system", "content": "Você é um assistente treinado para gerar ideias inovadoras para startups. Age de "
                                  "forma simpática e encorajadora em suas respostas, incentivando os usuários nessa "
                                  "jornada. Mesmo que o usuário troque totalmente de foco ou apenas te cumprimente, "
                                  "não deixe de sempre citar algo valioso e forçar a conversa para o seu foco como um "
                                  "assistente criativo. Faça sempre que puder sugestões de temas inovadores, direcione "
                                  "os usuários para o empreendedorismo com paixão, os impulsione e os ajude à criarem "
                                  "suas próprias startups."}
]


@app.route('/resposta/<string:resposta>', methods=['GET'])
def resposta(resposta):

    messages.append({"role": "user", "content": "Responda minha pergunta em até 250 palavras. Não deixe o assunto ser "
                                                "desviado do assunto sobre startups, empreendedorismo e inovaçao!: "
                                                + resposta})

    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages, temperature=1, max_tokens=1000)

    answer = response.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})

    respo = jsonify(answer)
    respo.headers.add("Access-Control-Allow-Origin", "*")
    respo.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
    respo.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")

    return respo

@app.route('/sugestoes/<string:sugestoes>', methods=['GET'])
def sugestoes(sugestoes):

    messages.append({"role": "user", "content": "Sugira de forma sucinta, usando no máximo 70 letras e com ponto final, um "
                                                "tópico novo que seja útil a respeito de startups e inovação, e que"
                                                " tenha conexão com a última coisa que você disse. Explique brevemente "
                                                "a importância do tópico para a área de startups e inovação: "
                                                + sugestoes})

    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages, temperature=0.1, max_tokens=1000)

    answer = response.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})

    respo = jsonify(answer + " Gostaria de saber mais a respeito?")
    respo.headers.add("Access-Control-Allow-Origin", "*")
    respo.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
    respo.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")

    return respo


@app.route('/resposta-sugestao/<string:respostaSugestao>', methods=['GET'])
def respostaSugestao(respostaSugestao):

    respostaSugestao = respostaSugestao[:-34]

    messages.append({"role": "user", "content": "Gostaria de saber mais, em até 250 palavras, sobre: "
                                                + respostaSugestao})

    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages, temperature=1, max_tokens=1000)

    answer = response.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})

    respo = jsonify(answer)
    respo.headers.add("Access-Control-Allow-Origin", "*")
    respo.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
    respo.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")

    return respo

@app.route('/sugestoes-aleatorias', methods=['GET'])
def sugestoesAleatorias():

    listaSugestoes = sugestoes_aleatorio(6)

    respo = jsonify(listaSugestoes)
    respo.headers.add("Access-Control-Allow-Origin", "*")
    respo.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
    respo.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")

    return respo


@app.route('/perguntaid/<int:id>', methods=['GET'])
def perguntaid(id):

    pergunta = pesquisa_pelo_id(id)

    print(pergunta)

    respo = jsonify(pergunta)
    respo.headers.add("Access-Control-Allow-Origin", "*")
    respo.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
    respo.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")

    return respo


@app.route('/assuntos', methods=['GET'])
def assuntos():

    assuntos = todos_assuntos()

    respo = jsonify(assuntos)
    respo.headers.add("Access-Control-Allow-Origin", "*")
    respo.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
    respo.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")

    return respo


@app.route('/perguntaassunto/<string:assunto>', methods=['GET'])
def pergunta_assunto(assunto):

    perguntas = pesquisa_pelo_assunto(assunto)

    respo = jsonify(perguntas)
    respo.headers.add("Access-Control-Allow-Origin", "*")
    respo.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
    respo.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")

    return respo


if __name__ == '__main__':
    app.run(debug=True)
