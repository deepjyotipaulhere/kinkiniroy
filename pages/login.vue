<template>
    <div>
        <div class="container">
            <div class="row">
                <div class="col-lg-4 col-md-4"></div>
                <div class="col-lg-4 col-md-4 col-sm-12 p-4">
                    <div class="card shadow" style="width: 100%;">
                        <div class="card-body">
                            <h2 class="card-title">Sign In</h2>
                            <h6 class="card-subtitle mb-2 text-muted">Sign in to upload photos</h6>
                            <br>
                            <form @submit.prevent="login">
                                <div class="form-group">
                                    <label for="exampleInputEmail1">Email address</label>
                                    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
                                </div>
                                <div class="form-group">
                                    <label for="exampleInputEmail1">Password</label>
                                    <input type="password" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter password">
                                </div>
                                <input type="submit" value="Sign In" class="btn btn-dark btn-block">
                            </form>
                        </div>
                    </div>
                    <center>
                        <small class="text-muted">&copy; Kinkini Roy</small>
                    </center>
                </div>
                <div class="col-lg-4 col-md-4"></div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    head:{
        title: 'Sign In'
    },
    methods:{
        login(){

            this.$router.push("/admin")
        }
    }
}
</script>

<style>

</style>