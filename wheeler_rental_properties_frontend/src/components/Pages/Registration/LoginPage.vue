<template>
  <div class="container ">
      <div class="center-screen ">
          <div class="row">
              <div class="col-12">
                <card-wrapper>
                  <h2>Please login:</h2>
                  <form-kit type="form" submit-label="Login" @submit="submitForm" >
                    <form-kit type='email' name="email" label="Email Address" validation="required|email" />
                    <form-kit type='password' name="password" label="Password" hint="Password" validation="required|password" />
                  </form-kit>

                  <div class="mt-3">
                    <h5>Don't have an account? <router-link to="Registration">Register</router-link> </h5>
                    <h5>Forgot Password?  <router-link to="PasswordReset">Reset Password</router-link> </h5>
                  </div>
                </card-wrapper>
              </div>
          </div>
      </div>
</div>


</template>

<script>
import {FormKit, } from "@formkit/vue/index";
import CardWrapper from "@/components/Layout/CardWrapper";
import axios from "axios";
import router from "@/router";
// import router from "@/router";
// import {toast} from "bulma-toast";
// FormKitSchema
export default {
  name: "LoginPage",
  components: {
    CardWrapper,
    FormKit,
  },
  methods: {
    async submitForm(data) {
      data.email = data.email.toLowerCase()
      this.$store.commit('setIsLoading', true)
      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('token')

      await axios
        .post('/api/v1/token/login/', data)
        .then(response => {
          const token = response.data.auth_token
          // console.log(response.data.is_admin)
          this.$store.commit('setToken', token)
          axios.defaults.headers.common['Authorization'] = 'Token ' + token
          localStorage.setItem('token', token)
        })
        .catch(error => {
          console.log("There was an error")
          if (error.response) {
            console.log(error.response)
              // for (const property in error.response.data) {
              //     this.errors.push(`${property}: ${error.response.data[property]}`)
              // }
          } else if (error.message) {
              this.errors.push('Something went wrong. Please try again!')
          }
        })
      await axios
        .get('/api/v1/users/me')
        .then(response => {
          this.$store.commit('setUser', {
            'id': response.data.id,
            'email': response.data.email,
            'first_name': response.data.first_name,
            'last_name': response.data.last_name,
          })
          localStorage.setItem('userid', response.data.id)
          localStorage.setItem('email', response.data.email)
          localStorage.setItem('first_name', response.data.first_name)
          localStorage.setItem('last_name', response.data.last_name)
          localStorage.setItem('is_admin', response.data.is_admin)
        })
        .catch(error => {
            console.log(error)
        })
      this.$store.commit('initializeStore')
      this.$store.commit('setIsLoading', false)
      await router.push({path: '/'})
    }
  }
}
</script>

<style scoped>
.center-screen {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 10%;
}

</style>






<!--<div class=" jumbotron ">-->
<!--    <div class="container">-->
<!--        <div class="row">-->
<!--            <div class="col-12">-->
<!--                <h2>Please login:</h2>-->
<!--                {%  if form.errors %}-->
<!--                    <p>Your username and password didn't match.  Please try again</p>-->
<!--                {% endif %}-->

<!--                <form action="{% url 'account:login' %}" method="POST">-->
<!--                    {% csrf_token %}-->
<!--                    {{ form|crispy}}-->
<!--                    <input type="submit" class="btn btn-primary mt-3" value="login">-->
<!--                    <input type="hidden" name="next" value="{{next}}">-->
<!--                </form>-->
<!--                <div class="mt-3">-->
<!--                    <h5>Don't have an account?  <a href="{%  url 'account:register' %}">Register</a></h5>-->
<!--                    <h5>Forgot Password?  <a href="{%  url 'account:reset_password' %}">Password Reset</a></h5>-->
<!--                </div>-->
<!--            </div>-->
<!--        </div>-->
<!--    </div>-->
<!--</div>-->











<!--submitForm(){-->
<!--      axios.defaults.headers.common['Authorization'] = ""-->
<!--      localStorage.removeItem('token')-->

<!--      const formData = {-->
<!--        username: this.email,-->
<!--        password: this.password-->
<!--      }-->

<!--      axios-->
<!--          .post('/account/login/', formData)-->
<!--          .then(response => {-->
<!--            const token = response.data.token-->
<!--            const first_name = response.data.first_name-->
<!--            const last_name = response.data.last_name-->

<!--            this.$store.commit('setToken', token)-->
<!--            this.$store.commit('setUser', first_name, last_name)-->
<!--            axios.defaults.headers.common['Authorization'] = 'token ' + token-->
<!--            localStorage.setItem('token', token)-->
<!--            this.$router.push('/')-->
<!--          })-->
<!--          .catch(error => {-->
<!--            if (error.response) {-->
<!--              for (const property in error.response.data) {-->
<!--                this.errors.push(`${property}: ${error.response.data[property]}`)-->
<!--              }-->
<!--            } else if (error.message) {-->
<!--              this.errors.push('Something went wrong.')-->
<!--            }-->
<!--          })-->
<!--    }-->