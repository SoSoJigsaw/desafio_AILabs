<template>
    <main>

        <CardsSugestoes v-if="!verificarClasseExiste('pergunta')" />

        <div v-for="(d, index) in data" :key="index">
            <div class="pergunta" v-if="d.pergunta">
                <p>{{ d.pergunta }}</p>
            </div>
            <div class="resposta" v-if="d.resposta"> 
              <p>{{ d.resposta }}</p>
            </div>
            <div class="sugestao" v-if="d.sugestao">
              <p>{{ d.sugestao }}</p>
                <button type="submit" class="botao-sugestao" @click.prevent="responderSugestao(d.sugestao)">Adoraria!</button>
            </div>
        </div>
        
        <Erro v-if="erro" />

        <div>
        <img v-if="loading" src="../assets/loading.gif" alt="Carregando...">     
        <form v-else @submit.prevent="receberResposta(question)">
            <input type="text" v-model="question" placeholder="Digite aqui...">
            <button type="submit"><i class="fa-sharp fa-solid fa-paper-plane"></i></button>
        </form>
        </div>
        
      </main>
    
    
</template>

<script lang="ts">
import axios from 'axios'
import Erro from '../components/erro.vue';
import CardsSugestoes from '@/components/CardsSugestoes.vue';

export default {
    data() {
        return {
            respostas: [],
            question: '',
            sugestoes: [],
            perguntas: [],
            data: [],
            loading: false,
            erro: false,
        };
    },

    methods: {
        async receberResposta(question) {

          const source = axios.CancelToken.source();

            if (question != '') {

                this.erro = false;

                this.perguntas.push(question);
                this.data.push({ pergunta: question});

                this.loading = true;

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

        async responderSugestao(sugestao) {

          this.erro = false;

          const source = axios.CancelToken.source();

            this.data.push({ pergunta: 'Gostaria de saber mais!'});

            this.loading = true;

            try {

              const response = await axios.get('http://127.0.0.1:5000/resposta-sugestao/' + sugestao, {
              cancelToken: source.token,
              });

                this.respostas.push(response.data);

                this.data.push({ resposta: response.data });

                const suges = this.respostas.length - 1;

                const res = await axios.get('http://127.0.0.1:5000/sugestoes/' + suges);
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

          },

          verificarClasseExiste(nomeClasse) {
      
            const elemento = document.querySelector('.pergunta');
    
            return elemento && elemento.classList.contains(nomeClasse);
          },  

    },

    components: {
      Erro, CardsSugestoes,
    },    
    
}
</script>

<style>
img {
  margin-left: 50px;
}

form {
  display: flex;
  flex-wrap: nowrap;
  flex-flow: row;
}

input {
  border-radius: 5px;
  border-color: transparent;
  background-color: #2c3e50;
  opacity: 0.8;
  width: 100%;
  line-height: 2;
  font-size: larger;
  color: #fff;
  margin-left: 10px;
}

button {
  width: 5%;
  background-color: transparent;
  border-color: transparent;
}

.item {
  margin-top: 2rem;
  display: flex;
}

.details {
  flex: 1;
  margin-left: 1rem;
}

h3 {
  font-size: 1.2rem;
  font-weight: 500;
  margin-bottom: 0.4rem;
  color: var(--color-heading);
}

@media (min-width: 1024px) {
  .item {
    margin-top: 0;
    padding: 0.4rem 0 1rem calc(var(--section-gap) / 2);
  }

  .item:before {
    content: ' ';
    border-left: 1px solid var(--color-border);
    position: absolute;
    left: 0;
    bottom: calc(50% + 25px);
    height: calc(50% - 25px);
  }

  .item:after {
    content: ' ';
    border-left: 1px solid var(--color-border);
    position: absolute;
    left: 0;
    top: calc(50% + 25px);
    height: calc(50% - 25px);
  }

  .item:first-of-type:before {
    display: none;
  }

  .item:last-of-type:after {
    display: none;
  }
}

.pergunta {
    text-align: end;
    background-color: rgba(222, 222, 222, 0.1);
    padding: 15px;
    margin: 7px;
    border-radius: 5px;
    font-size: larger;
}

.resposta {
    text-align: start;
    background-color: hsla(160, 100%, 37%, 0.8);;
    padding: 15px;
    margin: 7px;
    border-radius: 5px;
    font-size: larger;
}

.sugestao {
    text-align: start;
    background-color: rgba(235, 235, 235, 0.5);
    padding: 15px;
    margin: 7px;
    border-radius: 5px;
    font-size: larger;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}

.botao-sugestao {
    background-color: #2c3e50;
    padding: 5px;
    text-align: center;
    width: 25%;
    margin: 10px;
    border-radius: 5px;
    opacity: 0.8;
    display: inline-block;
    vertical-align: middle;
    color: #fff;
    font-weight: 700;
    font-size: medium;
    font-family: Arial, Helvetica, sans-serif;
    cursor: pointer;
}

.botao-sugestao:hover {
    opacity: 1;
}

button i {
  color: #fff;
  font-size: 30px;
  cursor: pointer;
  opacity: 0.9;
}

button i:hover {
  background-color: #fff;
  color: #2c3e50;
  opacity: 0.8;
  padding: 5px;
  border-radius: 5px;
}
</style>