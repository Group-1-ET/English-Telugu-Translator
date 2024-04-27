from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    sentence = request.form['sentence']

    if sentence:
        # Construct the command
        command = ["python3", "pages/model/inference.py", "--text", sentence, "-l", "te"]
        print(command)
        print(sentence)
        # Run the command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Capture the output and error messages
        output, error = process.communicate()
        
        return render_template('result.html', sentence=sentence, output=output.decode(), error=error.decode())

    return "No sentence provided."

if __name__ == '__main__':
    app.run(debug=True)
