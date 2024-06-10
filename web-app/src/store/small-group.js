import { defineStore } from 'pinia';

export const useSmallGroupStore = defineStore('small-group', {
    state: () => ({ items: [], selected: null }),
    getters: {
      all: (state) => state.items,
      detailed: (state) => state.selected,
    },
    actions: {
      load() {
        // TO-DO: Call API
        this.items = [
          {
            id: 'c4b962de-2342-4e63-9e93-03ca03dd9f8a',
            title: 'Men',
            weekday: 'Monday',
            startAt: 20,
            finishAt: 21
          },
          {
            id: '11dd0de8-3564-4369-96db-1f07a8de2d17',
            title: 'Women',
            weekday: 'Thursday',
            startAt: 20,
            finishAt: 21
          },
          {
            id: 'c5fb92c1-cf24-4aac-91f4-ebfe5e382aa0',
            title: 'Kids',
            weekday: 'Saturday',
            startAt: 15,
            finishAt: 16
          }
        ].sort((t) => t.title)
      },
      getById(id) {
        // TO-DO: Call API
        this.load();
        const filtered = this.all.filter((item) => item.id === id);
        this.selected = filtered.length === 1 ? filtered[0] : null;
      },
    },
  })