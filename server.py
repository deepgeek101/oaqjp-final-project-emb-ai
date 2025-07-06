from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detection():
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze is None or text_to_analyze.strip() == '':
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    # Check for None result (error case)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
