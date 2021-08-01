import telebot
import random
from telebot import types

TOKEN = '1892592237:AAFCFPwIEW3z5bZ8dbtj8rK1x4KoRUlRoBw'

bot = telebot.TeleBot(TOKEN)

HELP = 'Я умею не так уж и много, но воть с этим я справлюсь:\n' \
       '/command1 - Я тебе расскажу немножко о себе\n' \
       '/command2 - Я сыграю с тобой в игру "Угадай число"\n' \
       '/command3 - Тебе грустно? Я поддержу тебя'


compassion_emoji = '(っ´ω`)ﾉ(╥ω╥)\n\n'
soft_words = ['Безвыходных ситуаций не бывает. Мы сможем все решить'
              ' и когда-то будет вспоминать эти времена с улыбкой.',
              'Сейчас это тебя тревожит и волнует, но через год ты '
              'над этим рассмеешься. Зачем тратить время, если посмеяться можно уже сейчас?',
              'Самая большая ошибка в жизни – это боязнь ошибаться.',
              'Улыбнись сейчас же, ты же не хочешь расстраивать маленького глупого бота? (｡╯︵╰｡)',
              'Скорбью и беспокойством мы лишаем себя счастливого будущего.',
              'Лучший способ избавиться от боли – это почувствовать и принять ее. Выйди за ее пределы.',
              'Если проблемы нельзя решить, то о них не стоит беспокоиться. Расслабься и плыви по течению.',
              'Ты прекрасный человек, который заслуживает всего самого лучшего. Помни, именно в тяжелые '
              'времена раскрывается наш потенциал и возможности.\U0001F4AA',
              'Все проблемы несоизмеримы малы в сравнении с нашей внутренней силой.',
              'Все, что мы оставили в прошлом, нам совсем ненужно в будущем.',
              'У нас нет защитного панциря от проблем, но мы должны уметь прощать и '
              'отпускать все свои печали. Ты можешь смириться и отпустить все прошлое.',
              'Не отчаивайся. Тебя впереди ждет только самое лучшее. Ты мне веришь? (≧◡≦) ♡',
              'Не смей сдаваться и отчаиваться. Каждый день появляются новые возможности. '
              'Что еще сегодня кажется невозможным, завтра станет реальностью.',
              'Любая проблема может оказаться тем, что поможет тебе перейти на новый жизненный этап. '
              'Ищи во всем новые возможности. Я верю в тебя',
              'Очень грустно, что все так произошло, но это в прошлом. '
              'Давай подумаем над тем, как изменить ситуацию в настоящем.',
              'Давай верить лучшее. Все тучи быстро развеются и выйдет солнце.\U00002600',
              'Направь свои силы и мысли на что-то более приятное. Давай будет на стороне счастья?',
              'Нет ничего страшного, что ты беспокоишься о своем будущем в такое сложное время. '
              'Ты смелый и упорный, а значит сможешь победить.',
              'Если опоздал на один поезд, то всегда появится другой. Так и в жизни.'
              ' Всегда будут новые возможности, даже тогда, когда казалось все упущено.',
              'В мире много необъяснимого. '
              'Порой кажется, что все пропало, а потом происходит чудо. Главное не падай духом.',
              'Этот промежуток жизни у тебя нелегкий, но это только короткий отрезок '
              'твоего жизненного пути. Скоро у тебя начнется белая полоса, обещаю.',
              'Дыши глубже, прислушайся к своему сердцебиению. Жив? Значит все ещё можно исправить.',
              'Позволь себе на час позабыть о всем плохом. Сделай чая, '
              'скушай что-нибудь вкусненькое и насладись моментом. '
              'После этого тебе будет легче найти выход из ситуации.',
              'У тебя обязательно все получится, но моей только веры в '
              'тебя недостаточно. Ты тоже должен верить в себя.',
              'Все эти трудности временные, а ты это прекрасно знаешь. Когда-то и на '
              'нашей улице перевернется самосвал с пряниками.',
              'Пока мы крутим педали к цели, порой цепь соскальзывает и колеса пробиваются.'
              ' Но ты не должен забывать о прекрасном, что открывается каждый день за новым поворотом дороги.',
              'Хватит тратить жизнь на горести и печали. Время улыбнуться и идти по жизни дальше.',
              'Твои горести и проблемы не смогут уйти быстро. Но мы можем принять их и смириться '
              'с ними. Давай изменим наше отношение к неприятностям. ',
              'Самые сильные люди – это те, кто не сдается в даже самых сложных битвах. Ты один из них.',
              'Таким людям как ты нельзя грустить. Красные глаза и мокрый нос делам '
              'не помогут, поэтому наберись сил идти вперед.']

