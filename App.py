from flask import Flask, render_template, request, jsonify
import requests

# search about f'' and request and to_dict

app = Flask(__name__)

API_BASE_URL = 'https://jsonplaceholder.typicode.com'

@app.route("/")
def index():
  response = requests.get(f'{API_BASE_URL}/users')
  employees = response.json()
  return render_template('index.html', employees=employees)

@app.route("/create", methods=['POST'])
def create_employee():
  data = request.form.to_dict()
  response = requests.post(f'{API_BASE_URL}/users', json=data)
  new_employee = response.json()
  return jsonify(new_employee), 201

if __name__ == "__main__":
  app.run(debug=True) 