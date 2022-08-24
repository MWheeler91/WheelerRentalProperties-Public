<template>
  <div class=" container-fluid bg-secondary text-center text-light">
    <div class="row">
      <div class="col-md-12">
        <div>
          <h1 class="text-center property_header">Properties</h1>
        </div>
      </div>
    </div>
  </div>

  <div class="container">
    <div v-for="property in properties"  :key="property.id">
      <property-card-wrapper v-if="property.is_active">
        <property-card  :property="property" />
      </property-card-wrapper>
    </div>
  </div>




</template>

<script>
import axios from "axios";
// import moment from 'moment'
import PropertyCard from "@/components/Properties/PropertyCard";
import PropertyCardWrapper from "@/components/Properties/PropertyCardWrapper";


export default {
  name: "PropertyPage",
  components: {
    PropertyCardWrapper,
    PropertyCard,
  },
  data() {
    return {
      properties: {}
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    async getData() {
      this.$store.commit('setIsLoading', true)
      axios
        .get('/api/properties')
        .then(response => {
          this.properties = response.data
        })
        .catch(error => {
          console.log(error)
        })
      console.log(this.properties)
      this.$store.commit('setIsLoading', false)
    },
  }
}
</script>

<style scoped>

</style>



<!--    <ol>-->
<!--      <li>{{property.id}}</li>-->
<!--      <li>{{property.property_num}}</li>-->
<!--      <li>{{property.property_road}}</li>-->
<!--      <li>{{property.rent}}</li>-->
<!--      <li>{{property.city}}</li>-->
<!--      <li>{{property.state}}</li>-->
<!--      <li>{{property.zip}}</li>-->
<!--      <li>{{property.bedrooms}}</li>-->
<!--      <li>{{property.bathrooms}}</li>-->
<!--      <li>{{property.sq_foot}}</li>-->
<!--      <li>{{property.property_title}}</li>-->
<!--      <li>{{property.property_short_description}}</li>-->
<!--      <li>{{property.description}}</li>-->
<!--      <li>{{property.is_active}}</li>-->
<!--      <li>{{property.thumbnail}}</li>-->
<!--      <li>{{property.thumbnail_alt_text}}</li>-->
<!--      <li>{{property.slug}}</li>-->
<!--      <li>{{property.available_date}}</li>-->
<!--      &lt;!&ndash;      <li>{{property.property_num}}</li>&ndash;&gt;-->
<!--    </ol>-->