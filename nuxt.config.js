import pkg from './package';

export default {
  mode: 'universal',

  head: {
    titleTemplate: (titleChunk) => {
      return titleChunk ? `${titleChunk} - Kinkini Roy Art Emporium and Gallery` : 'Kinkini Roy Art Emporium and Gallery';
    },    
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: pkg.description }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/img/favicon.jpg' },
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Playfair+Display|Poppins&display=swap' },
      { rel: 'stylesheet', href: 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.0.0/css/fontawesome.min.css' },
      { rel: 'stylesheet', href: '/bootstrap/css/bootstrap.min.css' },
      { rel: 'stylesheet', href: '/css/styles.css' },
    ],
    script: [
      { src: '/js/jquery.min.js' },
      { src: '/bootstrap/js/bootstrap.min.js' },
    ]
  },

  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },

  /*
  ** Global CSS
  */
  css: [
  ],

  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    '@nuxtjs/axios',
  ],

  axios: {
    // baseURL:"http://localhost:5000"
    baseURL:"http://www.kinkiniroy.com/api"
  },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
    }
  },
  env:{
    // baseURL: 'http://localhost:5000',
    baseURL: 'http://www.kinkiniroy.com/api',
  }
}
