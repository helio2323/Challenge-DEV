<template>
    <div>
        <h2 class="">
                AVANCE AGORA MESMO 
                NOS SEUS ESTUDOS <strong>{{ text }}</strong>
            </h2>
    </div>
</template>

<script setup>

const props = defineProps({
    text: String
})

</script>

<style  scoped>
 h2 {
    color: white;
    font-size: 28px;
    font-weight: bold;
    text-align: start;
    width: 50%;
}

@media screen and (max-width: 950px) {
    h2 {
        width: 100%;
    }
}

strong{
    color: var(--Primary);
}
</style>