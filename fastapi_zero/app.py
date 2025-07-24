from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


@app.get(
    '/items/{item_id}', status_code=HTTPStatus.OK, response_class=HTMLResponse
)
def read_root_html():
    cod_html = """
                <html>
                    <title>Olá Mundo!</title>
                    <body>
                        <h1>Olá Mundo!</h1>
                    </body>
                </html>
                """
    return cod_html
