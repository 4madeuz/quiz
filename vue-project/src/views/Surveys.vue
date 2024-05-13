<script>
import { mapGetters, mapActions } from 'vuex';
import axios from 'axios';

export default {
  name: 'Surveys',
  created() {
    this.getSurveys(); // Dispatch action to get surveys
  },
  computed: {
    ...mapGetters({ surveys: 'stateSurveys', user: 'stateUser'}),
  },
  methods: {
    ...mapActions(['getSurveys']), // Map getSurveys action
    async Publish(id) {
      try {
        await axios.post(`/surveys/publish/${id}`);
        this.getSurveys();
      } catch (error) {
        console.error('Error while redirecting to login:', error);
      }
    },
  },
};

</script>



<template>
  <div class="card">
    <h5>Опросы</h5>
    <DataTable
        :value="surveys"
        :paginator="true"
        :rows="15"
        dataKey="id"
        :rowHover="true"
        v-model:filters="filters1"
        filterDisplay="menu"
        :loading="loading1"
        :filters="filters1"
        showGridlines
    >
        <template #empty> Ничего не найдено. </template>
        <template #loading> Загрузка опросов, подождите. </template>
        <Column field="name" header="Название" style="min-width: 12rem">
            <template #body="{ data }">
              <router-link :to="{name: 'Survey', params:{id: data.id}}">{{ data.title }}</router-link>
            </template>
        </Column>
        <Column field="name" header="ID" style="min-width: 12rem">
            <template #body="{ data }">
                {{ data.id }}
            </template>
        </Column>
        <Column v-if="user.is_admin" field="name" header="Статус" style="min-width: 12rem">
            <template #body="{ data }">
                {{ data.published }}
            </template>
        </Column>
        <Column v-if="user.is_admin" headerStyle="min-width:10rem;" header="Поменять статус">
          <template #body="{ data }">
              <Button icon="pi pi-pencil" class="mr-2" severity="success" rounded @click="Publish(data.id)" />
          </template>
      </Column>
    </DataTable>
  </div>
</template>