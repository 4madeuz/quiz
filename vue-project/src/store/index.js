import { createStore } from "vuex";

import surveys from './modules/surveys';
import users from './modules/users';
import results from './modules/results';

export default createStore({
  modules: {
    surveys,
    users,
    results,
  }
});
