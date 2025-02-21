# url = "https://google.com"
# print(url)/
# domain = "google.com"
# age = 5
# is_safe = False
# print (is_safe)
# blacklist = ["phishing.com", "fakesite.net"]
# whois_data = {"domain" : "phishing.com", "age" : 5}
# print(whois_data)
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return "hello there, i'm yash."
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return '''
        <h2>Phishing Detection</h2>
        <form action="/check" method="post">
            <input type="text" name="url" placeholder="Enter a URL">
            <button type="submit">Check</button>
        </form>
        '''
@app.route('/check', methods=['post'])
def check_url():
    url = request.form.get('url')
    return f"<h3>You entered: {url}</h3>"
        
if __name__ == '__main__':
    app.run(debug=True)
