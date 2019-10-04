<template>
    <div>
        <h1 class="text-center mt-4">Embroideries</h1>
        <div class="container p-4">
            <div class="gallery" id="gallery">
                <nuxt-link :to="'/item?id='+x._id" style="text-decoration:none" v-for="(x,i) in photos" :key="i">
                    <div class="pics mb-3" style="">
                        <img class="img-fluid" :src="x.path" :alt="x.title">
                        <h6 class="p-2 text-center text-secondary">{{x.title}}</h6>
                    </div>
                </nuxt-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    head:{
      title: 'Embroideries'
    },
    data(){
        return {
            photos: []
        }
    },
    created(){
        this.getphotos()
    },
    methods:{
        getphotos(){
            this.$axios.get("/getphotoscat/embroideries").then(response=>{
                this.photos=response.data
            })
        }
    }

}
</script>

<style>
.gallery {
    -webkit-column-count: 3;
    -moz-column-count: 3;
    column-count: 3;
    -webkit-column-width: 33%;
    -moz-column-width: 33%;
    column-width: 33%; }
  .gallery .pics {
      background-color: #fdfdfd;
    -webkit-transition: all 350ms ease;
    transition: all 350ms ease; }
  .gallery .animation {
    -webkit-transform: scale(1);
    -ms-transform: scale(1);
    transform: scale(1); }

  @media (max-width: 450px) {
    .gallery {
      -webkit-column-count: 1;
      -moz-column-count: 1;
      column-count: 1;
      -webkit-column-width: 100%;
      -moz-column-width: 100%;
      column-width: 100%;
    }
  }

  @media (max-width: 400px) {
    .btn.filter {
      padding-left: 1.1rem;
      padding-right: 1.1rem;
    }
  }
</style>