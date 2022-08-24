<template>
  <nav class="navbar navbar-expand-xl navbar-dark bg-dark" role="navigation" aria-label="">
    <div class="container-fluid">
        <router-link to="/">
          <a class="navbar-brand" href="#"><img src="~@/assets/images/brand.png" alt="Brand Image"></a>
        </router-link>

        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent" >
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                    <router-link to="/properties" class="nav-link">Properties</router-link>
                </li>
                <li class="nav-item">
                    <router-link to="/application" class="nav-link" v-if="isAuthenticated">Application</router-link>
                </li>
                <li class="nav-item">
                    <router-link to="/contact" class="nav-link">Contact Us</router-link>
                </li>
            </ul>
            <ul class="navbar-nav mr-auto  flex-wrap ms-md-auto">
               <li class="nav-item" v-if="isAuthenticated">
                   <a class='nav-link' href="#">View Applications</a>
               </li>
               <li class="nav-item">
                   <a class='nav-link' href="http://192.68.50.66:8000/admin/" v-if="isAuthenticated">Admin</a>
               </li>

                <li class="nav-item dropdown" v-if="isAuthenticated">
                    <a class="nav-link dropdown-toggle" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">Welcome: {{ first_name }} {{last_name}}</a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <li><a class="dropdown-item" href="#">My Account</a></li>
                        <li><a class="dropdown-item" href="#">Another action</a></li>
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item" href="/" @click="logout">Log Out</a></li>
                    </ul>
                </li>
                <li class="nav-item" v-else>
                    <router-link to="/login" class="nav-link" v-if="!isAuthenticated">Login</router-link>
                </li>
            </ul>
        </div>
    </div>
</nav>
</template>


<script>
export default{
  data() {
    return {
      first_name: localStorage.getItem('first_name'),
      last_name: localStorage.getItem('last_name'),
      isAuthenticated: this.$store.state.isAuthenticated
    }
  },
  methods: {
    logout() {
      this.$store.commit('removeToken')
    }
  },
  computed: {

  }
}

</script>


<style>


</style>



<!--<nav class="navbar navbar-expand-xl navbar-dark bg-dark" role="navigation" aria-label="">-->
<!--    <div class="container-fluid">-->
<!--{#        <a class="navbar-brand" href="{% url 'base:home' %}"><img src="https://wheelerrentalproperties-bucket.s3.amazonaws.com/static/images/text-1644336324060.png"></a>#}-->
<!--        <a class="navbar-brand" href="{% url 'base:home' %}"><img src="{% static 'images/text-1644336324060.png'  %}" alt="Brand Image"></a>-->
<!--{#        <a class="navbar-brand" href="{% url 'base:home' %}"><img src="{{ brand_image.image }}" alt="Brand Image"></a>#}-->
<!--        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">-->
<!--            <span class="navbar-toggler-icon"></span>-->
<!--        </button>-->
<!--        <div class="collapse navbar-collapse" id="navbarSupportedContent" >-->
<!--            <ul class="navbar-nav mr-auto">-->
<!--                <li class="nav-item">-->
<!--                    <a class="nav-link" href="{% url 'base:properties' %}">Properties</a>-->
<!--                </li>-->
<!--                <li class="nav-item">-->
<!--                    <a class="nav-link" href="{% url 'base:application' %}">Application</a>-->
<!--                </li>-->
<!--                <li class="nav-item">-->
<!--                    <a class="nav-link" href="{% url 'base:contact' %}">Contact Us</a>-->
<!--                </li>-->
<!--            </ul>-->
<!--            <ul class="navbar-nav mr-auto  flex-wrap ms-md-auto">-->
<!--                {% if user.is_authenticated %}-->
<!--                    {% if user.is_superuser %}-->
<!--                       <li class="nav-item">-->
<!--                           <a class='nav-link' href="{% url 'base:application_list' %}">View Applications</a>-->
<!--                       </li>-->
<!--                       <li class="nav-item">-->
<!--                           <a class='nav-link' href="{% url 'admin:index' %}">Admin</a>-->
<!--                       </li>-->
<!--                    {% endif %}-->
<!--                    <li class="nav-item dropdown">-->
<!--                        <a class="nav-link dropdown-toggle" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">Welcome: {{ user }}</a>-->
<!--                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">-->
<!--                            <li><a class="dropdown-item" href="{% url 'account:account_home' %}">My Account</a></li>-->
<!--                            <li><a class="dropdown-item" href="#">Another action</a></li>-->
<!--                            <li><hr class="dropdown-divider"></li>-->
<!--                            <li><a class="dropdown-item" href="{% url 'account:logout' %}">Log Out</a></li>-->
<!--                        </ul>-->
<!--                    </li>-->
<!--                {% else %}-->
<!--                    <li class="nav-item">-->
<!--                        <a class="nav nav-link navbar-nav navbar-end" href="{% url 'account:login' %}">Login</a>-->
<!--                    </li>-->
<!--                {% endif %}-->
<!--            </ul>-->
<!--        </div>-->
<!--    </div>-->
<!--</nav>-->