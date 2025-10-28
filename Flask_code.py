from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        user_message = request.form['message']
        message = f"Thank you {name}! Your message has been received."

    # open your html file manually
    with open("index.html") as file:
        html = file.read()

    return render_template_string(html, message=message)

if __name__ == '__main__':
    app.run(debug=True)
