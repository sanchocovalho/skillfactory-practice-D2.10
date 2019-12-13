import sentry_sdk
import os
import bottle
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_dns = os.environ.get('SENTRY_DNS')
# sentry_dns = "https://04ebf20152fb484aa8d39a256702dbcb@sentry.io/1855958"
app = bottle.Bottle()

sentry_sdk.init(
	dsn = sentry_dns,
    integrations = [BottleIntegration()]
)

@app.route('/')
def index():
	html = """
<!doctype html>
<html lang="ru">
  <head>
    <title>Стартовая страница</title>
  </head>
  <body>
    <div style="margin:0 30px;text-align:center;">
      <h1 style="font-size:40px;color:blue;">
      Привет Всем, кто зашёл на данную страницу!
      </h1>
      <p style="font-size:25px;color:green;">Пройдите по ссылкам ниже,
      чтобы посмотреть работу данного сервера совместно с 
      <span style="color:red;">SENTRY.IO</span>.</p>
      <p style="font-size:40px;">
      <a href="/success">SUCCESS</a> | <a href="/fail">FAIL</a>
      </p>
    </div>
  </body>
</html>
"""
	return html

@app.route('/success')
def success():
	html = """
<!doctype html>
<html lang="ru">
  <head>
    <title>Сообщение об успехе</title>
  </head>
  <body>
    <div style="margin:0 30px;text-align:center;">
      <h1 style="font-size:35px;color:blue;">
      Тестовая страница проверки работы сервера с 
      <span style="color:red;">SENTRY.IO</span>!
      </h1>
      <p style="font-size:25px;color:green;">Если вы видите это сообщение, 
      значит данный сервер передает сообщения об ошибках на платформу 
      <span style="color:red;">SENTRY.IO</span>.</p>
    </div>
  </body>
</html>
"""
	return html

@app.route('/fail')
def fail():
    raise RuntimeError("Сообщение об ошибке: RuntimeError")

if os.environ.get('APP_LOCATION') == 'heroku':
    bottle.run(app,
               host="0.0.0.0",
               port=int(os.environ.get("PORT", 5000)))
else:
    bottle.run(app,
               host='localhost',
               port=5000)