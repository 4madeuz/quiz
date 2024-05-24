<template>
  <div v-if="survey">
    <div v-if="surveystest">
      <SurveyComponent :model="surveystest" />
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';
import 'survey-core/defaultV2.min.css';
import { Model } from 'survey-core';
import { surveyLocalization } from 'survey-core';
const customLocaleStrings = {
  pagePrevText: "Назад",
  pageNextText: "Далее",
  completeText: "Отправить"
};

surveyLocalization.locales["customlocale"] = customLocaleStrings;
import axios from 'axios';

export default defineComponent({
  name: 'Survey',
  props: ['id'],
  async created() {
    try {
      console.log(this.$route.params.id);
      await this.viewSurvey(this.$route.params.id);
      
      // Access the survey data and create the Model
      const surveyData = this.survey.survey_json;
      this.surveystest = new Model(surveyData);
      this.surveystest.locale = "customlocale";
      
      // Add onComplete event handler
      this.surveystest.onComplete.add(async (sender, options) => {
        // Send data to the server using Axios
        try {
          
          // Include both survey data and route params id in the payload
          const payload = {
            survey_id: this.$route.params.id,
            answers: sender.data,
          };

          const response = await axios.post('/results', payload);
          this.$router.push({name: 'Result', params:{id: response.data}});
        } catch (error) {
          console.error('Error sending data to server:', error);
        }
      });
    } catch (error) {
      console.error(error);
    }
  },
  computed: {
    ...mapGetters({ survey: 'stateSurvey'}),
  },
  methods: {
    ...mapActions(['viewSurvey']),
  },
  data() {
    return {
      surveystest: null
    };
  }
});
</script>
