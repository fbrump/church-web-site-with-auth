import { defineStore } from 'pinia';
import { getAll } from '@/resources/small-group';


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
      getById(id) {
        // TO-DO: Call API
        this.load();
        const filtered = this.all.filter((item) => item.id === id);
        this.selected = filtered.length === 1 ? filtered[0] : null;
      },
    },
  })