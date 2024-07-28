<template>
<div class="card">
    <div class="card-content">
    <h3>Free</h3>
    <h2>{{ price }}<span>/mes</span></h2>
    
    <ul class="features-list">
        <li v-for="(item, index) in items" :key="index">
        <span><img :src="item.icon" alt=""></span> {{ item.text }}
        </li>
    </ul>
    
    <span @click="handleClick" class="subscribe-button">QUERO ESSE PLANO
        <img width="20" height="20" src="https://img.icons8.com/ios/50/061139/enter-2.png" alt="enter-2"/>
    </span>
    </div>
</div>
</template>

<script setup>
const props = defineProps({
price: {
    type: String,
    required: true
},
items: {
    type: Array,
    default: () => []
}
});

const handleClick = () => {
    navigateTo('/register');
}
</script>

<style scoped>
.card {
border: 1px solid #ddd;
border-radius: 8px;
overflow: hidden;
max-width: 400px;
margin: 20px auto;
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
padding: 10px;
}

.card-image {
width: 100%;
height: auto;
border-radius: 10px;
}

.card-content {
padding: 20px;
text-align: center;
}

.features-list img {
width: 20px;
height: 20px;
}

h3 {
margin: 0;
color: var(--Primary);
font-style: italic;
}

h2 {
margin: 10px 0;
color: var(--Primary);
}

h2 span {
font-size: 0.5em;
color: #647083;
}

.features-list {
list-style: none;
padding: 0;
text-align: left;
margin: 20px 0;
border-top: solid 1px #ddd;
}

.features-list li {
margin: 10px 0;
font-size: 1em;
display: flex;
align-items: center;
}

.features-list li span {
margin-right: 10px;
}

.subscribe-button {
display: flex;
flex-direction: row;
align-items: center;
justify-content: center;
gap: 10px;
padding: 10px 20px;
font-size: 1em;
color: var(--BackCover);
font-weight: bold;
background-color: var(--Primary);
border: none;
border-radius: 5px;
cursor: pointer;
transition: background-color 0.3s;
}

.subscribe-button:hover {
background-color: rgba(0, 0, 0, 0.1);
color: white;
}
</style>
