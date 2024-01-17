import { createRouter, createWebHistory } from 'vue-router'
import ReceberResposta from '../views/ReceberResposta.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: ReceberResposta
    },

    {
      path: '/card/:id',
      name: 'pesquisa-sugestoes',
      component: () => import('../views/CardSugestaoResposta.vue'),
      props: true,
    },

    {
      path: '/descubra',
      name: 'descubra-sua-area',
      component: () => import('../views/Descubra.vue'),
    }
    
  ]
})

export default router

