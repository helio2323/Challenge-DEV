<template>
  <div>
    <UButton
    icon="i-heroicons-question-mark-circle"
    size="sm"
    color="primary"
    square
    variant="solid"
    @click="isOpen = true"
  />
    
    <UModal v-model="isOpen">
      <div class="modal">
        <DesafiosChallengSecChallengInfos />
      </div>
    </UModal>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const isOpen = ref(false)
</script>

<style scoped>
.modal {
  display: flex;
  width: 100%;
  padding: 10px;

}
</style>

