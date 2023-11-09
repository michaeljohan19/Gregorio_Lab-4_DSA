from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/uppercase', methods=['GET', 'POST'])
def uppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    result = None
    if request.method == 'POST':
        input_integer = request.form.get('inputInteger', '')
        if input_integer and input_integer.isdigit():
            input_integer = int(input_integer)
            result = input_integer ** 2 * 3.14
    return render_template('circle.html', result=result)

@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    result = None
    if request.method == 'POST':
        input_base = request.form.get('input_base', '')
        input_height = request.form.get('input_height', '')
        
        if input_base and input_base.isdigit() and input_height and input_height.isdigit():
            input_base = int(input_base)
            input_height = int(input_height)
            result = (input_base * input_height)/2
    return render_template('triangle.html', result=result)

@app.route('/contacts')
def contact():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)
