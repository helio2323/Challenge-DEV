<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { useCompLevel } from '@/composables/useLevel';

const temp = ref(0);
const maxPoints = ref(0);
const level = ref(1);

const { useLevel, getUserLevel } = useCompLevel();

onMounted(async () => {
  const userId = parseInt(localStorage.getItem('userid') || '0');
  const response = await getUserLevel(userId);

  if (response) {
    temp.value = response.points;
    maxPoints.value = response.points + response.next_level_points;
    level.value = response.level;
  }
});

const color = computed(() => {
  const progress = (temp.value / maxPoints.value) * 100;
  if (progress < 25) return 'blue';
  if (progress < 50) return 'amber';
  if (progress < 75) return 'orange';
  return 'red';
});

const progressMessage = computed(() => {
  const progress = (temp.value / maxPoints.value) * 100;
  if (progress < 25) return `Too cold! - Level ${level.value}`;
  if (progress < 50) return `Warm - Level ${level.value}`;
  if (progress < 75) return `Hot - Level ${level.value}`;
  return `🔥 Too hot! - Level ${level.value}`;
});
</script>

<template>
  <UProgress size="lg" :value="temp" :max="maxPoints" :color="color" class="transition-all duration-500">
    <template #indicator="{ number }">
      <div class="text-right" :style="{ width: `${number}%` }">
        <span :class="{
          'text-blue-500': color === 'blue',
          'text-amber-500': color === 'amber',
          'text-orange-500': color === 'orange',
          'text-red-500 font-bold': color === 'red'
        }">
          {{ progressMessage }}
        </span>
      </div>
      <div class="mt-2">
        Points: {{ temp }} / {{ maxPoints }}
      </div>
    </template>
  </UProgress>
</template>

