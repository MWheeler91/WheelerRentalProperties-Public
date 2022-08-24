<template>
  <div>
    <h1>Application Page</h1>
    <h1 class="text-center">Primary Applicant</h1>
    <hr>
    <div class="container">
      <card-wrapper>
        <form class="post-form p-3" method="POST" enctype="multipart/form-data" role="form">

          <div class="container pt-3 pb-5">
            <h1>Property Details</h1>
            <div class="row">
              <div class="col-md-6">
                <base-input v-model="propertyOptions"  label="Property" type="text" class="field" disabled/>
              </div>
              <div class="col-md-6">
                <base-input v-model="requestedMoveIn"  label="Requested Move-in Date" type="date" class="field" required/>
              </div>
            </div>
          </div>

          <div class="container pb-5">
            <h1>Personal Information</h1>
            <personal-information :states='stateOptions' :petOptions="petOptions" v-model="personalInformation"/>
          </div >


        </form>
     </card-wrapper>
    </div>
  <!--            <input type="submit" class="btn btn-primary">-->
  </div>
</template>

<script>
// import {FormKit} from "@formkit/vue/index";
// import RentalHistory from "@/components/Application/RentalHistoryComp";
// import IncomeComp from "@/components/Application/IncomeComp";
// import PersonalInformation from "@/components/Application/PersonalInformation";
// import CardWrapper from "@/components/Layout/CardWrapper";
// import axios from "axios";

import BaseInput from "@/components/UI/BaseInput";
import CardWrapper from "@/components/Layout/CardWrapper";
import PersonalInformation from "@/components/Application/PersonalInformation";

export default {
  name: "ApplicationPage",
  components: { PersonalInformation, CardWrapper, BaseInput},
  // components: {CardWrapper, PersonalInformation, RentalHistory, IncomeComp, FormKit},
  props: {

  },
  data () {
    return {
      propertyOptions: "",
      personalInformation: {
        first_name: "",
        middle_name: "",
        last_name: "",
        date_of_birth: "",
        phone: null,
        email: "",
        pets: false,
        driver_license: null,
        driver_license_state: "",
        number_of_pets: null
      },
      fromPropertyPage: false,
      petOptions: ['No', 'Yes'],
      stateOptions: ['Alabama','Alaska','American Samoa','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District of Columbia','Federated States of Micronesia','Florida','Georgia','Guam','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Marshall Islands','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Northern Mariana Islands','Ohio','Oklahoma','Oregon','Palau','Pennsylvania','Puerto Rico','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virgin Island','Virginia','Washington','West Virginia','Wisconsin','Wyoming'],
      requestedMoveIn: null
    }
  },
  created() {
    this.checkFrom()
  },
  methods: {
    checkFrom() {
      if (this.$route.params.id){
        console.log(this.$route.params.address)
        this.fromPropertyPage = true
        this.propertyOptions = this.$route.params.address
      }
    }
  }
}


</script>

<style scoped>


</style>



<!-- <card-wrapper>-->
<!--        <form-kit type="form" submit-label="Submit" method="post">-->
<!--          <div class="container">-->
<!--            <h2>Property Details</h2>-->
<!--              <div class="row row justify-content-evenly">-->
<!--                <div class="col-md-6 ">-->
<!--                  <form-kit type='text' outer-class="row justify-content-evenly full-width" :value='propertyOptions' readonly="true" placeholder="Select a property" name="property" label="Property" validation="required|select" />-->
<!--                </div>-->
<!--                <div class="col-md-6 ">-->
<!--                  <form-kit  type='date' outer-class="row justify-content-evenly full-width" name="requestMoveInDate" label="Requested Move-in Date" validation="required|date" />-->
<!--                </div>-->
<!--              </div>`-->
<!--            </div>-->
<!--          <div>-->
<!--            <h2>Persoanl Information</h2>-->
<!--            <personal-information :states='stateOptions' :petOptions="petOptions" />-->
<!--          </div>-->

<!--          <div>-->
<!--            <h2 class="pt-3">Rental History</h2>-->
<!--            <rental-history :states='stateOptions' />-->
<!--          </div>-->
<!--          <div>-->
<!--            <h2 class="pt-3">Income</h2>-->
<!--            <income-comp :states='stateOptions'/>-->
<!--          </div>-->
<!--          <div class='row'>-->
<!--            <div class="col-md-12">-->
<!--              <div class="flex-fill bd-highlight full-width">-->
<!--                <form-kit type="textarea" rows="10" col="10000" outer-class="row justify-content-evenly " name="additionalComments" label="Additonal Comments"  />-->

<!--              </div>-->
<!--            </div>-->
<!--          </div>-->
<!--      </form-kit>-->
<!--      </card-wrapper>-->