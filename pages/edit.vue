<template>
    <div>
        <div class="container mt-4">
            <nuxt-link to="/admin" class="btn btn-outline-info mr-2" style="float:right"><i class="fas fa-power-off"></i> Upload</nuxt-link>
            <h4 class="ml-2">Welcome, Kinkini</h4>
            <br>
            <div class="card shadow">
                <div class="card-body">
                    <select name="category" id="" class="custom-select" style="float:right;width:200px" v-model="selectedcategory" @change="loadphotos(selectedcategory)">
                        <option value="quillings">Quillings</option>
                        <option value="earrings">Earrings</option>
                        <option value="embroideries">Embroideries</option>
                    </select>
                    <h5 class="card-title">Edit Items</h5>
                    <h6 class="card-subtitle mb-2 text-muted">Select category to edit products</h6>
                </div>
            </div>

            <div class="card shadow mt-4">
                <div class="card-body">
                    <button type="button" class="btn btn-success mr-2" style="float:right" @click.prevent="saveall"><i class="fas fa-power-off"></i> Save</button>
                    <span v-if="savevisible" class="text-success p-2" style="float:right">Saved successfully</span>
                    <h4>{{selectedcategory}} ({{photos.length}} photos)</h4>
                    <hr>
                    <div class="row" v-for="(x,i) in photos" :key="i">
                        <div class="col-lg-4 col-sm-12 col-md-4">
                            <img class="img-fluid" :src="x.path">
                        </div>
                        <div class="col-lg-8 col-sm-12 col-md-8">
                            <label for="exampleInputEmail1">Title</label>
                            <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter title" v-model="x.title">
                            <label for="exampleInputEmail1">Price</label>
                            <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Price" v-model="x.price">
                            <label for="exampleInputEmail1">Description</label>
                            <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" placeholder="Enter description" v-model="x.description"></textarea>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    head:{
        title: 'Edit Photos'
    },
    data(){
        return {
            selectedcategory:'quillings',
            photos:[],
            savevisible:false
        }
    },
    created(){
        this.loadphotos(this.selectedcategory)
    },
    methods:{
        loadphotos(type)
        {
            this.$axios.get("/getphotoscat/"+type).then(response=>{
                this.photos=response.data
            })
        },
        saveall(){
            this.photos.forEach(element => {
                element.cat=this.selectedcategory
                this.$axios.post("/updatephoto",element).then(response=>{
                    this.savevisible=true
                    setTimeout(() => {
                        this.savevisible=false
                    }, 3000);
                }).catch(err=>{
                    console.log(err)
                })
            });
        },
    }

}
</script>

<style>

</style>