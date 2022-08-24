<template>
  <div class="home-page-header">
    <img class="homepageimage" src="~@/assets/images/homepagebanner2.jpg" alt="House at night">
  </div>
  <div class="text-center">
    <h1> content </h1>
  </div>
</template>

<script>
export default {
  name: "HomePage"
}
</script>

<style scoped>
  .home-page-header{
      height: 600px;
  }
  .homepageimage{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
</style>