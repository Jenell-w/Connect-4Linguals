**Connect4 Linguals is a 2 player game, updated in real time, where players select a topic and enter words in order to get 4 in a row. To run the game you must install some dependencies as listed below. All game data is saved in HarperDBCloud database so as to easily retrieve it for future use. User data is stored securely.**

**_Running_**
_-In one terminal tab:_

1. `cd client`
2. `npm install`
3. `npm install vue-router`
4. `npm install socket.io-client vue-socket.io --save`
5. `npm run build`

_-In a new tab:_

1. `cd server`
2. `pipenv install`
3. `pipenv install requests`
4. `pipenv install bcrypt`
5. `pipenv install flask-socketio`
6. `pipenv install gevent`
7. `pipenv run python app.py`
