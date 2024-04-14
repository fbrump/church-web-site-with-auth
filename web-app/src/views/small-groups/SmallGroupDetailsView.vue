<script setup>
import { ref } from 'vue'
import PageHeader from './../../components/PageHeader.vue'

const smallGroupDetail = ref({
  title: 'Men',
  weekday: 'Friday',
  startAt: 20,
  finishAt: 21,
  phoneNumber: 919999002,
  url: 'https://maps.app.goo.gl/sNqrLEJodsjRYe6c7',
  address: {
    street: 'Rua Carlos Teixeira',
    number: 19,
    references: '1° Direito',
    zipCode: 4715213,
    neibohood: 'São Lázaro',
    state: 'Braga',
    city: 'Braga'
  }
});

</script>

<template>
  <main class="container">
    <page-header :title="smallGroupDetail.title" :subtitle="'#' + this.$route.params.id"></page-header>
    <section class="section">
      <div class="columns">
        <div class="column">
          <p>
            This is the {{ smallGroupDetail.title }} small group, every {{ smallGroupDetail.weekday }} 
            at <time :datetime="smallGroupDetail.startAt">{{ smallGroupDetail.startAt }}H</time> and finish
            at <time :datetime="smallGroupDetail.finishAt">{{ smallGroupDetail.finishAt }}H</time>.
          </p>
          <p>
            If you enjoy, and want to learn more about it let us know through this contact: <br />
            <strong>{{ smallGroupDetail.phoneNumber }}</strong>
          </p>
        </div>
        <div class="column">
          <p>
            Check our address:
            <address>
              {{ smallGroupDetail.address.number }}, {{ smallGroupDetail.address.street }} <br />
              {{ smallGroupDetail.address.neibohood }} <br />
              <span v-if="smallGroupDetail.address.references">
                {{ smallGroupDetail.address.references }} <br />
              </span>
              {{ smallGroupDetail.address.zipCode }}<br />
              {{ smallGroupDetail.address.city }} - {{ smallGroupDetail.address.state }}<br />
            </address>
            Or click on the <a :href=smallGroupDetail.url>map</a>.
          </p>
        </div>
      </div>
    </section>
  </main>
</template>

<style></style>
