# Desafio AI Labs
[![AI Labs]()]

## Menu:

## Sobre o desafio: 
Desenvolver uma aplicação que emprega a API do ChatGPT para gerar conceitos inovadores de startups com base nos inputs dos usuários. A ferramenta deve propor ideias de startups conforme os inputs dos usuários.

## Requisitos:
- Integração com a API do ChatGPT (sem divulgar a chave OpenAI)

## Solução Proposta: 
Criação de um software web baseado em REST API, com interface gráfica e de fácil utilização pelos usuários. Buscou-se modelar a API do ChatGPT ao máximo para aumentar a relevância de suas respostas referentes ao desejado, utilizando de todos os parâmetros úteis a esse propósito. 
[![Home Software]()]

## Tecnologias utilizadas:
- <b>Flask (Python):</b> micro framework ideal para a criação de REST APIs. A API foi consumida neste ambiente, passando os dados relevantes ao frontend através de requisições, em suma, no método "GET". Além disso, permitiu a configuração e modelagem dos comportamentos do ChatGPT, assim como teve papel importante em armazenar uma lista de dicionários que é parte importante do projeto, pois que foram usados para dar aos usuários a possibilidade de terem "sugestões" de input, o que visa melhorar a sua experiência utilizando o software.
- <b>Vue.js (Typescript):</b> framework onde o projeto frontend foi desenvolvido, em formato singlepage, proporcionando uma interface ao usuário agradável e rápida.
- <b>GPT-3.5-Turbo:</b> modelo escolhido no catálogo da OpenAI para utilizar o API do ChatGPT

## Manual de Uso
Acesse aqui o material completo.

## Funcionalidades
- Conversa interativa com o ChatGPT-3.5 modificado para atender aos usuários que buscam ideias em inovação, empreendedorismo e startups
- Dois perfis diferentes de resposta: um que prevalece a criatividade, e o outro mais analítico
- Mais de 150 sugestões de perguntas sobre startups em diversas áreas de interesse, geradas com este mesmo modelo desenvolvido no projeto
- Interface intuitiva

## Utilização da API ChatGPT (GPT-3.5-Turbo)

### 1. Controle de Temperature e Max Tokens
No projeto, foi configurado dois tipos distintos de saída através dos parâmetros `temperature` e `max_tokens`. O primeiro perfil atende com respostas mais criativas e tem maior limite de texto, o outro tem um olhar mais analítico e responde de forma mais direta. Ambos atendem ao que se propõem. O perfil criativo é o que tem o primeiro contato com o usuário, respondendo diretamente as suas demandas, enquanto que o outro tem o papel de analisar a sua própria resposta anterior e, assim, propor novos tópicos que sejam relevantes no que foi requisitado e gerando novas dúvidas ao usuário, ao qual tem a opção de pedir um aprofundamento do assunto levantado se o achar relevante. Para fazer isso, dentro da configuração da `response`, foi colocado os devidos argumentos:
- `temperature=1`, `max_tokens=1000`: Essa configuração permite ao ChatGPT elaborar respostas mais criativas, o que vai de encontro com o que o usuário deseja (`temperature=1` é o valor mais alto para esse parâmetro), enquanto que `max_tokens` delimita o número de caracteres utilizadas em uma resposta (sendo em torno de 4000 tokens o limite nesse modelo). Portanto, foi gerado um perfil no qual contribui para o processo criativo do usuário, e que não economiza na descrição.
- `temperature=0.1`, `max_tokens=1000`: Esse é o menor valor para o parâmetro temperature, o que faz com que as respostas do ChatGPT sejam mais sucintas e diretas. Apesar do limite de tokens ser o mesmo para os dois, através de outro parâmetro, que é o messages, foi configurado para que esse perfil para dê respostas curtas, já que não atendem diretamente ao que foi perguntado pelo usuário, mas sim é apenas um acréscimo que pode contribuir para a discussão e trazer insights.

### 2. Instruções ao ChatGPT através do messages
O parâmetro `messages` na API do ChatGPT é usado para fornecer o histórico da conversa para contextualizar a geração da resposta do modelo. Ele aceita uma lista de objetos, onde cada objeto representa uma mensagem na conversa. É por esse parâmetro onde o input do usuário é enviado à API. No entanto, sua configuração não se limita ao nível do usuário, mas sim também ao do próprio sistema, já que em sua estrutura de objeto há o parâmetro role, o que permite mandar instruções diretamente ao sistema e orientar de quê forma é desejado que ele atue. Dessa forma, foi possível tornar as respostas mais previsíveis, mesmo em testes realizados onde se tentava fugir do assunto no qual ele foi instruído. Sendo assim, dentro do Flask criei uma orientação direta ao `role` `system`:
```python
messages = [
    {"role": "system", "content": "Você é um assistente treinado para gerar ideias inovadoras para startups. Age de "
                                  "forma simpática e encorajadora em suas respostas, incentivando os usuários nessa "
                                  "jornada. Mesmo que o usuário troque totalmente de foco ou apenas te cumprimente, "
                                  "não deixe de sempre citar algo valioso e forçar a conversa para o seu foco como um "
                                  "assistente criativo. Faça sempre que puder sugestões de temas inovadores, direcione "
                                  "os usuários para o empreendedorismo com paixão, os impulsione e os ajude à criarem "
                                  "suas próprias startups."}
```
Com essas instruções gerais, a partir do primeiro input do usuário, as respostas já se mostravam satisfatórias.
Com o input do usuário e com a utilização do Flask, foi possível também personalizar as perguntas de forma que a devolutiva fosse mais eficiente:
```python
messages.append({"role": "user", "content": "Sugira de forma sucinta, usando no máximo 70 letras e com ponto final, um "
                                                "tópico novo que seja útil a respeito de startups e inovação, e que"
                                                " tenha conexão com a última coisa que você disse. Explique brevemente "
                                                "a importância do tópico para a área de startups e inovação: "
                                                + sugestoes})
```
O uso do messages foi o primordial para chegar aos resultados esperados, acima do `temperature` e do `max_tokens`, e assim se mostra a melhor maneira de programar as respostas da ferramenta.

