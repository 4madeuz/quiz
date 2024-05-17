<template>
    <ul class="layout-menu">
      <template v-for="(item, i) in modelWithPermissions" :key="i">
        <app-menu-item v-if="!item.separator" :item="item" :index="i"></app-menu-item>
        <li v-if="item.separator" class="menu-separator"></li>
      </template>
    </ul>
</template>

<script setup>
import { computed, ref } from 'vue';
import { useStore } from 'vuex';
import AppMenuItem from './AppMenuItem.vue';

const store = useStore();
const user = computed(() => store.getters.stateUser);

const model = [
  {
    label: 'Меню',
    items: [
      { label: 'Опросы', icon: 'pi pi-fw pi-home', to: '/surveys' },
      { label: 'Результаты', icon: 'pi pi-fw pi-home', to: '/results', adminOnly: true }, // добавляем флаг adminOnly
      { label: 'Результаты Пользователя', icon: 'pi pi-fw pi-home', to: '/user/self/results', userOnly: true },
    ],
  },
];

// Фильтруем модель на основе прав доступа пользователя
const modelWithPermissions = computed(() => {
  // Копируем модель, чтобы не изменять исходную
  const filteredModel = JSON.parse(JSON.stringify(model));
  
  // Если пользователь не администратор, удаляем элементы, доступные только для администраторов
  if (!user.value.is_admin) {
    filteredModel.forEach(menu => {
      menu.items = menu.items.filter(item => !item.adminOnly);
    });
  }
  if (user.value.is_admin) {
    filteredModel.forEach(menu => {
      menu.items = menu.items.filter(item => !item.userOnly);
    });
  }

  return filteredModel;
});
</script>   

<style lang="scss" scoped></style>
