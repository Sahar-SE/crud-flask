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
  print("Received data:", data)
  response = requests.post(f'{API_BASE_URL}/users', json=data)
  new_employee = response.json()
  return jsonify(new_employee), 201


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        # Get the employee ID from the form data
        employee_id = int(request.form.get('id'))
        
        # Fetch the existing employee data
        response = requests.get(f'{API_BASE_URL}/users/{employee_id}')
        employee_data = response.json()
        
        # Update the employee data
        employee_data['name'] = request.form['name']
        employee_data['email'] = request.form['email']
        employee_data['phone'] = request.form['phone']
        
        # Send PUT request to update the employee
        response = requests.put(f'{API_BASE_URL}/users/{employee_id}', json=employee_data)
        updated_employee = response.json()
        
        return jsonify(updated_employee), 200
        

@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_employee(user_id):
    response = requests.delete(f'{API_BASE_URL}/users/{user_id}')
    print("API Response for delete:", response.status_code)
    
    # Fetch all users again to get the updated list
    response = requests.get(f'{API_BASE_URL}/users')
    updated_employees = response.json()
    
    return jsonify(updated_employees), 200, {'Content-Type': 'application/json'}

if __name__ == "__main__":
  app.run(debug=True) 