### 3. Testagem e base de dados
Foram realizadas cerca de 250 `requests` à API, com diversos testes ao nível das respostas. Dentro desses testes, assumindo um papel de alguém que deseja abrir uma startup, o sistema foi capaz de me dar diversas ideais de aplicação, e cerca de 150 delas foram armazenadas em uma lista de dicionários em um arquivo Python. Esses dados se tornaram relevantes para uma funcionalidade do projeto, que é o de sugerir perguntas pertinentes aos usuários. Portanto, essa base de dados que foi criada a partir de testes acabou se tornando uma utilidade ao projeto, que pode ajudar um usuário em seu processo criativo. Além disso, todas as perguntas foram categorizadas, e dentro do software é possível acessá-las e usá-las como input.
```python
        {'id': 7, 'pesquisa': 'Estou interessado em uma ideia de startup relacionada à inteligência artificial.', 'assunto': 'Inteligência Artificial'},
        {'id': 8, 'pesquisa': 'Uma startup de IA inovadora pode focar em...', 'assunto': 'Inteligência Artificial'},
        {'id': 9, 'pesquisa': 'Quero uma ideia de startup que envolva realidade aumentada.', 'assunto': 'Realidade Aumentada'},
        {'id': 10, 'pesquisa': 'Uma startup de realidade aumentada pode criar...', 'assunto': 'Realidade Aumentada'},
        {'id': 11, 'pesquisa': 'Estou buscando uma ideia de startup para melhorar a educação online.', 'assunto': 'Educação'},
```

### 4. Configurações e Chave da API
```python
response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages, temperature=1, max_tokens=1000)
answer = response.choices[0].message.content
```
Para realizar a chamada à API GPT-3.5-Turbo, eu utilizei a biblioteca `OpenAI`. Com a chave (armazenada na variável `client`), eu dava chamada à função `create` que é a responsável por fazer a solicitação à API. A variável `response` armazena a resposta, e em `choices[0]` eu defino que iria extrair apenas a primeira escolha feita pelo modelo. Todas as requisições que fiz à API seguiram esse modelo básico.

```python
with open("configKey.json") as config_file:
    config = json.load(config_file)

client = OpenAI(api_key=config["openai_api_key"])
```
Com relação à chave, por questões de segurança, a mesma foi armazenada em um arquivo `.json` configurado no `.gitignore`. A partir da biblioteca `json`, eu extraio a senha para uso sem torná-la visível.

## Criação de REST API com Flask
O projeto no Flask seguiu uma estrutura simples de `routes`, cada um com uma função específica envolvendo o envio dos dados da API ao front-end. Foi dentro desses endpoints que a configuração do funcionamento do ChatGPT foi realizado, na medida da necessidade de cada caso. Pelo fato do projeto de backend e frontend serem separados, houve a necessidade também de configurar os `headers` das requisições por conta do `CORS`.
```python
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
```
Além dos endpoints criados apenas para comunicação entre o backend e o frontend, foi criado também um arquivo `.py` para armazenar as sugestões de pesquisa, e também para manipular esses dados através de métodos, que foram utilizados na lógica dos endpoints dos `routes` do Flask.
```python
def sugestoes_aleatorio(quantidade):

    return random.sample(sugestoes, quantidade)

def pesquisa_pelo_id(id):

    for item in sugestoes:
        if item['id'] == id:
            return item['pesquisa']
    return None
```

## Frontend com Vue.js e Typescript
Foi criado um projeto singlepage que conta com poucos `components` e `views`, tendo apenas três `routes`. As requisições ao backend, para receber os dados da API, foram feitos através da biblioteca `axios` de forma assíncrona (`async`). A partir daí, finalmente, os dados podiam serem exibidos na interface, assim como a interação do usuário com o sistema.
```typescript
 async receberResposta(question) {

                try {
                  const response = await axios.get('http://127.0.0.1:5000/resposta/' + question, {
                  cancelToken: source.token,
                });

                  this.respostas.push(response.data);
                  this.question = '';

                  this.data.push({ resposta: response.data });

                  const suges = this.respostas.length - 1;

                  const res = await axios.get('http://127.0.0.1:5000/sugestoes/' + suges, {
                    cancelToken: source.token,
                  });
                  
                  this.sugestoes.push(res.data);

                  this.data.push({ sugestao: res.data });
                
                } catch (error) {

                  this.erro = true;

                  if (axios.isCancel(error)) {
                    console.log('Requisição cancelada:', error.message);
                  } else {
                    console.error('Erro na requisição:', error.message);
                  }
                }

                this.loading = false;

              }
                
            },
```



