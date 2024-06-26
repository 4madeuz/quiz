import axios from 'axios';

const state = {
  user: null,
};

const getters = {
  isAuthenticated: state => !!state.user,
  stateUser: state => state.user,
};

const actions = {
  async register({ dispatch }, form) {
    try {
      const response = await fetch('http://127.0.0.1:8000/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(form),
      });
      return response
    } catch (error) {
      console.error('Fetch error:', error);
      return response
    }
  },
  async logIn({ dispatch }, user) {
    try {
      let UserForm = new FormData();
      UserForm.append('username', user.username);
      UserForm.append('password', user.password);

      const response = await axios.post('auth/login', UserForm); // Убедитесь, что URL правильный
      if (response.status === 200) {
        await dispatch('viewMe');
      } else {
        console.error('Login failed:', response.statusText);
        throw new Error('Login failed');
      }
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  },
  async viewMe({commit}) {
    let {data} = await axios.get('auth/me');
    await commit('setUser', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteUser({}, id) {
    await axios.delete(`user/${id}`);
  },
  async logOut({commit}) {
    let user = null;
    commit('logout', user);
  }
};

const mutations = {
  setUser(state, username) {
    state.user = username;
  },
  logout(state, user){
    state.user = user;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
