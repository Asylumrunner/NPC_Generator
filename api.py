from flask import Flask, jsonify, request
from generator import generate_characters
app = Flask(__name__)

@app.route('/characters/<int:numChars>')
def generate_character_endpoint(numChars=1):
    query_string = request.args
    user_supplied_attributes = []
    if 'att' in query_string:
        user_supplied_attributes = query_string.getlist('att')
    response = generate_characters(numChars, user_supplied_attributes)
    return jsonify(response)

app.run()
