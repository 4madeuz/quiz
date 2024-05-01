import axios from 'axios';

const state = {
  results: [],
  result: null
};

const getters = {
  stateResults: state => state.results,
  stateResult: state => state.result,
};

const actions = {
  async createResult({dispatch}, result) {
    await axios.post('result', result);
    await dispatch('getResults');
  },
  async getResults({commit}) {
    let {data} = await axios.get('results');
    commit('setResults', data);
  },
  async viewResult({commit}, id) {
    let {data} = await axios.get(`results/${id}`);
    commit('setResult', data);
  },
  async getUserResults({commit}, user_id) {
    let {data} = await axios.get(`results/user/${user_id}`);
    commit('setResults', data);
  },
};

const mutations = {
  setResults(state, results){
    state.results = results;
  },
  setResult(state, result){
    state.result = result;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
