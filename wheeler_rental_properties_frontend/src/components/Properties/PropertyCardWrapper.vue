<template>
  <div class="container">
    <div class="row main-section property-card property-shadow my-3">
      <slot></slot>
    </div>
  </div>

</template>

<script>
export default {
  name: "PropertyCardWrapper"
}
</script>

<style scoped>
.property-card{
    background-color: #ececec;
    padding: 10px;
    border-radius: 15px;
    border: solid 2px;
}
.property-shadow{
    box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(51, 51, 51) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
}
</style>