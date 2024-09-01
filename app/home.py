from pay_wall import  pay_wall_server
from pay_wall import pay_verification  
from pay_wall import settings
from pay_wall import pay_walldb  



@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8000, debug=True)
