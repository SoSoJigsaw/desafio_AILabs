# Desafio AI Labs
[![AI Labs]()]

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

# Manual de Uso
Acesse aqui o material completo.

## Funcionalidades


## Utilização da API ChatGPT (GPT-3.5-Turbo)

### 1. Controle de Temperature e Max Tokens
No projeto, foi configurado dois tipos distintos de saída através dos parâmetros temperature e max_tokens. O primeiro perfil atende com respostas mais criativas e tem maior limite de texto, o outro tem um olhar mais analítico e responde de forma mais direta. Ambos atendem ao que se propõem. O perfil criativo é o que tem o primeiro contato com o usuário, respondendo diretamente as suas demandas, enquanto que o outro tem o papel de analisar a sua própria resposta anterior e, assim, propor novos tópicos que sejam relevantes no que foi requisitado e gerando novas dúvidas ao usuário, ao qual tem a opção de pedir um aprofundamento do assunto levantado se o achar relevante. Para fazer isso, dentro da configuração da response, foi colocado os devidos argumentos:
- temperature=1, max_tokens=1000: Essa configuração permite ao ChatGPT elaborar respostas mais criativas, o que vai de encontro com o que o usuário deseja (temperature=1 é o valor mais alto para esse parâmetro), enquanto que max_tokens delimita o número de caracteres utilizadas em uma resposta (sendo em torno de 4000 tokens o limite nesse modelo). Portanto, foi gerado um perfil no qual contribui para o processo criativo do usuário, e que não economiza na descrição.
- temperature=0.1, max_tokens=1000: Esse é o menor valor para o parâmetro temperature, o que faz com que as respostas do ChatGPT sejam mais sucintas e diretas. Apesar do limite de tokens ser o mesmo para os dois, através de outro parâmetro, que é o messages, eu configurei esse perfil para dar respostas curtas, já que não atendem diretamente ao que foi perguntado pelo usuário, mas sim é apenas um acréscimo que pode contribuir para a discussão com o sistema.

### 2. Instruções ao ChatGPT através do messages


### 3. Testagem e base de dados


### 4. Configurações e Chave da API


## Criação de REST API com Flask


## Frontend com Vue.js e Typescript




