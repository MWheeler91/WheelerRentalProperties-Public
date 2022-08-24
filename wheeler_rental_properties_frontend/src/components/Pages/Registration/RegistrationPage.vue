<template>
  <div class='container'>
<!--    <div class="center-screen">-->
      <div class="row">
        <div class="col-12">
          <card-wrapper>
            <h1 class="title">Sign up</h1>
              <form-kit type="form" id='registration' submit-lable="Create Account"   @submit="submitForm">
                <form-kit type="email" name="email" label='Email' validation="required|email"/>
                <form-kit type="email" name="email_confirm" label='Confirm Email' validation="required|confirm"/>
                <form-kit type="password" name="password" label="Password" validation="required|length:8"/>
                <form-kit type="password" name="password_confirm" label="Confirm Password" validation="required|confirm"/>
                <form-kit type="text" name="first_name" label="First Name" validation="required|text"/>
                <form-kit type="text" name="last_name" label="Last Name" validation="required|text"/>
              </form-kit>
          </card-wrapper>
        </div>
      </div>
<!--    </div>-->
  </div>
</template>

<script>
import {FormKit} from "@formkit/vue/index";
import axios from "axios";
import {toast} from "bulma-toast";
import CardWrapper from "@/components/Layout/CardWrapper";
export default {
  name: "SignUp.vue",
  components: {CardWrapper, FormKit},
  methods: {
    submitForm(data){
      data.email = data.email.toLowerCase()
      axios
        .post('/account/register/', data)
        .then(response => {
          const token = response.data.token
          this.$store.commit('setToken', token)
          axios.defaults.headers.common['Authorization'] = 'Token ' + token
          localStorage.setItem('token', token)

          toast({
            message:'Account was created, Please Login',
            type: 'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: 'bottom-right',
          })
          this.$router.push('/login')
        })
        .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }
            } else if (error.message) {
              this.errors.push('Something went wrong.')
            }
          })
    }
  }
}
</script>

<style scoped>
.center-screen {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>




<!-- <form>-->
<!--          <div class="field">-->
<!--            <label>Email</label>-->
<!--            <div class="control">-->
<!--              <input type="email" name="email1" class="input">-->
<!--            </div>-->
<!--          </div>-->

<!--          <div class="field">-->
<!--            <label>Email</label>-->
<!--            <div class="control">-->
<!--              <input type="email" name="email2" class="input">-->
<!--            </div>-->
<!--          </div>-->

<!--          <div class="field">-->
<!--            <label>Password</label>-->
<!--            <div class="control">-->
<!--              <input type="password" name="password1" class="input">-->
<!--            </div>-->
<!--          </div>-->

<!--          <div class="field">-->
<!--            <label>Confirm Password</label>-->
<!--            <div class="control">-->
<!--              <input type="password" name="password2" class="input">-->
<!--            </div>-->
<!--          </div>-->

<!--          <div class="field">-->
<!--            <label>First Name</label>-->
<!--            <div class="control">-->
<!--              <input type="text" name="first-name" class="input">-->
<!--            </div>-->
<!--          </div>-->

<!--          <div class="field">-->
<!--            <label>Last name</label>-->
<!--            <div class="control">-->
<!--              <input type="text" name="last-name" class="input">-->
<!--            </div>-->
<!--          </div>-->

<!--          <div class="field">-->
<!--            <div class="control">-->
<!--              <button class="button is-success">Submit</button>-->
<!--            </div>-->
<!--          </div>-->

<!--        </form>-->