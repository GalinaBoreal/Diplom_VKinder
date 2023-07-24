from vk_bot import VkBot
from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

token = 'vk1.a.tjL8Ri4s2zRcPz3aB6CiZXZq2Undzl3sHeLV3tH6GGxQbPMYEJmfHIqNDoDaUw3e3MHnXjj3oI8Tx8KPQEepj5Zvh-P4rT2UUSbtirOtejoP1_2qCjGlKgqUOZFblASs4F4XjGMxtO7v2E8tvLXXNqoNABKmaBDoemiwniObrpbe3devZqxu9_QPidhPJjBnx0u6TB35NsQ6COelZmm4Aw'  # input('Token: ')

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,
                                'random_id': randrange(10 ** 7), })


print("Server started")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text

            print(f'New message for me from user with ID: {event.user_id}', end='')

            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))

            print('Text: ', event.text)
