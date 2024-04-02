<script setup>
import { RouterLink } from 'vue-router'

</script>

<template>
  <main>
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item" href="https://bulma.io">
          <span class="icon">
            <i class="fas fa-home"></i>
          </span>
        </router-link>

        <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">

          <router-link to="/" class="navbar-item" title="Go to the home page">
            Home
          </router-link>

          <router-link to="/small-groups" class="navbar-item" title="Go to the small groups">
            Small Groups
          </router-link>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <a class="button is-primary">
                <strong>Sign up</strong>
              </a>
              <a class="button is-light">
                Log in
              </a>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </main>
</template>
