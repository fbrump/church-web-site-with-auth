<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    title: String,
    subtitle: String
})

</script>

<template>
    <header>
        <h1 class="title">{{ props.title }}</h1>
        <h2 class="subtitle" v-hide="props.subtitle === ''" >{{ props.subtitle }}</h2>
    </header>
</template>

<style>
    
</style>