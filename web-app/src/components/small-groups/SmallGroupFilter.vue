<script setup>
import { ref } from 'vue'
import getWeekdays from '@/storage/weekday-resourse';

const byTitle = ref('');
const byWeekday = ref('');
const byHour = ref('');

const weekdays = ref(getWeekdays())
</script>

<template>

<form action="" id="filterForm">
    <div class="field">
        <label for="filter.title" class="label">
        Title
        <div id="filter.title" class="control">
            <input type="text" @change="$emit('updateFilterTitle', byTitle)" v-model="byTitle" class="input" placeholder="Search by title">
        </div>
        </label>
        <p class="help">Enter with the title</p>
    </div>
    <div class="field">
        <label class="label">
            Hour
            <div class="control has-icons-left has-icons-right">
                <input @change="$emit('updateFilterHour', byHour)" v-model="byHour" class="input" type="time" placeholder="hh:mm am/pm">
                <span class="icon is-small is-left">
                <i class="fas fa-clock"></i>
                </span>
            </div>
        </label>
        <p class="help">Enter with time (hh:mm AM/PM)</p>
    </div>
    <div class="field">
        <label class="label">
        Weekday
        <div class="control">
            <div class="select">
            <select @change="$emit('updateFilterWeekday', byWeekday)" v-model="byWeekday">
                <option disabled value="">Select one</option>
                <option v-for="day in weekdays" :key="day.id" v-memo="[day.id === selected]">
                    {{ day.name }}
                </option>
            </select>
            </div>
        </div>
        </label>
    </div>
</form>
</template>