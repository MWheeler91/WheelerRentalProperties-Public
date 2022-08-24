<template>
  <label class="form-label">{{ label }}</label>
  <input
    v-bind="$attrs"
    :placeholder="placeholder"
    class="field form-control"
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
  />
</template>

<script>
export default {
  name: "BaseInput",
  props: {
    label: {
      type: String,
      default: ""
    },
    modelValue: {
      type: [String, Number],
      default: ""
    },
    placeholder: {
      type: [String, Number],
      default: ""
    }
  }
}
</script>

<style scoped>

</style>