print('soft w:', len(soft_words))

with open('text_files/motivation_words.txt', 'r', encoding='utf-8') as f:
    motivation_words = f.readlines()

motivation_emoji = '(*＾ω＾)人(＾ω＾*)\n\n'

print('motivation w:', len(motivation_words))

MINIMUM = 0
MAXIMUM = 100
change_part = MAXIMUM
game_answer = int((change_part - MINIMUM) / 2)


@bot.message_handler(commands=['command4'])
def send_motivation(message):
    answer = motivation_emoji + motivation_words[random.randint(0, len(motivation_words) - 1)]
    bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['command3'])
def send_empathy(message):
    answer = compassion_emoji + soft_words[random.randint(0, len(soft_words) - 1)]
    bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['command2'])
def send_game(message, minimum=MINIMUM, maximum=MAXIMUM):
    bot.send_message(message.chat.id, 'Я так рад, что ты решил сыграть со мной ≧ω≦\n'
                                      'Загадай пожалуйста какое-нибудь число в диапазоне от {} до {}, '
                                      ' я постараюсь его отгадать.\n\nНачнем игру!'.format(minimum, maximum))
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup_item1 = telebot.types.KeyboardButton('Мое число больше...')
    markup_item2 = telebot.types.KeyboardButton('Мое число меньше...')
    markup_item3 = telebot.types.KeyboardButton('Это верный ответ!')
    markup.add(markup_item1, markup_item2, markup_item3)
    msg = bot.send_message(message.chat.id, 'Ответ {}?'.format(game_answer), reply_markup=markup)
    bot.register_next_step_handler(msg, some_wow)


def some_wow(message):
    global change_part
    global game_answer
    change_part, game_answer = process_game_answer(message, change_part, game_answer)
    if game_answer != '-1':
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup_item1 = telebot.types.KeyboardButton('Мое число больше...')
        markup_item2 = telebot.types.KeyboardButton('Мое число меньше...')
        markup_item3 = telebot.types.KeyboardButton('Это верный ответ!')
        markup.add(markup_item1, markup_item2, markup_item3)
        msg = bot.send_message(message.chat.id, 'Ответ {}?'.format(game_answer), reply_markup=markup)
        bot.register_next_step_handler(msg, some_wow)
    else:
        global MAXIMUM, MINIMUM
        change_part = MAXIMUM
        game_answer = int((change_part - MINIMUM) / 2)
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, 'Ура! Я победил! Спасибо за игру, '
                                          'мне было очень весело с тобой ≧ω≦', reply_markup=markup)
        return -1


def process_game_answer(message, cng_part, answer):
    if message.text == 'Мое число больше...':
        cng_part = round(cng_part / 2 + 1)
        answer = int(answer + cng_part / 2)
    elif message.text == 'Мое число меньше...':
        cng_part = round(cng_part / 2 + 1)
        answer = int(answer - cng_part / 2)
    else:
        answer = '-1'
    return cng_part, answer


@bot.message_handler(commands=['start', 'command1'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет! Я маленький и милый бот,'
                                      ' пока что я могу только поддержать тебя, если тебе '
                                      'грустно, играть с тобой и повторять твои слова, '
                                      'поэтому не обижай меня ≧ω≦')


@bot.message_handler(commands=['help'])
def send_help_msg(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(content_types=["text"])
def echo_text(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)  # начинает отправку запросов на сервера
