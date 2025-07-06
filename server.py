from flask import Flask, request, render_template, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detection():
    text_to_analyze = request.form['textToAnalyze']
    result = emotion_detector(text_to_analyze)

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return render_template('index.html', response=formatted_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
