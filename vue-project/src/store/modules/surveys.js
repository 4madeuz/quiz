import axios from 'axios';

const state = {
  surveys: [],
  survey: null
};

const getters = {
  stateSurveys: state => state.surveys,
  stateSurvey: state => state.survey,
};

const actions = {
  async createSurvey({dispatch}, survey) {
    await axios.post('surveys', survey);
    await dispatch('getSurveys');
  },
  async getSurveys({commit}) {
    let {data} = await axios.get('surveys');
    commit('setSurveys', data);
  },
  async viewSurvey({commit}, id) {
    let {data} = await axios.get(`surveys/${id}`);
    commit('setSurvey', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateSurvey({}, survey) {
    await axios.patch(`surveys/${survey.id}`, survey.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteSurvey({}, id) {
    await axios.delete(`surveys/${id}`);
  }
};

const mutations = {
  setSurveys(state, surveys){
    state.surveys = surveys;
  },
  setSurvey(state, survey){
    state.survey = survey;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
