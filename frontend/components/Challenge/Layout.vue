<template>
  <div class="layout-challenge">
    <div class="button-challenge">
      <ChallengeHeaderButtonSair  />
      <ChallengeHeaderButtonRun  @click="handleClick "/>
      <ChallengeHeaderButtonSubmit @click="handleSubmit" />
    </div>
    <h4 v-if="responseQuestion.response === 'Question incorrect'">{{ responseQuestion.response }}</h4>
    <h5 v-if="responseQuestion.response === 'Question correct'"> {{ responseQuestion.response }}</h5>
    <h6 v-if="responseQuestion.response === 'Question already answered'"> {{ responseQuestion.response }}</h6>
    <main class="main-challenge">
      <section class="question-section">
        <ChallengeQuestion class="question" /> 
      </section>
      <div class="code-sections" >
        <section class="code-section">
          <div class="monaco-ed">
            <div class="type-header-code">
              <p>{{ challengeStar.tipodesafio }}</p>
              <ChallengeQuestionModalQ class="modal"/>
            </div>
            <MonacoEditor
              class="editor"
              :options="{ theme: 'vs-dark', language: 'python' }"
              v-model="value"
              :lang="monacoLanguage"
            />
          </div>
        </section>
        <section class="code-section console">
          <div class="monaco-ed">
            <div class="type-header-code">Console Output</div>
            <div class="console-output">
              <p class="code-out"> <strong>Code Response: </strong> 
              {{ responseQuestion.code_response }}</p>
              <p class="question-out"><strong>Question Response: </strong> {{ responseQuestion.response }}</p>
            </div>
          </div>
        </section>
      </div>
    </main>
  </div>
</template>


<script lang="ts" setup>
const toast = useToast()

import { ref } from 'vue';
import { challengeStar, monacoLanguage, responseQuestion } from '~/api/statGlobal';
import { submitCode, verifyCode } from '~/api/challengTips';

const value = ref<string>(''); // Inicialize a referência como string


const handleClick = async () => {

  toast.add({ title: 'Validando sua resposta', click: handleClick })

  const questionvalues = challengeStar.value;

  const response = await verifyCode(
    questionvalues.tipodesafio,
    questionvalues.id_question,
    value.value,  // Passe o valor como string
    monacoLanguage.value
  );

  console.log(response);

  responseQuestion.value = response

  toast.add({ title: "Validação concluída", click: handleClick })


};

const handleSubmit = async () => {

toast.add({ title: 'Validando sua resposta', click: handleSubmit })

const questionvalues = challengeStar.value;

const response = await submitCode(
  questionvalues.tipodesafio,
  questionvalues.id_question,
  value.value,  // Passe o valor como string
  monacoLanguage.value,
  localStorage.getItem('userid')
);

responseQuestion.value = response

console.log(response);

toast.add({ title: "Validação concluída", click: handleSubmit })

if (response.response === 'Question answered') {
  navigateTo('/desafios');
}

};
</script>



  <style scoped>

  .modal{
    display: none;
  }

  .layout-challenge {
    display: flex;
    min-width: 100%;
    flex-direction: column;
    max-width: fit-content;
    height: 100%;
  }
  
  .button-challenge {
    display: flex;
    flex-direction: row;
    width: 100%;
    align-items: center;
    justify-content: center;
    gap: 20px;
    padding: 10px;
  }
  
  .main-challenge {
    display: flex;
    flex-direction: row;
    max-width: 100%;
    height: 100%;
    gap: 20px;
    padding: 20px;
  }
  
  .question-section {
    display: flex;
    flex-direction: column;
    min-width: 50%;
    height: 100%;
    background-color: var(--BackCover);
    border-radius: 15px;
    padding: 15px;
  }
  
  .code-sections {
    display: flex;
    flex-direction: column;
    min-width: 50%;
    height: 100%;
    gap: 20px;
  }
  
  .code-section {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
    border-radius: 15px;
  }
  
  .monaco-ed {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    gap: 10px;
    background-color: var(--BackCover);
    border-radius: 15px;    
  }
  
  .editor {
    width: 100%;
    height: 100%;
    max-height: 325px;
  }
  
  .type-header-code {
    width: 100%;
    display: flex;
    align-items: center;
    background-color: var(--Gray700);
    border-radius: 10px 10px 0 0;
    padding: 5px 10px;
    color: var(--Primary);
    font-size: 14px;
    font-weight: 500;
    justify-content: space-between
  }

  .console-output {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
    background-color: var(--BackCover);
    border-radius: 15px;
    padding: 15px;
    gap: 20px;
  }

  .console-output strong {
    color: var(--Primary);
  }

  .code-out {
    color: white;
  }

  .question-out {
    color: white;
  }

  h4 {
    color: white;
    width: 100%;
    text-align: center;
    font-size: 20px;
    font-weight: 500;
    background: #FB7185;
  }

  h5 {
    color: white;
    width: 100%;
    text-align: center;
    font-size: 20px;
    font-weight: 500;
    background: #00DC82;
  }

  h6 {
    color: white;
    width: 100%;
    text-align: center;
    font-size: 20px;
    font-weight: 500;
    background: #60A5F9;
  }

  @media screen and (max-width:1150px) {
    
    .modal {
      display: block;
    }

    .main-challenge{
        flex-direction: column;
        width: 100vw;
        padding: 10px;
    }

    .question-section {
        display: none;
    }

    .question-section{
        width: 100%;
        height: fit-content;
        flex-direction: row;
        align-items: center;
        gap: 20px;
        font-size: 20px;
        font-weight: 500;
    }

    .code-sections{
        width: 100%;
        height: fit-content;
    }
    .editor {
        height: 100%;
    }

    .console {
        height: 30%;
    }
  }

  @media screen and (max-width: 600px) {
        
    .button-challenge {
        width: 100%;
        flex-direction: column;
    }
  }
  </style>
  