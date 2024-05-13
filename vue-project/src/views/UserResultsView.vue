<template>
    <div class="card">
      <h5>Результаты</h5>
      <DataTable
          :value="results"
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
          <template #loading> Загрузка результатов, подождите. </template>
          <Column field="name" header="Правильных ответов" style="min-width: 12rem">
              <template #body="{ data }">
                  {{ data.answers_amount }}
              </template>
          </Column>
          <Column field="name" header="Подробнее" style="min-width: 12rem">
              <template #body="{ data }">
                <router-link :to="{name: 'Result', params:{id: data.id}}">Рекомендации</router-link>
              </template>
          </Column>
          <Column field="name" header="Количество вопросов" style="min-width: 12rem">
              <template #body="{ data }">
                  {{ data.survey_len }}
              </template>
          </Column>
          <Column field="name" header="Дата прохождения" style="min-width: 12rem">
                <template #body="{ data }">
                    {{ removeTimezone(data.created_at) }}
                </template>
            </Column>
          <Column field="name" header="Анкетирование" style="min-width: 12rem">
              <template #body="{ data }">
                <router-link :to="{name: 'Survey', params:{id: data.survey.id}}">{{ data.survey.title }}</router-link>
              </template>
          </Column>
          <Column field="name" header="Пользователь" style="min-width: 12rem">
            <template #body="{ data }">
                  {{ data.user.username }}
              </template>
          </Column>
      </DataTable>
    </div>
</template>
  
<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
name: 'UserResults',
async created() {
    try {
    await this.viewMe();
    await this.getUserResults(this.user.id);
    } catch (error) {
    console.error(error);
    //this.$router.push('/surveys');
    }
},
computed: {
    ...mapGetters({ results: 'stateResults', user: 'stateUser'}),
},
methods: {
    ...mapActions(['getUserResults', 'viewMe']),
    removeTimezone(created_at) {
            const date = new Date(created_at);
            return date.toLocaleString('ru-RU', { timeZone: 'UTC' });
        }
},
});
</script>
  