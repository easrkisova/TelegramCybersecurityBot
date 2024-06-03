import telebot
from telebot import types
from random import choice

bot = telebot.TeleBot('7379188784:AAH4yhvUn3Sk9YGBU4syGU__wL4s8dlZ0zU')


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    hello_text = f'''Привет <b>{message.chat.first_name}</b>! 🌐

Интернет и социальные сети предоставляют нам огромные возможности для общения и обмена информацией, но вместе с этим несут и немало опасностей. Мошенничество, фишинговые атаки, кража личных данных — это лишь некоторые из угроз, с которыми можно столкнуться в сети. Очень важно знать, как защитить себя и свои данные от злоумышленников.

Этот бот создан, чтобы помочь вам узнать о лучших способах защиты конфиденциальной информации и безопасного общения в интернете. Следуйте нашим советам и рекомендациям, чтобы минимизировать риски и обезопасить свою цифровую жизнь.

Начните использовать нашего бота, чтобы получить полезные советы и рекомендации по безопасности в интернете! 🔒'''

    bot.send_message(message.chat.id, hello_text, reply_markup=main_mess_markup(), parse_mode='html')


@bot.message_handler(content_types=["text"])
def msg(message):
    if message.text == 'главное меню':
        main_win(message)
    else:
        bot.send_message(message.chat.id, '<b>Неизвестная команда</b>',
                         parse_mode='html')
        main_win(message)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    bot.answer_callback_query(callback.id)
    if callback.data == "Получить совет":
        bot.send_message(callback.message.chat.id, rand_adv(), parse_mode='html')
    elif callback.data == "Инструменты и рекомендации":
        bot.send_message(callback.message.chat.id, '<b>Вот список инструментов и рекомендаций:</b>',
                         parse_mode='html', reply_markup=markup_for_instr_and_rect())
    elif callback.data == "Рекомендации по VPN":
        send_vpn_recommendations(callback.message)
    elif callback.data == "Менеджеры паролей":
        send_password_manager_recommendations(callback.message)
    elif callback.data == "Антивирусные программы":
        send_antivirus_recommendations(callback.message)
    elif callback.data == "Браузеры и расширения":
        send_browser_recommendations(callback.message)
    elif callback.data == "Шифрование данных":
        send_encryption_recommendations(callback.message)
    elif callback.data == "Часто задаваемые вопросы (FAQ)":
        send_faq(callback.message)
    elif callback.data == "Полезные ресурсы и ссылки":
        send_usefull_sources(callback.message)
    else:
        send_faq_answer(callback)


def send_usefull_sources(message):
    text = '''<b>Вот парочка полезный статей на эту тему</b>
    Максимальная защита в Интернете - https://habr.com/ru/articles/552126/
    
        Анализ способов и методов незаконного распространения личных данных пользователей мессенджеров, социальных сетей и поисковых систем - https://cyberleninka.ru/article/n/analiz-sposobov-i-metodov-nezakonnogo-rasprostraneniya-lichnyh-dannyh-polzovateley-messendzherov-sotsialnyh-setey-i-poiskovyh-sistem
    
    Как избежать кражи персональных данных в социальных сетях? - https://www.keepersecurity.com/blog/ru/2023/12/01/how-to-avoid-social-media-identity-theft/'''
    bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=main_mess_markup())


def send_vpn_recommendations(message):
    text = '''<b>Рекомендации по VPN:</b>

<b>NordVPN</b>: Один из самых популярных VPN-сервисов с высокой степенью шифрования и множеством серверов по всему миру.
<b>ExpressVPN</b>: Обеспечивает быструю и надежную защиту, легко настраивается и используется на разных устройствах.
<b>CyberGhost</b>: Отличный вариант для начинающих, предлагает интуитивно понятный интерфейс и хорошие функции безопасности.'''
    bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=main_mess_markup())


def send_password_manager_recommendations(message):
    text = '''<b>Рекомендации по менеджерам паролей:</b>

<b>LastPass</b>: Удобный менеджер паролей, который генерирует и сохраняет сложные пароли, а также синхронизируется на всех ваших устройствах.
<b>1Password</b>: Предлагает надежное хранение паролей и других конфиденциальных данных, а также интеграцию с различными приложениями и браузерами.
<b>Bitwarden</b>: Бесплатный и открытый менеджер паролей с высокими стандартами безопасности.'''
    bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=main_mess_markup())


def send_antivirus_recommendations(message):
    text = '''<b>Рекомендации по антивирусным программам:</b>

<b>Kaspersky</b>: Надежная защита от вирусов, троянов и других вредоносных программ, а также инструменты для защиты конфиденциальности.
<b>Bitdefender</b>: Обеспечивает высокую степень защиты и включает дополнительные функции, такие как VPN и менеджер паролей.
<b>Norton</b>: Комплексная защита от вредоносных программ, фишинга и других угроз, а также функции для защиты конфиденциальных данных.'''
    bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=main_mess_markup())


def send_browser_recommendations(message):
    text = '''<b>Рекомендации по браузерам и расширениям:</b>

<b>Mozilla Firefox</b>: Браузер с акцентом на конфиденциальность, поддерживает множество расширений для повышения безопасности.
<b>Brave</b>: Быстрый и защищенный браузер с встроенным блокировщиком рекламы и трекеров.
<b>uBlock Origin</b>: Расширение для блокировки рекламы и трекеров, совместимое с большинством браузеров.'''
    bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=main_mess_markup())


def send_encryption_recommendations(message):
    text = '''<b>Рекомендации по шифрованию данных:</b>

<b>VeraCrypt</b>: Бесплатное программное обеспечение для шифрования данных, обеспечивает надежную защиту файлов и дисков.
<b>BitLocker</b>: Встроенный в Windows инструмент для шифрования дисков, простой в использовании и эффективный.'''
    bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=main_mess_markup())


