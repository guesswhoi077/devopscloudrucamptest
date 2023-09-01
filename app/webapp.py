from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/hostname', methods=['GET'])
def get_hostname():
	return jsonify({'hostname':  socket.gethostname() })


@app.route('/author', methods=['GET'])
def get_author():
	return jsonify({'author': os.environ.get('USER') })


@app.route('/id', methods=['GET'])
def get_id():
	return jsonify({'UUID': os.environ.get('UUID') })


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))