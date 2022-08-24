<template>
<!--  Image section-->
    <div class="col-lg-5 verticalLine">
       <router-link :to="{name: 'propertyDetails', params: {
         slug: property.slug,
       }}">
        <img class="prop-image-scale" :src="getContentImageLink(property.thumbnail)" alt="{{ property.thumbnail_alt }}">
       </router-link>
    </div>

<!--    body section-->
    <div class="col-lg-7 property-details">
      <div class="row text-center property-text-line">
        <div class="col-6 col-md-3 p-2">
            <dt>RENT</dt>
            <dd> ${{ property.rent }}</dd>
        </div>
        <div class="col-6 col-md-3 p-2 property-text-border">
            <dt>Bed / Bath</dt>
            <dd> {{ property.bedrooms }} / {{ property.bathrooms }}</dd>
        </div>
        <div class="col-6 col-md-3 p-2 property-text-border">
            <dt>Square Foot</dt>
            <dd> {{ property.sq_foot }}</dd>
        </div>
        <div class="col-6 col-md-3 p-2 property-text-border">
            <dt>Available On</dt>
            <dd> {{ property.available_date }}</dd>
        </div>
      </div>
        <div class="row property-title">
        <p class="property-title-text">{{ property.property_title }}</p>
        <p class="property-address-text">{{ property.property_num }} {{property.property_road}}, {{ property.city }}, {{ property.state }} {{ property.zip }}</p>

      </div>
        <div class="row prop-short-desc">
          {{ property.property_short_description}}
        </div>
    </div>
</template>

<script>

export default {
  name: "PropertyCard",
  props: ['property'],
  data() {
    return{

    }
  },
  methods: {
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

.property-detail-card{
    background-color: #ececec;
    padding: 10px;
    border-radius: 15px;
    border: solid 2px;
}


.property-details{
    padding-left: 20px;
    /*background-color: #06BEE1;*/
}
.property-title-text{
    display: block;
    font-size: 1.24em;
    /*margin: 1.67em 0;*/
    font-weight: bold;
}
.property-address-text{
    display: block;
    font-size: .95em;
    /*margin: 1.67em 0;*/
    font-weight: 600;
}
.property-address{
    text-align: center;
}
/*.carousel-styling{*/
/*    background-color: white;*/
/*}*/
.container-max-width{
    width: 90%;
}
.property-text-line{
    border-bottom: 2px solid;
    padding-bottom: 5px;
}
.property-title{
    padding-top: 10px

}
.property-image{
    border-radius: 15px;
    background-color: #ececec
}
.prop-short-desc{
    padding-left: 20px;
}
.property_header{
    font-family: 'Alex Brush', cursive;
    text-align: justify;
    font-size: 4em

}

.spacing_test{
    line-height: .1;
}


img {
    max-width:100%;
    max-height:100%;
}
.image-main-section{
    margin-bottom:20px;
}
.img-part{
    border-radius: 5px;
    margin:0;
    border:1px solid #DDDDDD;
    background-color: #fff;
    padding-bottom: 20px;
}
.img-section{
    padding: 5px;
}
.img-section img{
    width: 100%;
}
.image-title h3{
    margin:0px;
    color:#4C4C4C;
    padding: 7px 0px 7px 0px;
    text-align: center;
}
.image-description p{
    color:#848484;
}
.add-cart-btn{
    border-radius:0px;
    font-size: 11px;
}
.prop-image-scale{
    /*height: 100%;*/
    width: 100%;
    object-fit: cover;
    border-radius: 15px;
}

.container-equal-height{
    grid-auto-rows: 1fr;
}
.jumbotron {
  padding: 2rem 1rem;
  margin-bottom: 2rem;
  background-color: #e9ecef;
  border-radius: .3rem;
}
</style>





<!--          <div class="row prop-short-desc">-->
<!--             <p>{{ property.property_short_description}}</p>-->
<!--          </div>-->

<!--&lt;!&ndash;              {# buttons #}&ndash;&gt;-->
<!--          <div class="row">-->
<!--              <div class="col">-->
<!--                <a href="{% url 'base:property_details' slug=property.slug %}" class="btn btn-primary add-cart-btn">View Property</a>-->
<!--                <a href="{% url 'base:property_details' slug=property.slug %}" class="btn btn-primary add-cart-btn centered">View Property (not active)</a>-->
<!--              </div>-->
<!--          </div>-->
<!--      </div>-->
<!--  </div>-->
<!--  <div class="row main-section property-card property-shadow my-3">-->
<!--&lt;!&ndash;      {# Thumbnail section#}&ndash;&gt;-->

<!--&lt;!&ndash;          {# Details section#}&ndash;&gt;-->
<!--      <div class="col-lg-7 property-details">-->
<!--          <div class="row text-center property-text-line">-->
<!--              <div class="col-6 col-md-3 p-2">-->
<!--                  <dt>RENT</dt>-->
<!--                  <dd> ${{ property.rent }}</dd>-->
<!--              </div>-->
<!--              <div class="col-6 col-md-3 p-2 property-text-border">-->
<!--                  <dt>Bed / Bath</dt>-->
<!--                  <dd> {{ property.bedrooms }} / {{ property.bathrooms }}</dd>-->
<!--              </div>-->
<!--              <div class="col-6 col-md-3 p-2 property-text-border">-->
<!--                  <dt>Square Foot</dt>-->
<!--                  <dd> {{ property.sq_foot }}</dd>-->
<!--              </div>-->
<!--              <div class="col-6 col-md-3 p-2 property-text-border">-->
<!--                  <dt>Available On</dt>-->
<!--                  <dd> {{ property.available_date }}</dd>-->
<!--              </div>-->
<!--          </div>-->
<!--          <div class="row property-title">-->
<!--              <p class="property-title-text">{{ property.property_title }}</p>-->
<!--{#                                    <h5 class="property-title-text">{{ property.property_title }}</h5>#}-->

<!--                  <p class="property-address-text">{{ property.address }}, {{ property.city }}, {{ property.state }} {{ property.zip }}</p>-->

<!--                  <p class="property-address-text">{{ property.address }}, {{ property.city }}, {{ property.state }} {{ property.zip }} (NOT ACTIVE)</p>-->

<!--          </div>-->
<!--          <div class="row prop-short-desc">-->
<!--             <p>{{ property.property_short_description}}</p>-->
<!--          </div>-->

<!--&lt;!&ndash;              {# buttons #}&ndash;&gt;-->
<!--          <div class="row">-->
<!--              <div class="col">-->
<!--                <a href="{% url 'base:property_details' slug=property.slug %}" class="btn btn-primary add-cart-btn">View Property</a>-->
<!--                <a href="{% url 'base:property_details' slug=property.slug %}" class="btn btn-primary add-cart-btn centered">View Property (not active)</a>-->
<!--              </div>-->
<!--          </div>-->
<!--      </div>-->
<!--  </div>-->