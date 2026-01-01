from flask import Flask, render_template ,redirect, url_for ,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page')
def page1():
    return render_template('page1.html')

### result cheacker html page 
@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        data = request.form['data']
        # Process the data as needed
        return redirect(url_for('result'))












if __name__ == '__main__':
    app.run(debug=True)