import vk
import requests
from getpass import getpass


def get_user_login():
    return input('Login: ')


def get_user_password():
    return getpass()


def get_online_friends(api, api_version):
    id_friends_online = api.friends.getOnline(version=api_version)
    return api.users.get(version=api_version, user_ids=id_friends_online)


def get_api(login, password, app_id):
    session = vk.AuthSession(
        app_id=app_id,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    return vk.API(session)


def output_friends_to_console(friends_online):
    print('Friends online:')
    for friend in sorted(friends_online, key=lambda x: x['last_name']):
        print('{0} {1}'.format(friend['last_name'], friend['first_name']))


if __name__ == '__main__':
    try:
        app_id = 6394729
        api_version = 5.73
        login = get_user_login()
        password = get_user_password()
        api = get_api(login, password, app_id)
        output_friends_to_console(get_online_friends(api, api_version))
    except vk.exceptions.VkAuthError:
        exit('Authentications Error')
    except requests.exceptions.ConnectionError:
        exit('No connection')
