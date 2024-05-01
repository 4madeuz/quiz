<script setup lang="ts">
import 'survey-core/defaultV2.min.css';
import { Model } from 'survey-core';


const surveyJson = {
    title: "American History",
    showProgressBar: "bottom",
    showTimerPanel: "top",
    maxTimeToFinishPage: 60,
    maxTimeToFinish: 300,
    firstPageIsStarted: true,
    startSurveyText: "Начать тестирование",
    pages: [{
        elements: [{
            type: "html",
            html: "Вопросы для тестирования пользователя"
        },]
    }, {
        elements: [{
            type: "radiogroup",
            name: "civilwar",
            title: "Что следует делать, если вам приходит подозрительное электронное письмо, запрашивающее личные данные?",
            choices: [
                "Отправить свои данные для проверки", "Изучить содержание письма и проверить адрес отправителя", "Напечатать и отправить в службу поддержки", "Проигнорировать письмо"
            ],
            correctAnswer: "Изучить содержание письма и проверить адрес отправителя"
        }]
    }, {
        elements: [{
            type: "radiogroup",
            name: "libertyordeath",
            title: "Какие действия следует предпринять, чтобы защитить себя от социальной инженерии?",
            choicesOrder: "random",
            choices: [
                "Передавать личные данные по телефону", "Проверять подлинность источника запроса информации", "Отправлять личные данные на любые запросы", "Раскрывать личные секреты"
            ],
            correctAnswer: "Проверять подлинность источника запроса информации"
        }]
    }, {
        elements: [{
            type: "radiogroup",
            name: "magnacarta",
            title: "Что следует делать, если вам приходит подозрительное SMS-сообщение с просьбой предоставить личные данные?",
            choicesOrder: "random",
            choices: [
                "Немедленно отправить запрашиваемую информацию",
                "Поделиться сообщением со всеми друзьями",
                "Проигнорировать сообщение и удалить его",
                "Тщательно изучить содержание сообщения и проверить номер отправителя"
            ],
            correctAnswer: "Тщательно изучить содержание сообщения и проверить номер отправителя"
        }]
    }, {
        elements: [{
            type: "radiogroup",
            name: "magnacartasd",
            title: "Какие меры предосторожности стоит предпринять при обнаружении подозрительной активности на своем онлайн аккаунте?",
            choicesOrder: "random",
            choices: [
                "Поделиться личными данными с неизвестными пользователями",
                "Сохранить все данные на устройстве",
                "Изменить пароль и уведомить службу поддержки",
                "Продолжить использование аккаунта как обычно"
            ],
            correctAnswer: "Изменить пароль и уведомить службу поддержки"
        }]
    }, {
        elements: [{
            type: "radiogroup",
            name: "magnacartadd",
            title: "Что следует делать, если вам приходит электронное письмо из Вуза, требующее скачать новую программу для обучения?",
            choicesOrder: "random",
            choices: [
                "Проверить адрес отправителя и убедиться, что это действительно официальный адрес электронной почты учебного заведения.",
                "Связаться с администрацией университета для подтверждения подлинности письма и новой программы обучения.",
                "Не следует скачивать программное обеспечение немедленно, а лучше провести дополнительные проверки на наличие вирусов и шпионского ПО.",
                "В случае сомнений или если что-то кажется подозрительным, лучше обратиться к специалисту по информационной безопасности для консультации."
            ],
            correctAnswer: "Связаться с администрацией университета для подтверждения подлинности письма и новой программы обучения."
        }]
    }],
    completedHtml: "<h4>You got <b>{correctAnswers}</b> out of <b>{questionCount}</b> correct answers.</h4>",
    completedHtmlOnCondition: [{
        expression: "{correctAnswers} == 0",
        html: "<h4>Unfortunately, none of your answers are correct. Please try again.</h4>"
    }, {
        expression: "{correctAnswers} == {questionCount}",
        html: "<h4>Congratulations! You answered all the questions correctly!</h4>"
    }]
};

const survey = new Model(surveyJson);
survey.onComplete.add((sender, options) => {
        console.log(JSON.stringify(sender.data, null, 3));
    });
</script>

<template>
    <SurveyComponent :model="survey" />
</template>