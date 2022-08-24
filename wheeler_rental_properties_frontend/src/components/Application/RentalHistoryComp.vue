<template>
  <div class="container">
    <div class='row'>
      <div class="col-md-4">
        <form-kit type="text" name="applicantAddress"  label="Address" validation="required|text" />
      </div>
      <div class="col-md-4">
        <form-kit type='date' name="moveInDate" label="Move-in Date" validation="required|date" />
      </div>
      <div class="col-md-4">
        <form-kit type='date' name="moveOutDate" label="Move-out Date" validation="required|date" />
      </div>
    </div>
    <div class='row' >
      <div class="col-md-4">
        <form-kit type="text" name="rentalHistoryCity"  label="City" validation="required|text" />
      </div>
      <div class="col-md-4">
        <form-kit  type="select" :options='states' placeholder='Select your state' label="State" validation="required" />
      </div>
      <div class="col-md-4">
        <form-kit type="number" name="rentalHistoryZip" label="Zip" validation="required|number|length:5" />
      </div>
    </div>
    <div class='row'>
      <div class="col-md-4">
        <form-kit type="text" name="rentalHistoryLandlord"  label="Landlord/Property Manager" validation="required|text" />
      </div>
      <div class="col-md-4">
        <form-kit type="number" name="rentalHistoryLandLordPhone" placeholder='999999999' label="Landlord/Property Manager Phone Number" validation="required|number|length:5" />
      </div>
      <div class="col-md-4">
        <form-kit type="number" name="rentalHistoryRent" label="Rent" validation="required|number" />
      </div>
    </div>

  </div>
</template>

<script>
import {FormKit} from "@formkit/vue/index";
export default {
  name: "RentalHistoryComp",
  components: {FormKit},
  props: ['states'],
}
</script>

<style>
.full-width {
  width: 100%;
}
</style>