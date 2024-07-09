<script setup>
import { RouterLink } from 'vue-router'
import { computed, defineProps } from 'vue'
import { useSmallGroupStore } from '@/store/small-group'

defineProps({
  filterParameter: Object
})

const smallGroupStore = useSmallGroupStore()

smallGroupStore.load()

var items = computed(() => smallGroupStore.all)
</script>

<template>
  <div class="table-container">
    <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
      <thead class="has-background-info-dark">
        <tr>
          <th>Title</th>
          <th>Weekday</th>
          <th>Start at</th>
          <th>Finish at</th>
          <th class="has-text-centered">Details</th>
        </tr>
      </thead>
      <tfoot class="has-background-info-dark">
        <th colspan="5" class="has-text-centered">Total Items {{ items.length }}</th>
      </tfoot>
      <tbody>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.title }}</td>
          <td>{{ item.weekday }}</td>
          <td>{{ item.start_at }}H</td>
          <td>{{ item.finish_at }}H</td>
          <td class="has-text-centered">
            <router-link :to="'/small-groups/' + item.id" class="button is-ghost">
              <span class="icon">
                <i class="fa-solid fa-pen-to-square"></i>
              </span>
              <span>More</span>
            </router-link>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
