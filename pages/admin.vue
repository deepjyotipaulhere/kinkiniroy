<template>
    <div>
        <div class="container mt-4">
            <button type="button" class="btn btn-outline-danger mr-2" style="float:right"><i class="fas fa-power-off"></i> Sign Out</button>
            <h4 class="ml-2">Welcome, Kinkini</h4>
            <br>
            <div class="card shadow">
                <div class="card-body">
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
                                server="/api"
                                v-bind:files="myFiles"
                                v-on:init="handleFilePondInit"
                                />
                        </div>
                        <div class="col-lg-4 col-md-4"></div>
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
        return { myFiles: [] };
    },
    methods: {
        handleFilePondInit: function() {
            console.log('FilePond has initialized');

            // FilePond instance methods are available on `this.$refs.pond`
        }
    },
    components: {
        FilePond
    }
}
</script>

<style>

</style>