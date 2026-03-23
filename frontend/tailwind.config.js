/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'temple-red': '#722F37', // Deep Maroon / wine structure
        'heritage-gold': '#D4AF37', // Soft warm gold accents
        'ivory-white': '#FDFBF7', // Parchment-like background
        'charcoal-dark': '#333333', // Maximum readability text
      },
      fontFamily: {
        'traditional': ['Lora', 'Georgia', 'serif'], // Elegant traditional touch
      },
      boxShadow: {
        'soft': '0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03)',
      }
    },
  },
  plugins: [],
}
