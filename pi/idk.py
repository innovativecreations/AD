from flask import *
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['video']
        save_path = '/home/pi/videos/video.mp4'
        print('Saving video to:', save_path)  # Debugging statement
        try:
            file.save(save_path)
            return 'Video saved successfully!'
        except Exception as e:
            print('Error saving video:', str(e))  # Debugging statement
            return 'Error saving video'
    return render_template('index.html')

app.run(debug=True, host='0.0.0.0', port=5000)
