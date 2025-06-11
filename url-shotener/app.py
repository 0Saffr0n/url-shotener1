from flask import Flask, request, redirect, jsonify
import random
import string
import os

app = Flask(__name__)

url_database = {}

def generate_short_code():
    """Generate a random 6-character code"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Create a short URL"""
    data = request.json
    
    if not data or 'url' not in data:
        return jsonify({"error": "URL is required"}), 400
    
    long_url = data['url']
    short_code = generate_short_code()
    
    while short_code in url_database:
        short_code = generate_short_code()
    
    url_database[short_code] = long_url
    
    short_url = f"http://{request.host}/{short_code}"
    
    return jsonify({
        "short_url": short_url,
        "original_url": long_url
    }), 201

@app.route('/<short_code>', methods=['GET'])
def redirect_url(short_code):
    """Redirect to the original URL"""
    if short_code not in url_database:
        return jsonify({"error": "URL not found"}), 404
    
    return redirect(url_database[short_code], code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)