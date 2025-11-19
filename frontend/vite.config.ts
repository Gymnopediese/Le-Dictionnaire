import tailwindcss from '@tailwindcss/vite';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [tailwindcss(), sveltekit()],
    server: {
        "allowedHosts" : ["dictionnaire.kofl.ch", "diskworld", "localhost"],
        proxy: {
            '/api': {
                target: 'http://backend:5000',
                changeOrigin: true,
                rewrite: (path) => path.replace(/^\/api/, ''),
            }
        }
    },
  
}
);
