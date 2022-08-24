<template>
  <div class="container">
    <div class='row'>
      <div class="col-md-4">
        <form-kit type="text" name="incomeEmployer"  label="Employer" validation="required|text" />
      </div>
      <div class="col-md-4">
        <form-kit type='text' name="incomeJobTitle" label="Job Title" validation="required|date" />
      </div>
      <div class="col-md-4">
        <form-kit type="text" name="IncomeAddress"  label="Address" validation="required|text" />
      </div>
    </div>
    <div class='row' >
      <div class="col-md-4">
        <form-kit type="text" name="incomeCity"  label="City" validation="required|text" />
      </div>
      <div class="col-md-4">
        <form-kit  type="select" :options='states'  name='incomeState' placeholder='Select your state' label="State" validation="required" />
      </div>
      <div class="col-md-4">
        <form-kit type="number" name="IncomeZip" label="Zip" validation="required|number|length:5" />
      </div>
    </div>
    <div class='row'>
      <div class="col-md-4">
        <form-kit type="text" name="incomeSupervisor"  label="Supervisor" validation="required|text" />
      </div>
      <div class="col-md-4">
        <form-kit type="date" name="incomeStartDate"  label="Start Date" validation="required|date" />
      </div>
      <div class="col-md-4">
        <form-kit type="number" name="incomeGrossMonthlyIncome" label="Gross Monthly Income" validation="required|number" />
      </div>
    </div>
<!--    <div class='row'>-->
      <div class="">
        <form-kit
            type="file"
            label="PayStubs / Tax Returns"
            accept=".pdf,.doc,.docx,.xml,.md,.csv"
            name="incomeDocuments"
            help=".pdf,.doc,.docx,.xml,.md,.csv format only."
            multiple
        />
      </div>
<!--    </div>-->
  </div>

</template>

<script>
import {FormKit} from "@formkit/vue/index";

export default {
  name: "IncomeComp",
  components: {FormKit},
  props: ['states'],
}
</script>

<style scoped>

</style>