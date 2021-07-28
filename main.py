import telebot
import const
from telebot import types
import sqlite3
import range
import subprocess
import os
import re
import string
import requests
import parsing
import threading, time



bot = telebot.TeleBot(const.token_bot)
city = dict()
tovar_d = dict()
ves_d = dict()
solo = list()
streat = list()
ban = list()
ph = ""

@bot.message_handler(commands=['start'])
def start_message(message):
        
        name = message.from_user.first_name
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Lviv", callback_data="Lviv")
        button2 = types.InlineKeyboardButton(text="Kiev", callback_data="Kiev")
        button3 = types.InlineKeyboardButton(text="Odessa", callback_data="Odessa")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text = "Bonjour, " + str(name) + ", Bienvenue dans notre Dobro🆂🅷🅾️🅿️. Il y a tout ce dont vous avez besoin, tout ce que vous avez à faire est de penser à ce que vous voulez ! Choisissez une ville, et l'action continue.", reply_markup=markup)
        
        

       
@bot.callback_query_handler(func=lambda c: (c.data == "Lviv" or c.data == "Kiev") or (c.data == "Odessa" or c.data == "mainmanu"))
def inline(c):
        cid = c.message.chat.id
        mid = c.message.message_id
        if c.data == "Lviv":
                city[c.from_user.first_name] = "lvov"
        elif c.data == "Kiev":
                city[c.from_user.first_name] = "kyiv"
        elif c.data == "Odessa":
                city[c.from_user.first_name] = "odessa"
        elif c.data == "mainmanu":
                keyboardmenu = types.InlineKeyboardMarkup(row_width=2)
                first_butt = types.InlineKeyboardButton(text="Règles", url="https://telegra.ph/Pravila-07-22-3")
                sec_butt = types.InlineKeyboardButton(text="Aide", url='t.me/alex_kotenko')
                th_butt = types.InlineKeyboardButton(text="Opérateur", url='t.me/Underbhoomi')
                f_buttom = types.InlineKeyboardButton(text="Liste d'articles", callback_data="positions")
                keyboardmenu.add(first_butt, sec_butt, th_butt, f_buttom)
                bot.edit_message_text(chat_id=cid, message_id=mid, text="La liste des articles vous permettra d'accéder à la boutique. N'oubliez pas de lire le règlement !",reply_markup=keyboardmenu)
        markup2 = types.InlineKeyboardMarkup()
        url_link = types.InlineKeyboardButton(text="Règles", url="https://telegra.ph/Pravila-07-22-3")
        switch_b1 = types.InlineKeyboardButton(text="Aide", url='t.me/alex_kotenko')
        switch_b2 = types.InlineKeyboardButton(text="Opérateur", url='t.me/Underbhoomi')
        po = types.InlineKeyboardButton(text="Liste d'articles", callback_data="positions")
        markup2.add(url_link, switch_b1, switch_b2, po)
        bot.edit_message_text(chat_id=cid, message_id=mid, text="La liste des articles vous permettra d'accéder à la boutique. N'oubliez pas de lire le règlement !",reply_markup=markup2)

@bot.callback_query_handler(func=lambda call: call.data == "positions" or call.data == "back2")
def positions(call):
        cid = call.message.chat.id
        mid = call.message.message_id

        if call.data == "back2":
                keyboardmenu2 = types.InlineKeyboardMarkup(row_width=2)
                b11 = types.InlineKeyboardButton(text="Le Philharmonique", callback_data="Le Philharmonique")
                b22 = types.InlineKeyboardButton(text="Shelh", callback_data="Shelh")
                b33 = types.InlineKeyboardButton(text="Kortoshka", callback_data="Kortoshka")
                back1 = types.InlineKeyboardButton(text="Dos", callback_data="mainmanu")
                keyboardmenu2.add(b11, b22, b33, back1)
                bot.edit_message_text(chat_id=cid, message_id=mid, text="De quel type de produit avez-vous besoin ?", reply_markup=keyboardmenu2)
        
        markup3 = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="Le Philharmonique", callback_data="Le Philharmonique")
        b2 = types.InlineKeyboardButton(text="Shelh", callback_data="Shelh")
        b3 = types.InlineKeyboardButton(text="Kortoshka", callback_data="Kortoshka")
        back = types.InlineKeyboardButton(text="Dos", callback_data="mainmanu")
        markup3.add(b1, b2, b3, back)
        bot.edit_message_text(chat_id=cid, message_id=mid, text="De quel type de produit avez-vous besoin ?", reply_markup=markup3)

