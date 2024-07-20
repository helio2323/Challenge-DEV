<template>
    <button class="exit-button">
      <span class="icon">
        <!-- Ícone de saída (você pode usar uma biblioteca de ícones ou um SVG inline) -->
        <img width="25" height="25" src="https://img.icons8.com/sf-black-filled/64/EAB308/exit.png" alt="exit"/>
      </span>
      <span class="text">Sair</span>
    </button>
  </template>
  
  <script setup>
  // Lógica do componente, se necessário
  </script>
  
  <style scoped>
  .exit-button {
    display: flex;
    height: 40px;
    width: 180px;
    align-items: center;
    justify-content: center;
    background-color: none ;
    color: var(--Tertiary);
    border: none;
    padding: 10px 20px;
    border-radius: 30px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s;
    border: solid 1px var(--Tertiary);
    
  }
  
  .exit-button:hover {
    background-color: #2d3748;
  }
  
  .icon {
    margin-right: 10px;
  }
  
  .text {
    font-weight: bold;
  }
  </style>
  