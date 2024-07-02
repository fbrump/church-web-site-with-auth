import { fileURLToPath, URL } from 'node:url'

import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import VueDevTools from 'vite-plugin-vue-devtools'

// https://vitejs.dev/config/
export default defineConfig(({ command, mode }) => {
  const env = loadEnv(mode, process.cwd(), '')

  const serverConfig = {
    proxy: {
      '/api-core': {
        target: env.VITE_API_CORE_HOST + '/api/v1/',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api-core/, ''),
      },
      '/api-auth': {
        target: env.VITE_API_CORE_HOST + '/api/v1/',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api-auth/, ''),
      }
    }
  }

  return {
    plugins: [
      vue(),
      VueDevTools(),
    ],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    },
    server: serverConfig
  }
})
