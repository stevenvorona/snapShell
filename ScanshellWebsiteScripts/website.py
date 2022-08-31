import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def sendData():
    # GET request
    if request.method == 'GET':
        username = request.args.get('username', default = 'emmettmiller', type = str)
        print(username)
        url = "https://feelinsonice.appspot.com/web/deeplink/snapcode?username=" + username + "&size=320&type=SVG"

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        #Get dot data
        dots = soup.findAll('path')[0]
        dotsData = dots['d']

        #Get bitmoji data
        bitmoji = soup.findAll('image')[0]
        bitmojiData = bitmoji['xlink:href']

        #Get specific dot outline data
        background = soup.findAll('path')[1]
        backgroundData = background['d']

        #Get svg data
        svg = soup.findAll('svg')[0]
        svgNumOne = svg['width']
        svgNumTwo = bitmoji['x']

        print(svgNumOne)
        print(svgNumTwo)

        message = {'dotsData':dotsData, 'bitmojiData':bitmojiData, 'backgroundData':backgroundData, 'svgNumOne':svgNumOne, 'svgNumTwo':svgNumTwo}
        return jsonify(message)  # serialize and use JSON headers


def test_page():
    # look inside `templates` and serve `index.html`
    return render_template('test.html')

if __name__ == "__main__":
    app.run()
