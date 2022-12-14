# -*- coding: utf-8 -*-
"""Nickpresents.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zgFbBH7gc0q-RbF3cQXMUAP7B0jdL1T0
"""

import nest_asyncio
nest_asyncio.apply()
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # for reply keyboard (sends message)

from time import sleep

bot = Bot(token='5797659424:AAHhiLaVZZm2HLIGWg_6SoLqKxU_Jun2sPE')
dp = Dispatcher(bot)

answers = []  # store the answers they have given

# Nick selection
Nick1 = KeyboardButton('Утренний Никита')  
Nick2 = KeyboardButton('Дневной Никита')
Nick3 = KeyboardButton('Вечерний Никита')
Nick4 = KeyboardButton('Ночной Никита')
Nick_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(Nick1).add(Nick2).add(Nick3).add(Nick4)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):

    await message.answer('Какой ты Никита сейчас?', reply_markup = Nick_kb)
    

morning_Nick = KeyboardButton('Взять структурированный подарочек для утреннего Никиты')
back_Nick = KeyboardButton('🔙 Выбрать другого Никиту')
morning_Nick_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(morning_Nick).add(back_Nick)

daily_Nick = KeyboardButton('Здесь art-and-science подарочек для дневного Никиты')
back_Nick = KeyboardButton('🔙 Выбрать другого Никиту')
daily_Nick_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(daily_Nick).add(back_Nick)

evening_Nick = KeyboardButton('Magical подарочек ждёт вечернего Никиту')
back_Nick = KeyboardButton('🔙 Выбрать другого Никиту')
evening_Nick_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(evening_Nick).add(back_Nick)

night_Nick = KeyboardButton('Забрать wild подарочек для ночного Никиты')
back_Nick = KeyboardButton('🔙 Выбрать другого Никиту')
night_Nick_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(night_Nick).add(back_Nick)

@dp.message_handler(regexp='🔙 Выбрать другого Никиту')
async def english(message: types.Message):
    answers.append(message.text)
    await message.answer('Какой ты Никита сейчас?', reply_markup = Nick_kb)
    

@dp.message_handler(regexp='Утренний Никита')
async def english(message: types.Message):
    answers.append(message.text)
    await message.answer('🧙🏻‍♂️☢️', reply_markup = morning_Nick_kb)
    await bot.send_photo(message.chat.id, photo="https://cdn.midjourney.com/cbb0eaa8-2be8-4078-81ae-1be9e6a159a7/grid_0.png")

@dp.message_handler(regexp='Взять структурированный подарочек для утреннего Никиты')
async def english(message: types.Message):
    answers.append(message.text)
    await message.answer('Вот здесь подарочек: https://drive.google.com/file/d/1hClYmpBIOFcPXNQ3Od2Q2XnnCfZyqrcI/view?usp=sharing', reply_markup = morning_Nick_kb)

@dp.message_handler(regexp='Дневной Никита')
async def english(message: types.Message):
    answers.append(message.text)
    await message.answer('🧙🏻‍♂️✡️', reply_markup = daily_Nick_kb)
    await bot.send_photo(message.chat.id, photo="https://snipboard.io/oyNkpW.jpg")

@dp.message_handler(regexp='Здесь art-and-science подарочек для дневного Никиты')
async def english(message: types.Message):
    answers.append(message.text)
    await message.answer('Вот тут: https://drive.google.com/file/d/1p8aOPcbJK9pWP103l6mZZQGajR_ftqVv/view?usp=sharing', reply_markup = daily_Nick_kb)

@dp.message_handler(regexp='Вечерний Никита')
async def english(message: types.Message):
    answers.append(message.text)
    await message.answer('🧙🏻‍♂️🌌', reply_markup = evening_Nick_kb)
    await bot.send_photo(message.chat.id, photo="https://cdn.midjourney.com/de1601ef-a730-4fb0-b47e-f3f09f09ddf6/grid_0.png")

@dp.message_handler(regexp='Magical подарочек ждёт вечернего Никиту')
async def english(message: types.Message):
    answers.append(message.text)
    await message.answer('Ждёт вот здесь (там непростительное заклинание): https://telegra.ph/A-kakie-razmery-Vselennoj-11-20', reply_markup = evening_Nick_kb)

@dp.message_handler(regexp='Ночной Никита')
async def english(message: types.Message):
    answers.append(message.text)
    await message.answer('🧙🏻‍♂️🌚', reply_markup = night_Nick_kb)
    await bot.send_photo(message.chat.id, photo="https://cdn.midjourney.com/ded88f0e-3018-4b14-9427-b420ceee202f/grid_0.png")

@dp.message_handler(regexp='Забрать wild подарочек для ночного Никиты')
async def english(message: types.Message):
    answers.append(message.text)
    await message.answer('Enjoy this guilty-guilty pleasure: https://docs.google.com/document/d/1jFIg2cICVtrWQQF4MG43ryIUgDPcTj2H62B-LOxr_Cw/edit?usp=sharing', reply_markup = night_Nick_kb)


executor.start_polling(dp)

