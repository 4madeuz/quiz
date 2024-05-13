<template>
    <div class="surface-ground flex align-items-center  min-h-screen min-w-screen overflow-hidden">
        <div class="flex flex-column align-items-center justify-content-center">
            <img :src="logoUrl" alt="Sakai logo" class="mb-5 w-6rem flex-shrink-0" />
            <div style="border-radius: 56px; padding: 0.3rem; background: linear-gradient(180deg, var(--primary-color) 10%, rgba(33, 150, 243, 0) 30%)">
                <div class="w-full surface-card py-8 px-5 sm:px-8" style="border-radius: 53px">
                    <div class="text-center mb-5">
                        <div class="text-900 text-3xl font-medium mb-3">Регистрация</div>
                        <span class="text-600 font-medium">Введите данные пользователя</span>
                    </div>
                    <div>
                        <label for="email1" class="block text-900 text-xl font-medium mb-2">Электронная почта</label>
                        <InputText id="email1" type="text" placeholder="user@mail.ru" class="w-full md:w-30rem mb-5" style="padding: 1rem" v-model="email" />
                        <label for="username" class="block text-900 text-xl font-medium mb-2">Имя пользователя</label>
                        <InputText id="username" type="text" placeholder="Username" class="w-full md:w-30rem mb-5" style="padding: 1rem" v-model="username" />
                        <label for="password1" class="block text-900 font-medium text-xl mb-2">Пароль</label>
                        <Password id="password1" v-model="password" placeholder="Password" :toggleMask="true" class="w-full mb-3" inputClass="w-full" :inputStyle="{ padding: '1rem' }"></Password>
                        <div class="flex align-items-center justify-content-between mb-5 gap-5">
                            <div class="flex align-items-center">
                                <Checkbox v-model="isAdmin" id="is_admin" binary class="mr-2"></Checkbox>
                                <label for="rememberme1">Администратор</label>
                            </div>
                        </div>
                        <Button label="Зарегистрироваться" class="w-full p-3 text-xl" @click="register"></Button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useLayout } from '@/layout/composables/layout';
import { ref, computed } from 'vue';
import AppConfig from '@/layout/AppConfig.vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import axios from 'axios';

const store = useStore();
const router = useRouter();
const { layoutConfig } = useLayout();
const email = ref('');
const password = ref('');
const checked = ref(false);
const isAdmin = ref(false);
const username = ref('');

const logoUrl = computed(() => {
    return `/layout/images/${layoutConfig.darkTheme.value ? 'logo-white' : 'logo-dark'}.svg`;
});



const register = async () => {
    try {
        await store.dispatch('register', { email: email.value, password: password.value, is_admin: isAdmin.value, username: username.value });
        // Redirect or show success message
    } catch (error) {
        console.error('Registration error:', error);
        // Show error message
    }
    router.push('/auth/login');
};
</script>

<style scoped>
.pi-eye {
    transform: scale(1.6);
    margin-right: 1rem;
}

.pi-eye-slash {
    transform: scale(1.6);
    margin-right: 1rem;
}
</style>