def send_faq(message):
    markup = types.InlineKeyboardMarkup()
    faq_list = ['Что такое фишинг?', 'Как защититься от вирусов?', 'Двухфакторная аутентификация это?',
                'Как создать надежный пароль?', 'Почему важны обновления?']
    for question in faq_list:
        markup.add(types.InlineKeyboardButton(question, callback_data=question))
    bot.send_message(message.chat.id, 'Выберите вопрос, чтобы получить ответ:', reply_markup=markup, parse_mode='html')


def send_faq_answer(callback):
    faq_answers = {
        'Что такое фишинг?': '<b>Фишинг</b> — это метод мошенничества, при котором злоумышленники пытаются получить конфиденциальную информацию (пароли, данные кредитных карт) под видом надежного источника.',
        'Как защититься от вирусов?': '<b>Для защиты от вирусов</b> используйте надежное антивирусное ПО, не открывайте подозрительные вложения в письмах и не переходите по сомнительным ссылкам.',
        'Двухфакторная аутентификация это?': '<b>Двухфакторная аутентификация (2FA)</b> — это метод защиты, который требует два шага для подтверждения вашей личности: обычно пароль и код из SMS или приложения.',
        'Как создать надежный пароль?': '<b>Надежный пароль</b> должен содержать буквы разных регистров, цифры и специальные символы. Избегайте использования личной информации и общих слов.',
        'Почему важны обновления?': '<b>Обновления</b> важны, потому что они содержат исправления безопасности и новые функции, которые помогают защитить ваши данные от новых угроз.'
    }
    answer = faq_answers.get(callback.data, 'Извините, я не могу найти ответ на этот вопрос.')
    bot.send_message(callback.message.chat.id, answer, parse_mode='html', reply_markup=main_mess_markup())


def markup_for_instr_and_rect():
    markup = types.InlineKeyboardMarkup()
    markup_list = ['Рекомендации по VPN', 'Менеджеры паролей',
                   'Антивирусные программы', 'Браузеры и расширения', 'Шифрование данных']
    for mark_text in markup_list:
        markup.add(types.InlineKeyboardButton(mark_text, callback_data=mark_text))
    return markup


def main_mess_markup():
    markup = types.InlineKeyboardMarkup()
    markup_list = ['Получить совет', 'Инструменты и рекомендации', "Полезные ресурсы и ссылки"
                   'Часто задаваемые вопросы (FAQ)']
    for mark_text in markup_list:
        button = types.InlineKeyboardButton(mark_text, callback_data=mark_text)
        markup.add(button)
    return markup


def rand_adv():
    advList = [
        '<b>Используйте энд-то-энд шифрование</b>\nУбедитесь, что используемые вами мессенджеры поддерживают энд-то-энд шифрование. Это гарантирует, что ваши сообщения шифруются на устройстве отправителя и могут быть расшифрованы только на устройстве получателя.',
        '<b>Настройте параметры конфиденциальности</b>\nРегулярно проверяйте и настраивайте параметры конфиденциальности в своих социальных сетях и мессенджерах. Ограничьте видимость ваших личных данных только для доверенных лиц.',
        '<b>Используйте двухфакторную аутентификацию (2FA)</b>\nВключите двухфакторную аутентификацию для всех своих аккаунтов. Это добавит дополнительный уровень защиты, требуя подтверждения входа через второй шаг, такой как код из SMS или приложения.',
        '<b>Создавайте надежные пароли </b>\nИспользуйте длинные и сложные пароли, состоящие из букв, цифр и символов. Избегайте использования одного и того же пароля для разных аккаунтов. Менеджеры паролей помогут вам хранить и генерировать безопасные пароли.',
        '<b>Будьте осторожны с публичными Wi-Fi сетями </b>\nИзбегайте передачи конфиденциальной информации через публичные Wi-Fi сети. При необходимости использования таких сетей, подключайтесь через VPN для шифрования данных.',
        '<b>Не раскрывайте лишнюю информацию </b>\nНе делитесь в социальных сетях и мессенджерах личной информацией, такой как адрес, номер телефона, данные банковских карт и другая чувствительная информация.',
        '<b>Будьте осторожны с подозрительными ссылками и вложениями </b>\nНе открывайте ссылки и не скачивайте файлы от незнакомых или подозрительных отправителей.Это может привести к установке вредоносного ПО на ваше устройство.',
        '<b>Регулярно обновляйте приложения </b>\nОбновляйте свои мессенджеры и социальные сети до последней версии. Это поможет вам получить все актуальные обновления безопасности.',
        '<b>Контролируйте доступ к вашему устройству </b>\nНастройте блокировку экрана с использованием пароля, PIN-кода или биометрической аутентификации. Это защитит ваши данные в случае кражи или утери устройства.',
        '<b>Будьте бдительны </b>\nВсегда будьте внимательны к тому, что и с кем вы делитесь в интернете. Подумайте дважды, прежде чем публиковать или отправлять любую информацию.']
    return choice(advList)


def main_win(message):
    message_text = "<b>главное меню</b>"
    bot.send_message(message.chat.id, message_text, parse_mode='html', reply_markup=main_mess_markup())


def main_mess_show(message):
    bot.send_message(message.chat.id, 'Выберите:', reply_markup=main_mess_markup())


def main_mess_markup():
    markup = types.InlineKeyboardMarkup()
    markup_list = ['Получить совет', 'Инструменты и рекомендации',
                   'Часто задаваемые вопросы (FAQ)', 'Полезные ресурсы и ссылки']
    for mark_text in markup_list:
        markup.add(types.InlineKeyboardButton(mark_text, callback_data=mark_text))
    return markup


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except:
        pass
