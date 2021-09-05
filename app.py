import json

import telebot
import uvicorn
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route
import config


async def send_json(request: Request):
    data = await request.json()
    with open(config.JSON_FILE_NAME, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    bot = telebot.TeleBot(config.TOKEN, threaded=False)
    bot.send_document(config.CHAT_ID, open(config.JSON_FILE_NAME, 'rb'))
    return JSONResponse({'status': True})


app = Starlette(debug=True, routes=[
    Route('/webhook', send_json, methods=['POST']),
])

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
