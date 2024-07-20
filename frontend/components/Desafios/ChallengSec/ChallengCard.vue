<template>
    <div class="challenge-card">
      <div class="challenge-icon">
        <img src="https://cdn3d.iconscout.com/3d/premium/thumb/python-6815592-5602757.png?f=webp" alt="Python Logo">
      </div>
      <div class="challenge-content">
        <h2>Crie um código em python que retorne a soma de 2 parâmetros</h2>
        <div class="challenge-details">
          <div class="flex gap-1 challenge-type">
            <img width="15" height="15" src="https://img.icons8.com/tiny-color/16/00C16A/code.png" alt="code"/>
            <p class="challenge-type">Code</p>
          </div>
          <div class="flex gap-1 challenge-difficulty">
            <img width="25" height="25" src="https://img.icons8.com/windows/20/00C16A/filled-circle.png" alt="filled-circle"/>            <p class="challenge-difficulty">Easy</p>
          </div>
          <div class="flex gap-1 challenge-xp">
            <img width="15" height="15" src="https://img.icons8.com/color/48/prize.png" alt="prize"/>
            <p class="challenge-xp">20 XP</p>
          </div>
        </div>
      </div>
      <div class="challenge-action">
        <button @click="startChallenge">
            <img width="30" height="30" src="https://img.icons8.com/ios-glyphs/30/FFFFFF/circled-play.png" alt="circled-play"/>
        </button>
      </div>
    </div>
  </template>
  
  <script setup>
  const startChallenge = () => {
    console.log("Desafio iniciado!");
  }
  </script>
  
  <style scoped>
  .challenge-card {
    display: flex;
    align-items: center;
    background-color: #0F172A;
    color: white;
    border-radius: 15px;
    height: 100px;
    padding-right: 10px;
    width: 100%;
    
  }

  .challenge-icon{
    border: solid 1px var(--Primary);
    width: 100px;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 10px;
  }

  .challenge-icon img {
    width: 100%;
    height: 100%;
  }
  
  .challenge-content {
    flex: 1;
    padding-left: 15px;
    padding-bottom: 15px;
    padding-top: 15px;
  }
  
  .challenge-content h2 {
    margin: 0;
    font-size: 16px;
    font-weight: 500;
    line-height: 1.5;
  }
  
  .challenge-details {
    display: flex;
    gap: 10px;
    margin-top: 5px;
  }
  
  .challenge-type, .challenge-difficulty, .challenge-xp {
    background-color: #1E293B;
    padding: 2px 5px;
    border-radius: 5px;
  }
  
  .challenge-type {
    display: flex;
    align-items: center;
    gap: 5px;
    
  }
  
  .challenge-difficulty {
    color: #22C55E;
  }
  
  .challenge-xp {
    display: flex;
    align-items: center;
    gap: 5px;
  }
  
  .challenge-action {
    padding-left: 15px;
  }
  
  .challenge-action button {
    background: none;
    border: none;
    color: white;
    font-size: 20px;
    cursor: pointer;
  }
  
  @media screen and (max-width: 500px) {
    .challenge-card{
        height: fit-content;
    }
    .challenge-icon{
        display: none;
    }

    p{
        font-size: 12px;
    }

    .challenge-action{
        display: none;
    }
  }

  </style>
  