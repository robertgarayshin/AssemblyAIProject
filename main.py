import subprocess
import telebot

bot = telebot.TeleBot('6088935436:AAGeLUqygWNlfW4qScaOes2j3vwnrw4Doqo')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Hey! This bot can help you to transcribe video into the text!\n'
                     'First of all, send me link to video on YouTube')


@bot.message_handler(content_types=['text', 'audio'])
def get_text_messages(message):
    print(message.text)
    try:
        bot.send_message(message.from_user.id, 'Wait...')
        subprocess.run(['python3', 'transcribe.py',
                        message.text,
                        '--api_key', 'c05a508dd63043c3837c2841991a3197'])
        f = open('transcript.txt', 'r')
        bot.send_message(message.from_user.id, f.read())
    except Exception:
        bot.send_message(message.from_user.id, 'Some error occurred while opening the link')
    finally:
        bot.send_message(message.from_user.id, 'Now you can enter new link')


bot.polling(none_stop=True, interval=0)
