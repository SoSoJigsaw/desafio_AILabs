# Manual de Uso 📘

## Menu:
- [Preparando o Ambiente](#Preparando-o-Ambiente)
- [Usando o Software](#Usando-o-Software)

## Preparando o Ambiente

### 1. Clonando o Repositório
- Acesse a página do repositório
- Clique no botão "Code" e copie o URL exibido
- No Terminal ou Bash, navegue até o diretório que deseja clonar o repositório
- Execute o comando ```git clone <URL>```
- O Git começará a baixar os arquivos do repositório. Aguarde até que o processo seja concluído.


### 2. Flask
- Se não tiver instalado, instale a versão mais recente do Python
- Através do gerenciador de pacotes do Python (`pip`), instale a biblioteca Flask ```pip install flask```. Isso instalará o Flask e suas dependências.
- Configuração do ambiente virtual: é o ideal para isolar as dependências do projeto. No diretório do projeto, execute no terminal:
  ```
  cd seu-projeto
  python -m venv venv
  ```
- Ative o ambiente virtual:
  - Windows:
     ```
    venv\Scripts\activate
     ```
  - No macOS/Linux:
     ```
    source venv/bin/activate
    ```
- Dependências do projeto: o projeto apenas utiliza funções nativas python e o Flask. Portanto, não tem com que se preocupar sobre dependências
- Execução do aplicativo Flask:
    ```
  python main.py
    ```
    
### 3. Vue.js
- Instale primariamente o `Node.js` e gerenciador de pacotes `npm`
- Instale as dependências do projeto:
  ```
  npm install
  ```
- Instale o Vue CLI globalmente:
  ```
  npm install -g @vue/cli
  ```
- Para executar o projeto, utilize:
    ```
    npm run dev
    ```

### ATENÇÃO: Para o uso da aplicação, é necessário que tanto o projeto do `Flask` quanto o projeto do `Vue.js` estejam sendo executados ao mesmo tempo. 

    
## Usando o Software
![Home Software](https://github.com/SoSoJigsaw/desafio_AILabs/blob/main/img/view-home.gif)

### 1. Usar o chat
O usuário pode usar o input a baixo para realizar suas consultas com o ChatGPT. A opção de chat livre, onde o input é realizado diretamente pelo usuário, se necontra na página inicial do software (a primeira que aparece assim que acessa). Na medida em que a conversa com o sistema progride, o usuário pode continuar enviando suas perguntas através desse input.

![chat](https://github.com/SoSoJigsaw/desafio_AILabs/blob/main/img/Screenshot%202024-01-18%20104656.png)

Toda pergunta realizada pelo usuário resultará em duas respostas do ChatGPT, cada uma com um perfil diferente de resposta. A resposta com fundo verde, é a que responde diretamente ao usuário, enquanto que a resposta marrom, é basicamente uma análise do que foi respondido anteriormente para buscar algum tema em destaque que tenha correlação com o contexto da conversa. A partir daí, o usuário tem a opção de pedir mais informações a respeito do que é falado na resposta de fundo marrom, ao clicar em um botão para isso, ou se não tiver relevância para ele, ele pode continuar a conversa atual.

![resposta](https://github.com/SoSoJigsaw/desafio_AILabs/blob/main/img/Screenshot%202024-01-18%20104853.png)

### 2. Selecionar uma sugestão
As sugestões são perguntas já pré-criadas (através deste mesmo modelo usado no projeto, durante a fase de testes) que possuem grande relevância em temáticas de startups, como tecnologia, empreendedorismo e inovação. Na página inicial, aparecerá aleatóriamente seis opções de sugestões (há mais de 150 sugestões, mas na página principal aparece apenas seis aleatoriamente, ou seja, toda vez que carregar a página, as sugestões mudarão). Caso o usuário se identifique e tenha interesse em utilizar alguma dessas sugestões, ele apenas precisa clicar em seu card que automaticamente se torna um input do usuário, e assim se inicia a conversa com o ChatGPT utilizando a mesma regra de quando se utiliza o chat de forma livre (com resposta em verde, que são mais criativas e longas, e mensagens em marrom, que não mais sucintas e faz proposições de tópicos relevantes).

![cards](https://github.com/SoSoJigsaw/desafio_AILabs/blob/main/img/Screenshot%202024-01-18%20104706.png)

### 3. Sugestões por área
Na seção (Descubra sua área!) da aplicação, o usuário tem a oportunidade de ver todos os mais de 150 sugestões de pesquisa separadas por área de interesse. Há um pequeno formulário para selecionar uma das áreas que tem interesse, e assim que a seleciona, aparece todas as sugestões cadastradas para aquela área. É uma forma de inspirar os usuários e ajudá-los a encontrar soluções novas para os seus objetivos.

![area](https://github.com/SoSoJigsaw/desafio_AILabs/blob/main/img/Screenshot%202024-01-18%20104738.png)
