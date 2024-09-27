from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters

TOKEN = '7669492702:AAH1TUztT4WzBMmgpEgavHgalmDHO-evszw'

codes_memory = {
    "ZOO": [f"ZOO-{i}" for i in range(1, 101)],
    "TILE": [f"TILE-{i}" for i in range(1, 101)],
    "CUBE": [f"CUBE-{i}" for i in range(1, 101)],
    "TRAIN": [f"TRAIN-{i}" for i in range(1, 101)],
    "MERGE": [f"MERGE-{i}" for i in range(1, 101)],
    "TWERK": [
        "TWERK-YEH-Y3QW-ZXMX-CZX",
        "TWERK-XE1-V3V6-ZMK9-FBJ",
        "TWERK-XDS-SLW1-ZDKH-CH5",
        "TWERK-WES-RM4F-ZDL9-FNR",
        "TWERK-ZEM-SZ77-ZML2-T9Y",
        "TWERK-WDM-R9FP-Z9K2-V4Y",
        "TWERK-ZE5-YXDF-ZFMA-TE6",
        "TWERK-XES-YVCF-ZZLA-2E8",
        "TWERK-XES-VBQX-ZBNW-1FZ",
        "TWERK-WDM-RR74-Z5LA-TYY",
        "TWERK-YEH-T15J-ZBLJ-YX1",
        "TWERK-WES-Y2PM-Z3MW-29A",
        "TWERK-XE1-Z3AZ-ZBNJ-67X",
        "TWERK-ZED-Y76Q-Z9K2-84P",
        "TWERK-XE1-VYWT-ZHKW-BXN",
        "TWERK-XE1-X3P8-ZVLA-EHM"
    ],
    "POLY": [f"POLY-{i}" for i in range(1, 101)],
    "TRIM": [f"TRIM-{i}" for i in range(1, 101)],
    "STONE": [f"STONE-{i}" for i in range(1, 101)],
    "BOUNC": [
        "BOUNC-WGE-NTLX-Z1ZZ-7HH",
        "BOUNC-ZGN-LTL1-Z1XF-KJD",
        "BOUNC-YFJ-KDAG-ZFXZ-GH1",
        "BOUNC-WF6-FSYN-Z3YZ-GHM",
        "BOUNC-YF6-LDRG-Z1Z7-KHB",
        "BOUNC-WF6-HDDX-Z9Y7-BK2",
        "BOUNC-ZFA-MS3W-ZHZF-LKR",
        "BOUNC-ZGW-HR59-ZKWQ-9Q3",
        "BOUNC-XG6-NRB7-ZFXZ-DPV",
        "BOUNC-YGE-LEXH-ZZWF-LQA",
        "BOUNC-XG2-MENM-ZZWZ-EGM",
        "BOUNC-YGE-JEPL-Z5ZF-GGJ",
        "BOUNC-ZFW-GEHS-Z3XZ-FJ2",
        "BOUNC-ZFR-F1NM-Z7YQ-M8T"
    ],
    "HIDE": [f"HIDE-{i}" for i in range(1, 101)],
    "WATER": [
        "WATER-YFE-ADFK-ZVZ4-G9Z",
        "WATER-YFN-9HL9-ZMYT-LD1",
        "WATER-ZFJ-AJJ3-ZZZT-FZW",
        "WATER-YFJ-92J2-ZVYT-873",
        "WATER-WGE-AKGG-Z5XC-9BA",
        "WATER-YGN-E4VH-ZXWL-LXQ",
        "WATER-WFN-9X2K-ZVYS-1VX",
        "WATER-WGA-79ZQ-Z9XM-1RY",
        "WATER-XFE-9WR4-Z3ZD-1BW",
        "WATER-ZFJ-EVJ3-ZMYS-4WS",
        "WATER-XF2-9V1J-Z7X5-52K",
        "WATER-ZF2-CVFS-Z9XM-VA8",
        "WATER-ZFR-8TP5-Z1WS-YL6",
        "WATER-XF6-7DKN-ZHXM-ZRT",
        "WATER-YF2-BSNW-ZFZ5-VSK",
        "WATER-XGW-7SXN-ZSX5-PRX"
    ]
}

user_selected_game = {}

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("ZOO", callback_data='ZOO')],
        [InlineKeyboardButton("TILE", callback_data='TILE')],
        [InlineKeyboardButton("CUBE", callback_data='CUBE')],
        [InlineKeyboardButton("TRAIN", callback_data='TRAIN')],
        [InlineKeyboardButton("MERGE", callback_data='MERGE')],
        [InlineKeyboardButton("TWERK", callback_data='TWERK')],
        [InlineKeyboardButton("POLY", callback_data='POLY')],
        [InlineKeyboardButton("TRIM", callback_data='TRIM')],
        [InlineKeyboardButton("STONE", callback_data='STONE')],
        [InlineKeyboardButton("BOUNC", callback_data='BOUNC')],
        [InlineKeyboardButton("HIDE", callback_data='HIDE')],
        [InlineKeyboardButton("WATER", callback_data='WATER')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Please select a game to add or get codes:', reply_markup=reply_markup)

async def button(update, context):
    query = update.callback_query
    game_name = query.data
    user_id = query.from_user.id
    user_selected_game[user_id] = game_name
    keyboard = [
        [InlineKeyboardButton("Add Codes", callback_data=f'add_{game_name}')],
        [InlineKeyboardButton("Get Codes", callback_data=f'get_{game_name}')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(f"Game {game_name} selected. Choose an action:", reply_markup=reply_markup)

async def add_codes(update, context):
    user_id = update.message.from_user.id
    if user_id in user_selected_game:
        game_name = user_selected_game[user_id]
        new_codes = update.message.text.splitlines()

        if len(new_codes) == 16:
            codes_memory[game_name].extend(new_codes)
            await update.message.reply_text(f"16 new codes added to {game_name}.")
        else:
            await update.message.reply_text("Please send exactly 16 codes.")
    else:
        await update.message.reply_text("Select a game first using /start.")

async def get_codes(update, context):
    query = update.callback_query
    game_name = query.data.split('_')[1]
    if game_name in codes_memory and len(codes_memory[game_name]) >= 4:
        selected_codes = codes_memory[game_name][:4]
        codes_memory[game_name] = codes_memory[game_name][4:]
        await query.edit_message_text(f"Here are 4 codes from {game_name}: \n" + "\n".join(selected_codes))
    else:
        await query.edit_message_text(f"Not enough codes available in {game_name}.")

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button, pattern='^(?!add_|get_).*'))
    application.add_handler(CallbackQueryHandler(get_codes, pattern='^get_'))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, add_codes))

    application.run_polling()

if __name__ == '__main__':
    main()
