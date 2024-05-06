<script setup>
import { ref } from 'vue'
import PageHeader from '@/components/PageHeader.vue'
import { getSmallGroup } from '@/storage/small-group-resource';


var props = defineProps({
  id: {
    type: String,
    required: true,
  }
});

const pageTitle = ref('Small Group Details');
const itemDetails = ref(getSmallGroup(props.id));

</script>

<template>
  <main class="container">
    <page-header :title="pageTitle" :subtitle="itemDetails.title"></page-header>
    <section>
      <p>
        Let's be part of the {{ itemDetails.title }} group too!
      </p>
      <p>
        Every {{ itemDetails.weekday }} at {{ itemDetails.startAt }} (and ending at {{ itemDetails.finishAt }}).
      </p>
    </section>
  </main>
</template>

<style></style>
