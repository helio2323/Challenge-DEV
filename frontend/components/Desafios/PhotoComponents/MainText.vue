<template>
    <div>
      <h2 class="">
        AVANCE AGORA MESMO NOS SEUS ESTUDOS <strong>{{ languageText }}</strong>
      </h2>
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue';
  import { languageFilter as globalLanguageFilter } from '@/api/statGlobal';
  
  // Corrigir a sintaxe do if e renomear a variável para evitar conflito
  const languageText = computed(() => {
    if (globalLanguageFilter.value === 1) {
      return 'PYTHON';
    } else if (globalLanguageFilter.value === 2) {
      return 'JAVASCRIPT';
    } else if (globalLanguageFilter.value === 3) {
        return "JAVA"       
    } else if (globalLanguageFilter.value === 4) {
        return "RUST"
    }
    return 'Language Not Set'; // Valor padrão se nenhum dos casos acima for verdadeiro
  });
  </script>
  
  <style scoped>
  h2 {
    color: white;
    font-size: 28px;
    font-weight: bold;
    text-align: start;
    width: 50%;
  }
  
  @media screen and (max-width: 950px) {
    h2 {
      width: 100%;
    }
  }
  
  strong {
    color: var(--Primary);
  }
  </style>
  