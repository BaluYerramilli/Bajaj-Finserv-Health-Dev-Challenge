from flask import Flask, request, jsonify

app = Flask(__name__)

def seperation(full_list):
    alphabets = []
    numbers = []

    for item in full_list:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
    return alphabets,numbers

@app.route('/bfhl', methods=['POST', 'GET'])
def search_devices():
    try:
        if request.method == "POST":
            data = request.json  # Parse the JSON data from the request
            values = data.get('data')
            # Your logic here (e.g., querying a database, processing data)
            alphabets,numbers = seperation(values)
            highest = sorted(alphabets)
            response_data = {
                'is_success': True,
                'user_id': 'john_doe_17091999',
                'email': 'john@xyz.com',
                'roll_number': 'ABCD123',
                'numbers': [numbers],
                'alphabets': [alphabets],
                'highest_alphabet': [highest[-1]]
            }
            return jsonify(response_data), 200
        else:
            response_data = {'Operation_code': 1}
            return jsonify(response_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
