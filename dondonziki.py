import telebot,random
from telebot import types

TOKEN="YOUR_BOT_TOKEN"
bot=telebot.TeleBot(TOKEN)
opts=["✊","✌️","🖐️"]

@bot.message_handler(commands=['start'])
def s(m):
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(*opts)
    bot.send_message(m.chat.id,"Tanlang:",reply_markup=kb)

@bot.message_handler(func=lambda m:m.text in opts)
def p(m):
    b=random.choice(opts);u=m.text
    if u==b:r="🤝 Durrang"
    elif(u,b)in[("✊","✌️"),("✌️","🖐️"),("🖐️","✊")]:r="🎉 Siz yutdingiz"
    else:r="😢 Bot yutdi"
    bot.send_message(m.chat.id,f"Siz:{u}\nBot:{b}\n{r}")

bot.infinity_polling()