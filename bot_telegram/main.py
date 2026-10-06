import os
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup , KeyboardButton, InlineKeyboardButton ,InlineKeyboardMarkup# pour implementer une focnction qui pose une question et propose 4 options en commentaires comme si c'etait un quiz ;InlineKeyboardButton ,InlineKeyboardMarkup pour les boutons cliquable afficher directement dans le chat
from telegram.ext import Application , CommandHandler# on importe  ce qui nous interresse dans le modile telgremme pour creer l'app, commandhandel pour l'enregistrement des commandes
load_dotenv() #pour charger l'environnement virtuel

token = os.getenv('TOKEN')#pour recuperer le token


async def start(update, context):#fontion telegram avec une decllaration asynchrone pour les bots
    await update.message.reply_text("""Bienvenue  sur le bot de comment coder. pour avoir 
les dernieres informations, veuillez faire:
- /site pour consulter le site
- /question pour repondre a une question
- /youtube pour voir les dernieres videos""")#update cest pour repondre quand l'utilisateur tape la commande /start


async def site(update, context):
    await update.message.reply_text("""le lien du site comment coder est https://www.commentcoder.com""")


async def question(update, context):
    keyboard = [# on declare un clavier de 4 bouton qui es une liste contstitue elle meme d'une liste par ligne de 2 boutons
        [KeyboardButton("python"), KeyboardButton("java")],
        [KeyboardButton("javaScript"), KeyboardButton("c et ++")]
    ]

    reply_markup = ReplyKeyboardMarkup (
        keyboard=keyboard, 
        resize_keyboard=True, 
        one_time_keyboard=True
    )#on prepare le clavier avec un markup les 2 derniers options permet d'eviter d'avoir les problemes d'affochage
    await update.message.reply_text("quel es votre language preferer ?",
                                    reply_markup=reply_markup)
    

async def youtube (update, context):
    keyboard = [
        [InlineKeyboardButton('Python', 'https://www.python.org/downloads/windows/')],
        [InlineKeyboardButton('django', 'https://www.djangoproject.com/')],
        [InlineKeyboardButton('java', 'https://www.java.com/de/')],
        [InlineKeyboardButton('bot discord en python', 'https://discord.com/')],
        
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("que voulez vous aprendre aujourdhui?",
                                    reply_markup=reply_markup)
    



if __name__ == '__main__':# coe ca le code qui es dans ce bloc ne s'execute que si on lance le fichier directement avec python main.py
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler('start', start))# on declare la dfonction au gestionaire de commande et on fourni en parametre la commande 
    app.add_handler(CommandHandler('site', site)) #on declare la dfonction au gestionaire de commande et on fourni en parametre la commande
    app.add_handler(CommandHandler('question', question))# on declare la dfonction au gestionaire de commande et on fourni en parametre la commande 
    app.add_handler(CommandHandler('youtube', youtube))# on declare la dfonction au gestionaire de commande et on fourni en parametre la commande 

    app.run_polling(poll_interval=5)# permet d'interoger les serveurs telegram regulierement pour voir des choses se sont passees avec intervale de frequence