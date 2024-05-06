<script setup>
import { RouterView } from 'vue-router'
import NavbarMenu from '@/components/loyout/NavbarMenu.vue'
import FooterComponent from '@/components/loyout/FooterComponent.vue'
</script>

<template>
  <header>
    <navbar-menu></navbar-menu>
  </header>
  <RouterView />
  <footer-component></footer-component>
</template>

<style scoped></style>
