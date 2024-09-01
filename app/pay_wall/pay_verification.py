import os
import requests
from settings import app, db

PAYSTACK_SECRET_KEY = os.getenv('PAYSTACK_SECRET_KEY', 'sk_test_13b0d842352136d91e09139441abed6d951ab516')
def response(reference):
    try:
        url = f"https://api.paystack.co/transaction/verify/{reference}"
        headers = {
            "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json().get('data')
        transaction = Transaction(
            paystack_id=data['id'],
            reference=data['reference'],
            status=data['status'],
            amount=data['amount'],
            currency=data['currency'],
            paid_at=data['paid_at'],
            created_at=data['created_at'],
            customer_email=data['customer']['email'],
            authorization_code=data['authorization']['authorization_code'] if data['authorization'] else None
        )
        db.session.add(transaction)
        db.session.commit()
        return {"message": "you have just sent money to this vendor."}, 200
        
    except requests.exceptions.RequestException as req_err:
        raise RuntimeError(f"Request error: {str(req_err)}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")

