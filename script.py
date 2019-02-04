# -*- coding: utf-8 -*-
import vk_api
import requests
import json
from vk_api.longpoll import VkLongPoll, VkEventType

def two_factor():
    code = input('Code? ')
    remember_device= True
    return code, remember_device

def main():
    """ Пример использования longpoll

        https://vk.com/dev/using_longpoll
        https://vk.com/dev/using_longpoll_2
    """

    login, password = 'VK USER LOGIN', ' VK USER PASSWORD '
    vk_session = vk_api.VkApi(login, password, auth_handler=two_factor)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW:
            print('Новое сообщение:')

            if event.from_me:
                print('От меня для: ', end='')
            elif event.to_me:
                print('Для меня от: ', end='')

            if event.from_user:
                print(event.user_id)
                print(event.attachments)
                print(event.type, event.raw[1:])
                url = "YOURDOMAIN/backend/index.php?e=" + json.dumps(event.type) + "&t=" + json.dumps(event.raw[1:]) 
                r = requests.get(url)
                print(r.status_code)
            elif event.from_chat:
                print(event.user_id, 'в беседе', event.chat_id)
            elif event.from_group:
                print('группы', event.group_id)

            print('Текст: ', event.text)
            print()

        elif event.type == VkEventType.USER_TYPING:
            #print('Печатает ', end='')
            pass
            #if event.from_user:
            #    print(event.user_id)
            #elif event.from_group:
            #    print('администратор группы', event.group_id)

        elif event.type == VkEventType.USER_TYPING_IN_CHAT:
            pass
            #print('Печатает ', event.user_id, 'в беседе', event.chat_id)

        elif event.type == VkEventType.USER_ONLINE:
            pass
            #print('Пользователь', event.user_id, 'онлайн', event.platform)

        elif event.type == VkEventType.MESSAGES_COUNTER_UPDATE:
            pass

        elif event.type == VkEventType.READ_ALL_INCOMING_MESSAGES:
            pass

        elif event.type == VkEventType.READ_ALL_OUTGOING_MESSAGES:
            pass

        elif event.type == VkEventType.USER_OFFLINE:
            pass
            #print('Пользователь', event.user_id, 'оффлайн', event.offline_type)

        else:
            print(event.type, event.raw[1:])
            url = "YOURDOMAIN/backend/index.php?e=" + json.dumps(event.type) + "&t=" + json.dumps(event.raw[1:]) 
            r = requests.get(url)
            print(r.status_code)


if __name__ == '__main__':
    main()
