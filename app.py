from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():


    if request.method == 'POST':
        input1 = request.form['from']
        input2 = request.form['to']
        input3 = request.form['amount']

        # Replace the API endpoint and parameters with the actual API you are working with
        api_url = f'http://api.exchangerate.host/convert?access_key=e699c163003c8887e2835efd5fac2237&from={input1}&to={input2}&amount={input3}'
        
        try:
            # Make API request
            response = requests.get(api_url)
            data = response.json()
            print(data)

            return render_template('holden.html', data=data)

        except Exception as e:
            error_message = f'Error fetching data: {str(e)}'
            return render_template('holden.html', error_message=error_message)

    return render_template('holden.html', data=None, error_message=None)

if __name__ == '__main__':
    app.run(debug=True)
