class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paystack_id = db.Column(db.String(50), unique=True, nullable=False)
    reference = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    paid_at = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.String(50), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    authorization_code = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<Transaction {self.reference}>'


with app.app_context():
    db.create_all()