@bot.callback_query_handler(func=lambda tovar: tovar.data == "Le Philharmonique" or tovar.data == "Shelh"  or tovar.data == "Kortoshka" or tovar.data == "back4")
def tovar_end(tovar):
        cid = tovar.message.chat.id
        mid = tovar.message.message_id
        markup = types.InlineKeyboardMarkup()
        if tovar.data == "Le Philharmonique" or tovar.data == "1":
                tovar_d[tovar.from_user.first_name] = "Le Philharmonique"
        elif tovar.data == "Shelh" or tovar.data =="3":
                tovar_d[tovar.from_user.first_name] = "Shelh"
        elif tovar.data == "Kortoshka" or tovar.data == "3":
                tovar_d[tovar.from_user.first_name] = "Kortoshka"
        elif tovar.data == "back4":
                keyboardmenu3 = types.InlineKeyboardMarkup()
                q1 = types.InlineKeyboardButton(text="1г", callback_data="1")
                q2 = types.InlineKeyboardButton(text="3г", callback_data="3")
                q3 = types.InlineKeyboardButton(text="5г", callback_data="5")
                back3 = types.InlineKeyboardButton(text="Dos", callback_data="back2")
                switch_v1 = types.InlineKeyboardButton(text="Opérateur", url='t.me/Underbhoomi')
                keyboardmenu3.add(q1, q2, q3, switch_v1, back3)
                bot.edit_message_text(chat_id=cid, message_id=mid, text="De quel poids avez-vous besoin ? Si vous avez besoin de plus, écrivez à notre opérateur !", reply_markup=keyboardmenu3)

        
        v1 = types.InlineKeyboardButton(text="1г", callback_data="1")
        v2 = types.InlineKeyboardButton(text="3г", callback_data="3")
        v3 = types.InlineKeyboardButton(text="5г", callback_data="5")
        back3 = types.InlineKeyboardButton(text="Dos", callback_data="back2")
        switch_v = types.InlineKeyboardButton(text="Opérateur", url='t.me/Underbhoomi')
        markup.add(v1, v2, v3, back3, switch_v)
        try:
                bot.edit_message_text(chat_id=cid, message_id=mid, text="De quel poids avez-vous besoin ? Si vous avez besoin de plus, écrivez à notre opérateur !", reply_markup=markup)
        except:
                v1 = types.InlineKeyboardButton(text="1г", callback_data="1")
                v2 = types.InlineKeyboardButton(text="3г", callback_data="3")
                v3 = types.InlineKeyboardButton(text="5г", callback_data="5")
                back3 = types.InlineKeyboardButton(text="Dos", callback_data="back2")
                switch_v = types.InlineKeyboardButton(text="Opérateur", url='t.me/Underbhoomi')
                markup.add(v1, v2, v3, back3, switch_v)

@bot.callback_query_handler(func=lambda ves: (ves.data == "1" or ves.data == "3") or ves.data == "5")
def ves_end(ves):
        try:
                cid = ves.message.chat.id
                mid = ves.message.message_id        
                country = list()
                region = list()
                if ves.data == "1":
                        ves_d[ves.from_user.first_name] = "1"
                elif ves.data == "3":
                        ves_d[ves.from_user.first_name] = "3"
                elif ves.data == "5":
                        ves_d[ves.from_user.first_name] = "5"
                country.append(city[ves.from_user.first_name])
                t = tovar_d[ves.from_user.first_name]
        except KeyError:
                pass
        cid = ves.message.chat.id
        mid = ves.message.message_id 
       
     
        region.append(ves.data) 
        ve =  ves_d[ves.from_user.first_name]
        con = sqlite3.connect("DataBase.db")
        cur = con.cursor()
        cur.execute("SELECT DISTINCT streat FROM stock WHERE city = (?) AND name_stock = (?) AND much = (?)",[country[0], t, int(ve)])
        datadb = list(cur)
        markup = types.InlineKeyboardMarkup()  
        for row in datadb:
                a = types.InlineKeyboardButton(text=row[const.const], callback_data=row[const.const]) 
                streat.append(row[const.const])
                markup.add(a) 
        back4 = types.InlineKeyboardButton(text="Dos", callback_data="back4")
        markup.add(back4)
        con.commit() 
        cur.close()
        con.close()   
        bot.edit_message_text(chat_id=cid, message_id=mid, text="Zones possibles selon votre demande. Sélectionnez celui que vous souhaitez pour connaître le prix.", reply_markup=markup)


@bot.callback_query_handler(func=lambda all_req: all_req.data in streat)
def funct(all_req):
        cid = all_req.message.chat.id
        mid = all_req.message.message_id
        countrys = city[all_req.from_user.first_name] 
        ts = tovar_d[all_req.from_user.first_name]
        ves =  ves_d[all_req.from_user.first_name]
        st = all_req.data
        con1 = sqlite3.connect("DataBase.db")
        cur = con1.cursor()
        cur.execute("SELECT DISTINCT price FROM stock WHERE city = (?) AND name_stock = (?) AND much = (?) AND streat = (?)",[countrys, ts, int(ves), st])
        datadb = list(cur)
        for row in datadb:
                solo.append(row[const.const])
                pr = row[const.const]
        markup = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text="Annulation", callback_data="mainmanu")
        buy = types.InlineKeyboardButton(text="Payez", callback_data="price")
        markup.add(back, buy)
        con1.commit()
        cur.close()
        con1.close()
        bot.edit_message_text(chat_id=cid, message_id=mid, text="Très bien, qu'est-ce qu'on a ? Vous avez choisi une ville. - {} dans le voisinage {} et en poids  {} sera {}grammes . Vous devez payer{}UAH. Prêt à s'amuser ?".format(countrys, st, ts, ves, pr), reply_markup=markup)


