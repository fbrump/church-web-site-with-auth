import { defineStore } from 'pinia';
import { getAll, getById } from '@/resources/small-group';


export const useSmallGroupStore = defineStore('small-group', {
    state: () => ({ items: [], selected: null }),
    getters: {
      all: (state) => state.items,
      detailed: (state) => state.selected,
    },
    actions: {
      async load() {
        getAll()
          .then((response) => {
            this.items = response.data;
          })
          .catch((error) => console.error(error));
      },
      async getById(id) {
        getById(id)
          .then((response) => {
            this.selected = response.data;
          })
          .catch((error) => {
            this.selected = null;
            console.error(error)
          });
      },
    },
  })