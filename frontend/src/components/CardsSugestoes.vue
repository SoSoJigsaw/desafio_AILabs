<template>
    <main>
        <h1>Sem ideias? Veja algumas sugestões...</h1>
        <div class="container-card">
            <div class="card" v-for="r in recomendacoes" :key="r.id" @click="clickPesquisa(r.id)">
                <h2>{{ r.assunto }}</h2>
                <p>"{{ r.pesquisa }}"</p>
            </div>
        </div>
    </main>    
</template>

<script lang="ts">
import axios from 'axios'

export default {
    data() {
        return {
            recomendacoes: [],
        }
    },

    mounted() {

        this.recomendaAlea();
        
    },

    methods: {

        async recomendaAlea() {

            const response = await axios.get('http://127.0.0.1:5000/sugestoes-aleatorias');

            this.recomendacoes = response.data.map((item: String) => ({
                id: item.id,
                assunto: item.assunto,
                pesquisa: item.pesquisa
            }));

        },

        clickPesquisa(id: string) {

            this.$router.push({
                name: 'pesquisa-sugestoes',
                params: {
                    id: id
                }
            });

        },

    }
}
</script>

<style>
.container-card {
    display: grid;
    grid-template-columns: 50% 50%;
    grid-gap: 10px;
    padding-top: 10px;
    padding-bottom: 20px;
}

.card {
    background-color: rgba(222, 222, 222, 0.3);
    border-radius: 5px;
    padding: 15px;
    text-align: center;
    color: var(--azul-principal);
    cursor: pointer;
}

.card:hover {
    background-color: rgba(222, 222, 222, 0.5);
}
</style>