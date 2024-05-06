<script setup>
import { ref } from 'vue'
import PageHeader from '@/components/PageHeader.vue'

const pageTitle = ref('Home Page')
</script>

<template>
  <main class="container">
    <page-header :title="pageTitle"></page-header>
    <section class="section">
      <p class="has-text-centered">Welcome to the Church Web Site</p>
    </section>
  </main>
</template>

<style></style>
