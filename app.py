from flask import Flask, render_template, request
from DataBase import get_job_order_data

app = Flask(__name__)
@app.route('/order_tracking', methods=['POST'])
def order_tracking():
    job_order_data = {} 
    invalid_order = False  
    if request.method == 'POST':
        order_number = request.form['order_number']
        if order_number:
            job_order_data = get_job_order_data(order_number)
            if not job_order_data:
                invalid_order = True
        else:
            invalid_order = True
    return render_template('index.html', job_order_data=job_order_data, invalid_order=invalid_order)
@app.route('/')
def index():
    return render_template('index.html', invalid_order=False)
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
