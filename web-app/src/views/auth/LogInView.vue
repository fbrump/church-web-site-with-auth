<script setup>
import { useAuthStore } from '@/store/auth'
import { ref } from 'vue'

const authStore = useAuthStore()

const username = ref('')
const password = ref('')
const rememberMe = ref(false)

const onSubmitLogin = async () => {
  await authStore.login(username.value, password.value)
}
</script>

<template>
  <main>
    <section class="hero is-fullheight">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <div class="column is-5-tablet is-4-desktop is-3-widescreen">
              <form action="" class="box" @submit.prevent="onSubmitLogin">
                <div class="field">
                  <label for="" class="label">Email</label>
                  <div class="control has-icons-left">
                    <input
                      type="text"
                      v-model="username"
                      placeholder="e.g. bobsmith@gmail.com"
                      class="input"
                      required
                    />
                    <span class="icon is-small is-left">
                      <i class="fa fa-envelope"></i>
                    </span>
                  </div>
                </div>
                <div class="field">
                  <label for="" class="label">Password</label>
                  <div class="control has-icons-left">
                    <input
                      type="password"
                      v-model="password"
                      placeholder="*******"
                      class="input"
                      required
                    />
                    <span class="icon is-small is-left">
                      <i class="fa fa-lock"></i>
                    </span>
                  </div>
                </div>
                <div class="field">
                  <label for="" class="checkbox">
                    <input type="checkbox" v-model="rememberMe" />
                    Remember me
                  </label>
                </div>
                <div class="field">
                  <button class="button is-success">Login</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>
