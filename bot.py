# # from telegram import Update, Bot
# # from telegram.constants import ParseMode
# # from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext, ApplicationBuilder
# # from django.conf import settings
# #
# # # from logistika_web.models import Order
# #
# # # Global variable to store the authorized user's chat ID
# # AUTHORIZED_CHAT_ID = []
# #
# # TELEGRAM_BOT_TOKEN = '7382369483:AAHkXNv8ETW0Bu3Jvn-dax5r4pa_ZnIasYM'
# # CORRECT_PASSWORD = 'salom'
# #
# # fields_name = {
# #     'user': 'Ф.И.О',
# #     'phone_number': 'Номер телефона',
# #     'sender_address': 'Адрес отправителя',
# #     'data_load': 'Дата загрузки груза',
# #     'destination': 'Место доставки груза (пункт назначения)',
# #     'cargo_type': 'Вид груза, его классификационное описание',
# #     'code': 'Товарный код',
# #     'marking': 'Маркировка',
# #     'country_origin': 'Страна происхождения',
# #     'cost': 'Стоимость  груза',
# #     'size': 'Размер упаковки',
# #     'volume': 'Объем',
# #     'number_seats': 'Количество мест',
# #     'weight': 'Вес /брутто, нетто/ всех мест',
# #     'transport_type': 'Вид транспорта и условия по отправке',
# #     'product_insurance': 'Указания о страховании груза (Осуществляется за счет Клиента)',
# #     'special_notes': 'Особые отметки',
# #     'tg_nickname': 'Никнейм в Telegram',
# #     'comment': 'Комментарий',
# # }
# #
# #
# # async def start(update: Update, context: CallbackContext):
# #     await update.message.reply_text("Please enter the password:")
# #
# #
# # async def check_password(update: Update, context: CallbackContext):
# #     global AUTHORIZED_CHAT_ID
# #     user = update.message.from_user
# #     if update.message.text == CORRECT_PASSWORD:
# #         if update.message.chat_id in AUTHORIZED_CHAT_ID:
# #             await update.message.reply_text(f"Hello {user}. Password correct! You will receive all form submissions.")
# #         else:
# #             AUTHORIZED_CHAT_ID.append(update.message.chat_id)
# #             await update.message.reply_text("Password correct! You will receive all form submissions. I will remember you.")
# #     else:
# #         await update.message.reply_text("Incorrect password. Please try again.")
# #
# #
# # async def notify_new_submission(form_data):
# #     global AUTHORIZED_CHAT_ID
# #     # if AUTHORIZED_CHAT_ID:
# #     print(form_data)
# #     bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
# #     message = f"Форма заказа:\n"
# #     for field, label in fields_name.items():
# #         value = getattr(form_data, field, None)
# #         print(label, ': ', value)
# #         if value:
# #             message += f"<b>{label}</b>: <em>{value}</em>\n"
# #     for chat_id in AUTHORIZED_CHAT_ID:
# #         await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)
# #
# #
# # def main():
# #     app = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()
# #     app.add_handler(CommandHandler("start", start))
# #     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_password))
# #
# #     app.run_polling()
# #
# #
# # # if __name__ == '__main__':
# #     main()
#
# from flask import Flask, request, jsonify
# from telegram import Bot
# from telegram.ext import Updater, CommandHandler
# import os
#
# app = Flask(__name__)
#
# TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'your-telegram-bot-token-here')
# AUTHORIZED_CHAT_ID = None
#
# bot = Bot(token=TELEGRAM_BOT_TOKEN)
#
# def send_message_to_authorized_user(data):
#     global AUTHORIZED_CHAT_ID
#     if AUTHORIZED_CHAT_ID:
#         message = f"New submission:\nName: {data['name']}\nEmail: {data['email']}\nMessage: {data['message']}"
#         bot.send_message(chat_id=AUTHORIZED_CHAT_ID, text=message)
#
# @app.route('/notify', methods=['POST'])
# def notify():
#     data = request.json
#     send_message_to_authorized_user(data)
#     return jsonify({"status": "success"}), 200
#
# def start(update, context):
#     update.message.reply_text("Please enter the password:")
#
# def check_password(update, context):
#     global AUTHORIZED_CHAT_ID
#     if update.message.text == os.getenv('BOT_PASSWORD', 'your-secure-password'):
#         AUTHORIZED_CHAT_ID = update.message.chat_id
#         update.message.reply_text("Password correct! You will receive all form submissions.")
#     else:
#         update.message.reply_text("Incorrect password. Please try again.")
#
# def main():
#     updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
#     dispatcher = updater.dispatcher
#
#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(CommandHandler("check_password", check_password))
#
#     updater.start_polling()
#     updater.idle()
#
# if __name__ == '__main__':
#     from threading import Thread
#     Thread(target=main).start()
#     app.run(host='0.0.0.0', port=5000)
