<template>
  <div :style="{ border: isResponded ? '1px solid #00C16A' : '1px none #fff' }" class="challenge-card">
    <div class="challenge-icon">
      <img :src="srcUrl" alt="Challenge Icon">
    </div>
    <div class="challenge-content">
      <h2 >{{ title }}</h2>
      <div class="challenge-details">
        <div class="flex gap-1 challenge-type">
          <img width="15" height="15" src="https://img.icons8.com/tiny-color/16/00C16A/code.png" alt="code"/>
          <p class="challenge-type">{{ tipodesafio }}</p>
        </div>
        <div class="flex gap-1 challenge-difficulty">
          <p class="challenge-difficulty">{{ dificuldade }}</p>
        </div>
        <div class="flex gap-1 challenge-xp">
          <img width="15" height="15" src="https://img.icons8.com/color/48/prize.png" alt="prize"/>
          <p class="challenge-xp">{{ xpreward }} XP</p>
        </div>
      </div>
    </div>
    <div class="challenge-action">
      <button @click="startChallenge">
        <img width="30" height="30" src="https://img.icons8.com/ios-glyphs/30/FFFFFF/circled-play.png" alt="start"/>
      </button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  id_question: Number,
  title: String,
  subtitle: String,
  exemplo: String,
  tipodesafio: String,
  pergunta: String,
  linguagem: String,
  xpreward: String,
  resposta: String,
  dificuldade: String,
  srcUrl: {
    type: String,
    default: ''
  },
  isResponded: Boolean // Adicione a propriedade isResponded
});

import { challengeStar, monacoLanguage } from "@/api/statGlobal";
import { getLanguages } from '~/api/languageTips';

const startChallenge = async () => {
  const row = {
    id_question: props.id_question,
    title: props.title,
    subtitle: props.subtitle,
    exemplo: props.exemplo,
    tipodesafio: props.tipodesafio,
    pergunta: props.pergunta,
    linguagem: props.linguagem,
    xpreward: props.xpreward,
    resposta: props.resposta,
    dificuldade: props.dificuldade
  };

  challengeStar.value = row;
  const selectedLang = await getLanguages(undefined, row.linguagem);
  let lowerCaselang = selectedLang.name.toLowerCase();
  monacoLanguage.value = lowerCaselang;

  navigateTo('/questao');
};
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

.challenge-icon {
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
  font-size: 20px;
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
  color: white;
}

.challenge-xp {
  display: flex;
  align-items: center;
  gap: 5px;
  color: var(--Secondary);
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
  .challenge-card {
    height: fit-content;
  }
  .challenge-icon {
    display: none;
  }

  p {
    font-size: 12px;
  }

  .challenge-action {
    display: none;
  }
}
</style>
