<template>
    <div>
        <br>
        <div class="container pt-4" v-show="photo.path!=undefined">
            <div class="row">
                <div class="col-lg-2 col-md-2"></div>
                <div class="col-lg-4 col-md-4 col-sm-12">
                    <img :src="photo.path" :alt="photo.title" class="img-fluid">
                </div>
                <div class="col-lg-6 col-md-4 col-sm-12">
                    <h2 class="mb-4 mt-4">{{photo.title}}</h2>
                    <h6 class="mb-4">Size: {{photo.size}}</h6>
                    <p v-if="photo.color">Color: {{photo.color}}</p>
                    <p class="mb-4 text-muted">{{photo.description}}</p>
                    <p style="font-size:xx-large" class="mt-4">&#8377; {{photo.price}}</p>
                </div>
                <div class="col-lg-2 col-md-2"></div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            photo:{}
        }
    },

    created(){
        this.loadphoto()
    },

    methods:{
        loadphoto(){
            this.$axios.get("/getphotos/"+this.$route.query.id).then(response=>{
                this.photo=response.data
            })
        }
    }
}
</script>

<style>

</style>