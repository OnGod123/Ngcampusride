from flask import Flask, request, jsonify
import requests
from app.home import app
app = Flask(__name__)

@app.route('/initialize_payment', methods=['POST'])
def initialize_payment():
    try:
        # Get data from the request
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        email = data.get('email')
        amount = data.get('amount')

        # Validate inputs
        if not email or not isinstance(amount, (int, float)):
            return jsonify({'error': 'Email and amount are required, and amount must be a number'}), 400

        # Paystack API endpoint
        url = "https://api.paystack.co/transaction/initialize"

        # Set headers for the request
        headers = {
        "Authorization": "Bearer sk_test_13b0d842352136d91e09139441abed6d951ab516",  # Your Paystack secret key
        "Content-Type": "application/json"
        }


        # Prepare the payload
        payload = {
            "email": email,
            "amount": int(amount * 100)  # Convert amount to kobo (smallest currency unit in NGN)
        }

        # Make the POST request to Paystack
        response = requests.post(url, json=payload, headers=headers)

        # Check for response status
        if response.status_code != 200:
            response_data = response.json()
            return jsonify({'error': response_data.get('message', 'Error during transaction initialization')}), response.status_code

        # Return the authorization URL to the user
        response_data = response.json()
        return jsonify({
            'status': response_data['status'],
            'message': response_data['message'],
            'authorization_url': response_data['data']['authorization_url'],
            'access_code': response_data['data']['access_code'],
            'reference': response_data['data']['reference']
        }), response.status_code

    except requests.exceptions.RequestException as req_err:
        return jsonify({'error': 'Request error: ' + str(req_err)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

