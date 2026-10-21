from flask import Flask, render_template

# Point Flask to load templates directly from the root directory
app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
