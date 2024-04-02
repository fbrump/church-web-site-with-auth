<script setup>
import { ref } from 'vue'
import PageHeader from './../../components/PageHeader.vue'

const pageTitle = ref('Small Groups')
</script>

<template>
  <main class="container">
    <page-header :title="pageTitle"></page-header>
  </main>
</template>

<style></style>
