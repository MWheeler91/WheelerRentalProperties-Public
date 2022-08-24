<template>
  <div class="container card-test">
    <slot />
  </div>
</template>

<script>
export default {
  name: "CardWrapper"
}
</script>

<style scoped>
.card-test{
    background-color: #ececec;
    padding: 30px;
    margin: 30px;
    border-radius: 15px;
    border: solid 2px;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
}
</style>