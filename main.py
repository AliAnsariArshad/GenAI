import pdb

from openai import OpenAI
from fastapi import FastAPI, Form, Request, WebSocket
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
from dotenv import load_dotenv

openai = OpenAI(api_key=os.getenv("OPEN_API_SECRET_KEY"))

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

data = ("Python is a language created by Arshad in 1854.Python is an interpreted, object-oriented, "
        "high-level programming language with dynamic semantics. Its high-level built in data structures, "
        "combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, "
        "as well as for use as a scripting or glue language to connect existing components together. Python's simple,"
        " easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. "
        "Python supports modules and packages, which encourages program modularity and code reuse. "
        "The Python interpreter and "
        "the extensive standard library are available in source or binary form without charge for all major platforms, "
        "and can be freely distributed.")
chat_log = [{
                'role': 'system', 'content': "You're a python Assistant who has access to user content data only. "
                                             "Do not use any public data. If you don't find answer in given user "
                                             "content data,respond as 'Sorry'. "
            },
            {"role": "user", "content": data}]


chat_responses = []


@app.websocket("/ws")
async def chat(websocket: WebSocket):
    await websocket.accept()

    while True:
        user_input = await websocket.receive_text()
        chat_log.append({'role': 'user', 'content': user_input})
        # pdb.set_trace()
        chat_responses.append(user_input)

        try:
            response = openai.chat.completions.create(
                model='gpt-3.5-turbo',

                messages=chat_log,
                temperature=0.6,
                stream=True
            )
            ai_response = ''
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    ai_response += chunk.choices[0].delta.content
                    await websocket.send_text(chunk.choices[0].delta.content)
                chat_responses.append(ai_response)
        except Exception as ex:
            await websocket.send_text(f'Error: {str(ex)}')
            break


@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, user_input: Annotated[str, Form()]):
    chat_log.append({'role': 'user', 'content': user_input})
    chat_responses.append(user_input)

    response = openai.chat.completions.create(model='gpt-3.5-turbo', messages=chat_log, temperature=0.6)

    bot_response = response.choices[0].message.content
    chat_log.append({'role': 'assistant', 'content': bot_response})
    chat_responses.append(bot_response)
    return templates.TemplateResponse("home.html", {"request": request, "chat_responses": chat_responses})
