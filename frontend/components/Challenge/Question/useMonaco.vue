<template>
    <MonacoEditor
              class="editor"
              :options="{ theme: 'vs-dark', language: 'python' }"
              v-model="value"
              :lang="langValue"
               
            />
  </template>
  
  <script lang="ts" setup>
  const editorRef = ref<InstanceType<typeof MonacoEditor>>()
    
    const props = defineProps({
      langValue: {
        type: String,
        default: 'python',
      },
    })
    const onEditorDidMount = (editor: any, monaco: any) => {
      editorRef.value = editor

      editor.onDidChangeModelContent(() => {
        const model = editor.getModel()
        if (model) {
          value.value = model.getValue()
        }
      })
    }


  </script>
  