<script setup>
import { ref } from 'vue'
import PageHeader from '@/components/PageHeader.vue'
import SmallGroupTable from '@/components/small-groups/SmallGroupTable.vue'
import SmallGroupFilter from '@/components/small-groups/SmallGroupFilter.vue'

const pageTitle = ref('Small Groups');

const filterParameters = ref({
  byTitle: '',
  byHour: '',
  byWeekday: ''
})

const updateFilterTitle = (title) => {
  filterParameters.value.byTitle = title;
};

const updateFilterHour = (hour) => {
  filterParameters.value.byHour = hour;
};

const updateFilterWeekday = (weekday) => {
  filterParameters.value.byWeekday = weekday;
};

</script>

<template>
  <main class="container">
    <page-header :title="pageTitle"></page-header>
    <section class="section">
      <small-group-filter @update-filter-title="updateFilterTitle" @update-filter-hour="updateFilterHour"
        @update-filter-weekday="updateFilterWeekday"></small-group-filter>
    </section>
    <section class="section">
      <small-group-table :filterParameter="filterParameters"></small-group-table>
    </section>
  </main>
</template>

<style></style>
