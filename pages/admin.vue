<template>
    <div>
        <div class="container mt-4">
            <button type="button" class="btn btn-outline-danger mr-2" style="float:right"><i class="fas fa-power-off"></i> Sign Out</button>
            <h4 class="ml-2">Welcome, Kinkini</h4>
            <br>
            <div class="card shadow">
                <div class="card-body">
                    <select name="category" id="" class="form-select" style="float:right">
                        <option value="1">1</option>
                        <option value="2">2</option>
                    </select>
                    <h5 class="card-title">Select images</h5>
                    <h6 class="card-subtitle mb-2 text-muted">Select images to upload products</h6>
                    <div class="row">
                        <div class="col-lg-4 col-md-4"></div>
                        <div class="col-lg-4 col-md-4 col-sm-12">
                            <file-pond
                                name="test"
                                ref="pond"
                                label-idle="Drop image files here..."
                                v-bind:allow-multiple="true"
                                accepted-file-types="image/jpeg, image/png"
                                :server="url+'/savephotos'"
                                v-bind:files="myFiles"
                                v-on:init="handleFilePondInit"
                                @processfiles="handleComplete"
                                @processfile="handleAdd"
                                />
                        </div>
                        <div class="col-lg-4 col-md-4"></div>
                    </div>
                </div>
            </div>
            <br>
            <div class="card shadow" v-if="uploaded.length>0">
                <div class="card-body">
                    <button type="button" class="btn btn-success mr-2" style="float:right" @click.prevent="saveall"><i class="fas fa-power-off"></i> Save</button>
                    <button type="reset" class="btn btn-outline-dark mr-2" style="float:right" @click.prevent="reset"><i class="fas fa-power-off"></i> Reset</button>
                    <h5 class="card-title">Details</h5>
                    <br>
                    <div class="row no-gutters">
                        <div class="col-lg-4 col-md-6 col-sm-12 p-2" v-for="(x,i) in uploaded" :key="i" style="border:1px solid #eee">
                            <img :src="x.path" alt="" class="img-fluid mb-2">
                            <div class="row no-gutters">
                                <div class="form-group col-lg-9 col-md-9 col-sm-9">
                                    <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter title" v-model="x.title">
                                </div>
                                <div class="form-group col-lg-3 col-md-3 col-sm-3">
                                    <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Price" v-model="x.price">
                                </div>
                                <div class="form-group col-lg-12 col-md-12 col-sm-12">
                                    <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" placeholder="Enter description" v-model="x.description"></textarea>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import vueFilePond from 'vue-filepond';
import 'filepond/dist/filepond.min.css';
import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css';
import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type';
import FilePondPluginImagePreview from 'filepond-plugin-image-preview';
const FilePond = vueFilePond(FilePondPluginFileValidateType, FilePondPluginImagePreview);
export default {
    head:{
        title: "Admin"
    },
    data: function() {
        return { 
            myFiles: [],
            url: process.env.baseURL,
            uploading:[],
            uploaded:[]
        };
    },
    methods: {
        handleFilePondInit: function() {
            // FilePond instance methods are available on `this.$refs.pond`
        },
        handleComplete: function () {
            this.myFiles=[]
            this.uploading.forEach(element => {
                this.$axios.get("/getphotos/"+element).then(response=>{
                    var datax=response.data
                    datax.title=''
                    datax.price=''
                    datax.description=''
                    this.uploaded.push(datax)
                })
            });
            this.uploading=[]
        },
        handleAdd: function (error, file) {
            this.uploading.push(file.serverId)
        },
        saveall(){
            this.uploaded.forEach(element => {
                this.$axios.post("/updatephoto",element).then(response=>{
                    console.log(response.data)
                }).catch(err=>{
                    console.log(err)
                })
            });
        },
        reset(){
            this.uploaded=[]
            this.uploading=[]
        }
    },
    components: {
        FilePond
    }
}
</script>

<style>

</style>