<script setup>
import { ref } from 'vue'

const company = ref('Brum')
</script>

<template>
  <main>
    <footer class="footer">
      <div class="content has-text-centered">
        <p>
          Powered by <strong>{{ company }}</strong
          >. The source code is licensed
          <a href="http://opensource.org/licenses/mit-license.php">MIT</a>.
        </p>
      </div>
    </footer>
  </main>
</template>
