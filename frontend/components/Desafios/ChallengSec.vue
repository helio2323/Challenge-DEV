<template>
    <div class="challeng">
        <section class="challeng-cards">
            <div class="tittle-infos">
                <h3 class="tittle">Inicie agora seu aprendizado</h3>
                <DesafiosChallengSecModalInfos class="phone-infos"/>
            </div>
            <div v-for="(question, index) in filteredQuestions" :key="index" class="cads-ajust">
                <DesafiosChallengSecChallengCard
                    :id_question="question.id"
                    :title="question.title"
                    :subtitle="question.subtitle"
                    :exemplo="question.example"
                    :tipodesafio="question.type_question"
                    :pergunta="question.question"
                    :linguagem="question.id_language"
                    :xpreward="question.xp_reward"
                    :resposta="question.response"
                    :dificuldade="question.dificulty"
                    :srcUrl="imageUrl"
                    :isResponded="question.responded"
                    v-if="question.id_language === languageFilter &&  question.dificulty === dificultyFilter"
                />
            </div>
        </section>
        <DesafiosChallengSecChallengInfos class="challeng-infos" />
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import useQuestions from '@/composables/useQuestions';
import { languageFilter } from '@/api/statGlobal';
import { getResponses } from '@/api/questionTips.js';
import { dificultyFilter } from '@/api/statGlobal';

const { questions, fetchAllQuestions } = useQuestions();
const userResponses = ref<any[]>([]);
const filteredQuestions = ref<any[]>([]);

onMounted(async () => {
    await fetchAllQuestions();
    userResponses.value = await getResponses(); // Obtém as respostas do usuário
    
    
    // Filtra as perguntas marcando se foram respondidas
    filteredQuestions.value = questions.value.map(question => ({
        ...question,
        responded: userResponses.value.some(response => response.question_id === question.id && response.user_id === Number(localStorage.getItem('userid')))
    }));
});

const imageUrl = computed(() => {
    if (languageFilter.value === 2) {
        return 'https://cdn3d.iconscout.com/3d/free/thumb/free-javascript-9294848-7577991.png?f=webp';
    } else if (languageFilter.value === 1) {
        return 'https://cdn3d.iconscout.com/3d/premium/thumb/python-6815592-5602757.png?f=webp';
    } else if(languageFilter.value === 3) {
        return 'https://cdn3d.iconscout.com/3d/free/thumb/free-java-9294874-7578017.png?f=webp'
    } else if (languageFilter.value === 4) {
        return 'https://rust-book.cs.brown.edu/img/ferris/not_desired_behavior.svg'
    }
    return 'https://cdn3d.iconscout.com/3d/free/thumb/free-java-9294874-7578017.png?f=webp'; // ou algum valor padrão
});
</script>

  
  <style scoped>
  .tittle-infos{
      display: flex;
      width: 100%;
      justify-content: space-between;
  }
  
  .challeng {
      display: flex;
      flex-direction: row;
      gap: 40px;
  }
  
  .tittle{
      font-size: 28px;
      font-weight: 500;
  }
  
  .challeng-cards{
      height: 100%;
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: start;
      align-items: start;
      gap: 5px;
  }
  
  .phone-infos{
      display: none;
  }
  
  .cads-ajust{
      display: flex;
      flex-direction: column;
      width: 100%;
  }
  
  @media screen and (max-width: 950px) {
      .challeng {
          display: flex;
          flex-direction: column;
          width: 100%;
          align-items: center;
      }
  
      .challeng-cards{
          width: 100%;
      }
  
      .challeng-infos{
          display: none;
      }
  
      .phone-infos{
          display: flex;
      }   
  
      @media screen and (max-width: 500px) { 
          .tittle {
              font-size: 20px;
          }
      }
  }
  </style>
  