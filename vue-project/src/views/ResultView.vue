<template>
  <div v-if="result">
    <div v-for="(item, index) in result.recomendations" :key="index">
      <Card style="margin-bottom: 10px;">
        <template #title>{{ item.title }}</template>
        <template #content>
          <p> {{ item.recomendation }}</p>
        </template>
      </Card>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'Result',
  props: ['id'],
  async created() {
    try {
      await this.viewResult(this.id);
    } catch (error) {
      console.error(error);
      this.$router.push('/surveys');
    }
  },
  computed: {
    ...mapGetters({ result: 'stateResult', user: 'stateUser'}),
  },
  methods: {
    ...mapActions(['viewResult']),
  },
});
</script>
