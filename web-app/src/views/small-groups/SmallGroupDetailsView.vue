<script setup>
import { computed, ref, defineProps } from 'vue'
import PageHeader from '@/components/PageHeader.vue'
import { useSmallGroupStore } from '@/store/small-group';


var props = defineProps({
  id: {
    type: String,
    required: true
  }
})

const smallGroupStore = useSmallGroupStore();

smallGroupStore.getById(props.id);

const itemDetails = computed(() => smallGroupStore.selected);

const pageTitle = ref('Small Group Details');
</script>

<template>
  <main class="container">
    <page-header :title="pageTitle" :subtitle="itemDetails.title"></page-header>
    <section>
      <p>Let's be part of the {{ itemDetails.title }} group too!</p>
      <p>
        Every {{ itemDetails.weekday }} at {{ itemDetails.start_at }} (and ending at
        {{ itemDetails.finish_at }}).
      </p>
    </section>
  </main>
</template>

<style></style>
