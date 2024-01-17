<script lang="ts">
import { RouterLink, RouterView } from 'vue-router'

export default {
  data() {
    return {
      headerBaixo: false,
      headerCima: false,
      position: document.documentElement.clientHeight || window.innerHeight,
    };
  },
  mounted() {
    this.verificarPosicao();

    setInterval(() => {
      this.verificarPosicao();
    }, 100);

    window.addEventListener('scroll', this.verificarPosicao);
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.verificarPosicao);
  },
  methods: {
    verificarPosicao() {

      this.position = (document.documentElement.clientHeight || window.innerHeight) + window.scrollY;

      const scrollUnder = window.scrollY;

      if (window.scrollY > 0) {

        this.headerCima = false;
        this.headerBaixo = scrollUnder > 0;

        this.$refs.header.style.transform = `translateY(${scrollUnder}px)`;
      
      } else {
        this.headerBaixo = false;
        this.headerCima = true;
      }
    },
  },
};
</script>

<template>
  <header :class="{ 'fixo': headerBaixo && !headerCima, 'inicial': headerCima && !headerBaixo }" 
  :style="headerBaixo && !headerCima ? { 'margin-top': 'calc(' + position + 'px - 105%)' } : {}">

    <div class="wrapper">
      <img alt="Vue logo" class="logo" src="@/assets/logo.png"/>
      <h1 class="green">Bem vindo Empreendedor! :)</h1>
      <h3>
        Em busca de uma ideia inovadora para sua startup? Podemos ajudar!
        Utilize a nossa ferramenta ao lado para lhe ajudar em seu processo criativo!
      </h3>
      <h2>Através das informações fornecidas por você, respostas relevantes surgirão para te ajudar à realizar seus objetivos!
        O assistente também irá acrescentar perguntas pertinentes para continuar lhe ajudando.
      </h2>

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/descubra">Descubra sua área!</RouterLink>
      </nav>

    </div>

    

  </header>

  <RouterView />
</template>

<style scoped>
@import "./assets/base.css";

header {
  line-height: 1.5;
  max-height: 100vh;
  position: initial;
  text-align: center;
  transition: transform 2s linear;
}

.fixo {
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  transition: 2s linear;
  transform: translateY(0); 
  transition-delay: 0.5s;
}

.inicial {
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  margin-top: calc(100vh - 99.5vh); 
  transition: 2s linear;
  transform: translateY(0); 
  transition-delay: 0.5s;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:hover {
  color: hsla(160, 100%, 37%, 0.5);
}

nav a:first-of-type {
  border: 0;
}

h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
  padding-top: 15px;
}

h3 {
  padding-top: 5px;
  font-size: 1.2rem;
}

h2 {
  padding-top: 20px;
  text-align: center;
  opacity: 0.8;
  font-size: 1rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
