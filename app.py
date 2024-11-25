from flask import Flask, jsonify
from tiktok_script import get_trending_hashtags

app = Flask(__name__)

@app.route('/trending-hashtags', methods=['GET'])
def trending_hashtags():
    hashtags = get_trending_hashtags()
    return jsonify(hashtags)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
