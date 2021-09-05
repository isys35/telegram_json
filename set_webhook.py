import requests
import config


def set_webhook():
    url = 'https://api.telegram.org/bot{}/setWebhook?url={}'.format(config.TOKEN, config.URL_WEBHOOK)
    response = requests.get(url)
    if response.status_code == 200 and response.json()['result']:
        print('Вебхук установлен')
    else:
        raise Exception('Вебхук не установлен')


if __name__ == '__main__':
    set_webhook()
