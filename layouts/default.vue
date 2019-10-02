<template>
  <div>
    <div class="shadow">
      <div class="text-center" style="margin: 1em;margin-bottom:0"><img src="/img/kinkini.jpg" width="200px" height="auto"></div>
      <nav class="navbar navbar-light navbar-expand-md">
          <div class="d-flex w-50 order-2 justify-content-center">
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsingNavbar">
                  <span class="navbar-toggler-icon"></span>
              </button>
          </div>
          <div class="navbar-collapse collapse justify-content-center order-2" id="collapsingNavbar">
              <ul class="navbar-nav">
                  <li class="nav-item p-2">
                      <a class="nav-link" href="#">Home <span class="sr-only">Home</span></a>
                  </li>
                  <li class="nav-item p-2">
                      <a class="nav-link" href="#">About</a>
                  </li>
                  <li class="nav-item p-2">
                      <nuxt-link class="nav-link" to="/quillings">Quillings</nuxt-link>
                  </li>
                  <li class="nav-item p-2">
                      <nuxt-link class="nav-link" to="/earrings">Earrings</nuxt-link>
                  </li>
                  <li class="nav-item p-2">
                      <nuxt-link class="nav-link" to="/embroideries">Embroideries</nuxt-link>
                  </li>
                  <li class="nav-item p-2">
                      <a class="nav-link" href="#">Contact</a>
                  </li>
              </ul>
          </div>
          <span class="navbar-text small text-truncate mt-1 w-50 text-right order-1 order-md-last"></span>
      </nav>
    </div>
    <nuxt />
  </div>
</template>

<script>
export default {
    head:{
        meta:[
            { name: 'description', content: 'Kinkini Roy Art Emporium and Gallery' },
            { name: 'og:title', content: 'Kinkini Roy Art Emporium and Gallery' },
            { name: 'og:url', content: 'http://www.kinkiniroy.com' },
            { name: 'og:description', content: 'Kinkini Roy Art Emporium and Gallery' },
            { name: 'og:type', content: 'website' },

            { name: 'og:image', content: '/cover.jpg' },
            { name: 'og:image:type', content: 'image/jpg' },
            { name: 'og:image:width', content: '1200' },
            { name: 'og:image:height', content: '630' },

            { name: 'og:image', content: '/whatsappcover.jpg' },
            { name: 'og:image:type', content: 'image/jpg' },
            { name: 'og:image:width', content: '400' },
            { name: 'og:image:height', content: '400' },

            { name: 'twitter:card', content: 'summary_large_image' },
            { name: 'twitter:description', content: 'Kinkini Roy Art Emporium and Gallery' },
            { name: 'twitter:image', content: '/cover.jpg' },
        ]
    }
}
</script>

<style>
</style>
