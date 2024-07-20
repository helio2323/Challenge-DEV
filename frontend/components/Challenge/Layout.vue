<template>
    <div class="layout-challenge">
        <div class="button-challenge">
           <ChallengeHeaderButtonSair />
           <ChallengeHeaderButtonRun />
           <ChallengeHeaderButtonSubmit />
        </div>
        <main class="main-challenge">
            
            <section class="question-section">
                <ChallengeQuestion />  
            </section>
                
            <div class="code-sections">
                <section class="code-section">
                    <div class="monaco-ed">
                        <MonacoEditor
                        class="editor"
                        :options="{ theme: 'vs-dark' }" 
                        v-model="value" 
                        lang="python" />

                    </div>
                </section>
                <section class="code-section">
                    <div class="monaco-ed">
                        <MonacoEditor
                        class="editor"
                        :options="{ theme: 'vs-dark' }" 
                        v-model="value" 
                        lang="typescript" />

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

.layout-challenge{
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
}

.button-challenge{
    display: flex;
    flex-direction: row;
    width: 100%;
    align-items: center;
    justify-content: center;
    gap: 20px;
}

.main-challenge{
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 100%;
    gap: 20px;
    padding: 20px;
}

.question-section{
    display: flex;
    flex-direction: column;
    width: 50%;
    height: 100%;
    background-color: var(--BackCover);
    border-radius: 15px;
    padding: 15px;
}

.code-sections{
    display: flex;
    flex-direction: column;
    width: 50%;
    height: 100%;
}

.code-section {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
    border-radius: 15px;
}

.monaco-ed{
    width: 100%;
    height: 100%;
    border-radius: 15px;
    background-color: var(--Primary);
    border-radius: 15px;
    padding: 15px;
}

.editor {
    width: 100%;
    height: 100%;

}

</style>