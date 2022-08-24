<template>
<!--  <div class="container">-->

    <div class="row">
      <div class="col-md-4">
<!--        <form-kit type='text' name="firstName" label="First Name" validation="required|text" />-->
        <base-input v-model="personalInformation.first_name" label="First Name" type="text" class="field" required/>
      </div>
      <div class="col-md-4">
        <form-kit type='text' name="middleName" label="Middle Name" validation="text" />
      </div>
      <div class="col-md-4">
        <form-kit type='text' name="lastName" label="Last Name" validation="required|text" />
      </div>
    </div>
    <div class="row">
      <div class="col-md-4">
        <form-kit type='date' name="dateOfBirth" label="Date of Birth" validation="required|date" />
      </div>
      <div class="col-md-4">
        <form-kit type="number" name="applicantPhone"  placeholder='999999999'  label="Phone" validation="required|text" />
      </div>
      <div class="col-md-4">
        <form-kit type="email" name="applicantEmail" label="Email" validation="required|email" />
      </div>
    </div>
    <div class="row">
      <div class="col-md-3">
        <form-kit type="select" :options='petOptions' name="applicantPets" label="Pets"/>
      </div>
      <div class="col-md-3">
        <form-kit type="number" name="numberOfPets" label="Number of Pets" validation="required|number" />
      </div>
      <div class="col-md-3">
        <form-kit type="number" name="applicantDL" label="Driver License" validation="required|number" />
      </div>
      <div class="col-md-3">
        <form-kit type="select" :options='states' placeholder='Select your state' label="Driver License State" validation="required" />
      </div>
    </div>
<!--  </div>-->
</template>

<script>
import {FormKit} from "@formkit/vue/index";
import BaseInput from "@/components/UI/BaseInput";

export default {
  name: "PersonalInformation",
  components: {BaseInput, FormKit},
  // props: ['states', 'petOptions', 'personalInformation'],
  props: {
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
    states: {
      type: String
    },
    petOptions: {
      type: String
    }
  },
}
</script>

<style scoped>

</style>