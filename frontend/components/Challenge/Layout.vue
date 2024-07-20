<template>
    <div class="layout-challenge">
      <div class="button-challenge">
        <ChallengeHeaderButtonSair />
        <ChallengeHeaderButtonRun />
        <ChallengeHeaderButtonSubmit />
      </div>
      <main class="main-challenge">
        <section class="question-section">
        <ChallengeQuestion class="question" /> 
        </section>
        <div class="code-sections">
          <section class="code-section">
            <div class="monaco-ed">
              <div class="type-header-code">
                <p>Code</p>
                <ChallengeQuestionModalQ class="modal"/>
              </div>
              <MonacoEditor
                class="editor"
                :options="{ theme: 'vs-dark' }"
                v-model="value"
                lang="python" 
              />
            </div>
          </section>
          <section class="code-section console">
            <div class="monaco-ed">
              <div class="type-header-code">Console Output</div>
              <div class="console-output">
                <h1>Consle Output</h1>
              </div>
            </div>
          </section>
        </div>
      </main>
    </div>
  </template>
  
  <script lang="ts" setup>
  const value = ref('')
  </script>
  
  <style scoped>

  .modal{
    display: none;
  }

  .layout-challenge {
    display: flex;
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
    width: 100%;
    height: 100%;
    gap: 20px;
    padding: 20px;
  }
  
  .question-section {
    display: flex;
    flex-direction: column;
    width: 50%;
    height: 100%;
    background-color: var(--BackCover);
    border-radius: 15px;
    padding: 15px;
  }
  
  .code-sections {
    display: flex;
    flex-direction: column;
    width: 50%;
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
  