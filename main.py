import requests
import random


ACCESS_TOKEN = raw_input("Access Token: ")

UUID = raw_input("UUID: ")

headers = {
    'pragma': 'no-cache',
    'origin': 'https://event.crowdcompass.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,es-US;q=0.8,es;q=0.6,ru-BY;q=0.4,ru;q=0.2,en;q=0.2',
    'access-token': ACCESS_TOKEN,
    'content-type': 'application/json',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'cache-control': 'no-cache',
    'authority': 'game.crowdcompass.com',
    'referer': 'https://event.crowdcompass.com/2019techintern/activity/anzXndMzGS',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Mobile Safari/537.36',
}

def construct_event_submission_data(trigger, i):
    # Trigger -> String representing the Achievement Name
    # i -> Integer representing an iterating number
    # UUID is not passed, as it seems like it can be any 9 digit integer
    return '{"player_actions":[{"uuid":' + ''.join([str(random.randint(1, 9)) for i in range(9)]) + ',"trigger_name":"' + trigger + '","triggered_at":"2019-06-02T17:28:35.' + str(i) + '7Z"}]}'

def complete_event(trigger, i):
    # Completes each event on the Onboarding achievements page
    data = construct_event_submission_data(trigger, i)
    response = requests.post('https://game.crowdcompass.com/games/E2HnUZ3rp1/players/{}/actions'.format(UUID), headers=headers, data=data)
    print response.text


def get_stats():
    # Gets the achievements that the current account can obtain
    params = (
        ('_release', '2019050100'),
    )
    response = requests.get('https://game.crowdcompass.com/games/E2HnUZ3rp1/players/{}'.format(UUID), headers=headers, params=params)
    return response.json()

if __name__ == '__main__':
    for e in range(3):
        for i, val in enumerate(get_stats()['player']['progress']):
            complete_event(val['trigger_name'], i+(30*e))
