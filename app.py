from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def welcome_page():
    """Returns 'welcome' to the browser."""

    return "<p>welcome</p>"

@app.get('/welcome/<page>')
def welcome_specific_page(page):
    """Welcomes user to specific page"""

    return f"<p>welcome {page}</p>"