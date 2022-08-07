from requirements.functions import dp
from aiogram import executor

import actions.start, actions.my_wallet, actions.pay_money, actions.magazin, actions.change_lang, actions.boglanish
import admin_panel.panel, admin_panel.magazin, admin_panel.rubl_kursi, admin_panel.keshbek, admin_panel.payment_confirmer, admin_panel.statistics, admin_panel.payment_controller, admin_panel.settings, admin_panel.payment_history, admin_panel.send_to_all

import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger().disabled = True

executor.start_polling(dp, skip_updates=True)