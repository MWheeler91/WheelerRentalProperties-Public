<template>

  <div class="jumbotron text-center " >
      <h1>{{ propertyDetails.full_address }}</h1>
<!--    <hr>-->
  </div>




  <property-card-wrapper>
    <div class="container ">
      <div id="carouselExampleIndicators" class="carousel slide carousel-styling " data-bs-ride="carousel">
        <div class="carousel-indicators ">
          <div v-for="(image, index) in propertyImages" :key="index">
              <button type="button" data-bs-target="#carouselExampleIndicators" :data-bs-slide-to="index" :class=" index === 0? 'active' : '' " aria-current="true" aria-label="Slide 1"></button>
          </div>
        </div>
        <div class="carousel-inner property-image">
          <div v-for="(image, index) in propertyImages" :key="index" :class="index === 0 ? 'carousel-item active' : 'carousel-item'">
            <img :src="getContentImageLink(image.image)" alt="image.alt_text" class="d-block w-100" >
            <div class="carousel-caption d-none d-md-block">
              <h5>{{ image.alt_text }}</h5>
              <p v-if='image.image_description'>{{ image.image_description }}</p>
            </div>
          </div>
<!--                 <div class="carousel-item {% if forloop.counter0 == 0 %}active{% endif %}" data-interval="5000">-->
<!--                </div>-->
        </div>

        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="visually">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually">Next</span>
        </button>
      </div>
    </div>

    <div class="container">
      <div class="row text-center">
          <div class="col-6 col-md-3 p-2">
              <dt>RENT</dt>
              <dd> ${{ propertyDetails.rent }}</dd>
          </div>
          <div class="col-6 col-md-3 p-2 property-text-border">
              <dt>Bed / Bath</dt>
              <dd> {{ propertyDetails.bedrooms }} / {{ propertyDetails.bathrooms }}</dd>
          </div>
          <div class="col-6 col-md-3 p-2 property-text-border">
              <dt>Square Foot</dt>
              <dd> {{ propertyDetails.sq_foot }}</dd>
          </div>
          <div class="col-6 col-md-3 p-2 property-text-border">
              <dt>Available On</dt>
              <dd> {{ propertyDetails.available_date }}</dd>
          </div>
      </div>
      <div class="row">
          <div class="col-lg-12">
          </div>
      </div>
      <div class="row mt-4">
          <p style="white-space: pre-wrap;" >Description: {{ propertyDetails.description }}</p>
      </div>
    </div>

    <div class="container">
      <router-link class="btn btn-primary" :to="{name: 'Application',
          params: {
            id: propertyDetails.id,
            address: propertyDetails.address
          }}">Apply Today! </router-link>

    </div>
  </property-card-wrapper>

<!--     <router-link :to="{name: 'propertyDetails', params: {-->
<!--       slug: property.slug,-->
<!--     }}">-->

</template>

<script>
import axios from "axios";
import PropertyCardWrapper from "@/components/Properties/PropertyCardWrapper";
// import {BCarousel, BCarouselSlide} from "bootstrap-vue-3";

export default {
  name: "PropertyDetails",
  components: {
    PropertyCardWrapper,
    // BCarousel,
    // BCarouselSlide
  },
  props: [

  ],

  data() {
    return {
      propertyDetails: {},
      propertyImages: {},
      slide: 0,
      sliding: null,
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    async getData() {
      // const propertyId = this.id
      this.$store.commit('setIsLoading', true)
        await axios
          .get('/api/properties/get_details/' + this.$route.params.slug)
          .then(response => {
            this.propertyDetails = response.data
          })
          .catch(error => {
          console.log("error: " +error)
        })
      await axios
        .get('/api/properties/get_images/' + this.propertyDetails.id)
        .then(response => {
        this.propertyImages = response.data
        })
        .catch(error => {
          console.log("error: " +error)
        })

      console.log(this.properties)
      this.$store.commit('setIsLoading', false)
    },

    getContentImageLink(link) {
      return "http://127.0.0.1:8000/" + link
    }
  }
}

</script>

<style scoped>
.property-text-border{
    border-left: 2px solid;
}
.jumbotron {
  padding: 2rem 1rem;
  margin-bottom: 2rem;
  background-color: #e9ecef;
  border-radius: .3rem;
}
</style>


<!--  <property-card-wrapper>-->
<!--    <div class="container ">-->
<!--      <div id="carouselExampleIndicators" class="carousel slide carousel-styling " data-bs-ride="carousel">-->
<!--        <div class="carousel-indicators ">-->
<!--             {% for image in property.images.all %}-->
<!--            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="{{forloop.counter0}}" class="{% if forloop.counter0 == 0 %}active{% endif %}" aria-current="true" aria-label="Slide 1"></button>-->
<!--            {% endfor %}-->
<!--        </div>-->
<!--        <div class="carousel-inner property-image">-->
<!--          {% for pic in property.images.all %}-->

<!--                 <div class="carousel-item {% if forloop.counter0 == 0 %}active{% endif %}" data-interval="5000">-->

<!--                    <img src="#" class="d-block w-100" alt="#">-->
<!--                </div>-->
<!--            {% endfor %}-->
<!--        </div>-->

<!--        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">-->
<!--              <span class="carousel-control-prev-icon" aria-hidden="true"></span>-->
<!--              <span class="visually">Previous</span>-->
<!--        </button>-->
<!--        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">-->
<!--            <span class="carousel-control-next-icon" aria-hidden="true"></span>-->
<!--            <span class="visually">Next</span>-->
<!--        </button>-->
<!--      </div>-->
<!--    </div>-->


<!--    <div class="container">-->
<!--    <div class="row text-center">-->
<!--        <div class="col-6 col-md-3 p-2">-->
<!--            <dt>RENT</dt>-->
<!--            <dd> ${{ rent }}</dd>-->
<!--        </div>-->
<!--        <div class="col-6 col-md-3 p-2 property-text-border">-->
<!--            <dt>Bed / Bath</dt>-->
<!--            <dd> {{ bed }} / {{ bath }}</dd>-->
<!--        </div>-->
<!--        <div class="col-6 col-md-3 p-2 property-text-border">-->
<!--            <dt>Square Foot</dt>-->
<!--            <dd> {{ sq }}</dd>-->
<!--        </div>-->
<!--        <div class="col-6 col-md-3 p-2 property-text-border">-->
<!--            <dt>Available On</dt>-->
<!--            <dd> {{ availableDate }}</dd>-->
<!--        </div>-->
<!--    </div>-->
<!--    <div class="row">-->
<!--        <div class="col-lg-12">-->
<!--        </div>-->
<!--    </div>-->
<!--    <div class="row mt-4">-->
<!--        <p style="white-space: pre-wrap;" >Description: {{ description }}</p>-->
<!--    </div>-->

<!--</div>-->



<!--  </property-card-wrapper>-->






<!-- <b-carousel-->
<!--      id="carousel-1"-->
<!--      v-model="slide"-->
<!--      :interval="4000"-->
<!--      controls-->
<!--      indicators-->

<!--      style="text-shadow: 1px 1px 2px #333;"-->
<!--      @sliding-start="onSlideStart"-->
<!--      @sliding-end="onSlideEnd"></b-carousel>-->

<!--        <b-carousel-slide-->
<!--            v-for="prop in propertyImages"-->
<!--            :key="prop.id"-->
<!--            :img-src="getContentImageLink(prop.image)">-->

<!--&lt;!&ndash;          <h1>Hello world!</h1>&ndash;&gt;-->
<!--        </b-carousel-slide>-->