@bot.callback_query_handler(func=lambda yets: yets.data == "price")
def somfunk(yets):
        cid = yets.message.chat.id
        mid = yets.message.message_id
        markup = types.InlineKeyboardMarkup() 
        bby = types.InlineKeyboardButton(text="Envoyer pour vérifier", callback_data="check")
        oo = types.InlineKeyboardButton(text="EasyPay - 95436138", url="https://easypay.ua/ua/catalog/e-money/easypay/easypay-money-deposit?account=95436138")
        markup.add(oo)
        markup.add(bby)
        bot.edit_message_text(chat_id=cid, message_id=mid,text="Après être allé sur le site pour payer, n'oubliez pas d'appuyer sur le bouton "Envoyer pour vérifier". Vous avez 35 minutes pour tout faire. Si vous ne le faites pas ou si vous vous trompez, vous serez banni. 3 interdictions - vous obtiendrez une interdiction d'urgence.", reply_markup=markup)




@bot.callback_query_handler(func=lambda okbuy: okbuy.data == "check")
def ff(okbuy):
        cid = okbuy.message.chat.id
        mid = okbuy.message.message_id
        bot.edit_message_text(chat_id=cid, message_id=mid, text="Entrez le montant que vous avez payé")       


@bot.message_handler(content_types=['text'])
def price_streat(price):
        bal, state = parsing.chakout()
        time.sleep(10)
        cid = price.chat.id
        mid = price.message_id
        countrys = city[price.from_user.first_name] 
        ts = tovar_d[price.from_user.first_name]
        ves =  ves_d[price.from_user.first_name]
        st = streat[-1]
        so = solo[-1]
        con1 = sqlite3.connect("DataBase.db")
        cur = con1.cursor()
        cur.execute("SELECT DISTINCT * FROM stock WHERE city = (?) AND name_stock = (?) AND much = (?) AND streat = (?) AND price = (?)",[countrys, ts, int(ves), st, so])
        datadb = list(cur)
        counterc = 0
        cr = list()
        for row in datadb:
                solo.append(row[counterc])
                cr.append(row[counterc])
                counterc = counterc + 1
        cur.execute("SELECT DISTINCT photo FROM stock WHERE city = (?) AND name_stock = (?) AND much = (?) AND streat = (?) AND price = (?)",[countrys, ts, int(ves), st, so])
        datadb = list(cur)
        for row in datadb:
                ph = row[const.const]
        print(ph)
        con1.commit()
        cur.close()
        con1.close()
        msg = ""
        if((bal < price.data) or (state == price.data)):
                bot.edit_message_text(chat_id=cid, message_id=mid, text="OK, je vous envoie un lien vers une photo de l'endroit !")
                time.sleep(3)
                msg = bot.edit_message_text(chat_id=cid, message_id=mid, text="Le lien a été envoyé. N'oubliez pas de le sauvegarder!" + ph)
                conn = sqlite3.connect("DataBase.db")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM stock WHERE photo = (?)",[ph])
                conn.commit()
                cursor.close()
                conn.close()
                ok = "end"
                baaaan(ok)
        else:
                bot.register_next_step_handler(msg, "Quelque chose a mal tourné pour vous. Essayez encore !", moreOne(bal, price.data. state))

def moreOne(message):
        chat_id = message.chat.id
        
        if((bal < price.data) or (state == price.data)):
                bot.send_message(chat_id, text="OK, je vous envoie un lien vers une photo de l'endroit !")
                time.sleep(3)
                bot.send_message(chat_id, text="Le lien a été envoyé. N'oubliez pas de le sauvegarder !" + ph)
                conn = sqlite3.connect("DataBase.db")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM stock WHERE photo = (?)",[ph])
                conn.commit()
                cursor.close()
                conn.close()
                ok = "end"
                baaaan(ok)
        else:
                if ban[message.from_user.first_name] == 0:
                        bot.send_message(chat_id, text="Vous avez 1 réprimande. 3 démérites - BAN")
                        ban[message.from_user.first_name] = 1
                elif ban[message.from_user.first_name] == 1:
                        bot.send_message(chat_id, text="Vous avez 2 réprimandes. 3 démérites - BAN")
                        ban[message.from_user.first_name] = 2
                elif ban[message.from_user.first_name] == 2:
                        bot.send_message(chat_id, text="Vous avez 3 réprimandes. 3 démérites - BAN")
                        ban[message.from_user.first_name] = 3
                        notok = "sad"
                        baaaan(notok)
                elif ban[message.from_user.first_name] == 3:
                        bot.send_message(chat_id, text="Vous avez 3 réprimandes. 3 démérites - BAN")
                        notok = "sad"
                        baaaan(notok)

                
def baaaan(m):
        chat_id = m.chat.id
        if m == "end":
                pass
        if m == "sad":
                bot.edit_message_text(chat_id, "Tu as eu trois interdictions. Disons au revoir !")





  
if __name__ == "__main__":
        bot.polling(none_stop=True, interval=0)
                
        
