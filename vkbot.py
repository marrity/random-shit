# -*- coding: utf-8 -*-
"""vkbot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13MU_jkrblFY2f1q_kcxPEESylrn3geUZ
"""

!pip install vk_api

import vk_api
import random
from random import choice, randrange
from vk_api.longpoll import VkLongPoll, VkEventType


TOKEN = 'vk1.a.OnSJdGzkye0jOUmN2ZJQMFW3R8nm6X0YVmeLZKXW2io25wIaaG_aU2yVXRjFT0lQdmjQIGhBbzb26hzdvi3iU_nVC1GSAm5HxtZC2YsEYVPz9OcWuSZtDfJqROLrWXTi1Paasw8897w1zzzZsD7Bg8zNnIXCIwrysiMUoP0ctSwS9ioR3oTmNrg8DGeD9gJ7DTfe7on82VS0XOi_frw2PA'


vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


vars = ['камень', 'ножницы', 'бумага']

for event in longpoll.listen():
  if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text.lower() in vars:
    if event.from_user:
      user = event.text.lower()
      bot = choice(vars)
      vk.messages.send(user_id=event.user_id, message=bot, random_id = randrange(1, 10000000))
      out = ''
      if bot == 'ножницы':
        if user == 'ножницы':
            out = 'ничья'
        elif user == 'бумага':
            out = 'ты проиграл'
        else:
            out = 'ты выиграл'
      if bot == 'бумага':
        if user == 'бумага':
            out = 'ничья'
        elif user == 'камень':
            out = 'ты проиграл'
        else:
            out = 'ты выиграл'
      if bot == 'камень':
        if user == 'камень':
            out = 'ничья'
        elif user == 'ножницы':
            out = 'ты проиграл'
        else:
            out = 'ты выиграл'
      vk.messages.send(user_id=event.user_id, message=out, random_id=randrange(1, 1000000000))

