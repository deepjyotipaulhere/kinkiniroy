<template>
    <div>
        <div class="container">
            <div class="row">
                <div class="col-lg-4 col-md-4"></div>
                <div class="col-lg-4 col-md-4 col-sm-12">
                    <h2 class="text-center mt-4">Feedback and Query</h2>
                    <div class="alert alert-success" role="alert" v-show="isok">
                        Your message has been saved. We will get in touch with you soon!
                    </div>
                    <div class="card shadow m-4">
                        <div class="card-body">
                            <form @submit.prevent="send">
                                <div class="form-group">
                                    <label for="exampleInputEmail1">Subject</label>
                                    <input v-model="message.subject" type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter subject">
                                </div>
                                <div class="form-group">
                                    <label for="exampleInputEmail1">Name</label>
                                    <input v-model="message.name" type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter your name">
                                </div>
                                <div class="form-group">
                                    <label for="exampleInputEmail1">Your email</label>
                                    <input v-model="message.email" type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter your email">
                                </div>
                                <div class="form-group">
                                    <label for="exampleFormControlTextarea1">Your message</label>
                                    <textarea v-model="message.text" class="form-control" id="exampleFormControlTextarea1" rows="3" placeholder="Write your message here..."></textarea>
                                </div>
                                <input type="submit" value="Send message" class="btn btn-block btn-primary">
                            </form>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-4"></div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            message:{
                subject:'',
                name: '',
                email: '',
                text: ''
            },
            isok:false
        }
    },
    methods:{
        send(){
            this.$axios.post("/sendmessage",this.message).then(response=>{
                this.isok=true
                this.message.subject=''
                this.message.name=''
                this.message.email=''
                this.message.text=''
            })
        }
    }
}
</script>

<style>

</style>