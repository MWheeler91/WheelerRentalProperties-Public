<template>
  <div>
    <NavBar />
    <div class="content">
      <router-view/>
    </div>

  </div>
  <div class="footer">
    <hr>
    <p role="contentinfo" class="container"> Copyright &copy; {% now "Y" %} MWheeler Development. </p>
  </div>
</template>

<script>
import NavBar from './components/Layout/NavBar'
import axios from "axios";


  export default {
    name: 'App',
    components: {
      NavBar
    },
    beforeCreate() {
      this.$store.commit('initializeStore')

      if (this.$store.state.token) {
        axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
    }
  }
</script>

<style>
.content {
  min-height: calc(100vh - 70px);
}
.footer {
  height: 50px;
}
body{
  background-color: #d4d4d4;
}
.formkit-inner{
  background-color: white;
  width: 100%;

}
.formkit-wrapper{
    width: 100%;
}
.formkit-wrapper{
    width: 100%;
}
.full-width {
  width: 100%;
}

/*.form-label {*/
/*  font-weight: bold;*/
/*}*/

</style>
