from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sentence = request.form['sentence']

        if sentence:
            # Construct the command
            command = ["python3", "pages/model/inference.py", "--text", sentence, "-l", "te"]

            # Run the command
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Capture the output and error messages
            output, error = process.communicate()

            # Return the output directly
            return output.decode()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
