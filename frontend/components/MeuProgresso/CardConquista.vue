<template>
    <div class="daily-challenges-card">
      <img class="icon" :src="iconUrl" alt="Daily Challenges Icon" />
      <div class="description">Desafios diários concluídos</div>
      <div class="count">{{ count }}</div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  // Dados do componente
  const iconUrl = ref('https://img.icons8.com/color/48/new-year-calendar.png'); // Substitua pelo caminho real do ícone
  const count = ref(20);
  </script>
  
  <style scoped>
  .daily-challenges-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #0e1320; /* Substitua pela cor de fundo desejada */
    padding: 10px;
    border-radius: 10px;
    width: 165px; /* Ajuste a largura conforme necessário */
    height: fit-content; /* Ajuste a altura conforme necessário */
    color: #fff;
    text-align: center;
  }
  
  .icon {
    width: 40px; /* Ajuste o tamanho do ícone conforme necessário */
    height: 40px;
    margin-bottom: 10px;
  }
  
  .description {
    font-size: 14px;
    margin-bottom: 10px;
  }
  
  .count {
    font-size: 24px;
    color: #0057ff; /* Substitua pela cor desejada para o número */
  }
  </style>
  