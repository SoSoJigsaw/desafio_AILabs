<template>
    <main>
        <h1>Muitas áreas da sociedade, com seus desafios imensos, estão procurando por inovação.</h1>
        <h3>Qual área mais te interessa?</h3>
        <select v-model="area">
            <option value=null>Escolha uma...</option>
            <option v-for="a in areas" @click.prevent="buscarSugestoes()">{{ a }}</option>
        </select>

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
            area: null,
            areas: [],
            recomendacoes: [],
        }
    },

    mounted() {
        this.getAreas();
    },

    methods: {

        async getAreas() {

            const response = await axios.get('http://127.0.0.1:5000/assuntos');

            this.areas = response.data;

        },

        async buscarSugestoes() {

            const response = await axios.get('http://127.0.0.1:5000/perguntaassunto/' + this.area);

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



      },

    }
</script>

<style>
select {
    width: 100%;
    height: 50px;
    font-size: medium;
    text-align: center;
    background-color: rgba(222, 222, 222, 1);
    border-radius: 5px;
}

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