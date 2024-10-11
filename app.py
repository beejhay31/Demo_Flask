from flask import Flask, render_template, request, redirect, url_for, session, flash
from my_app.classification import load_iris_data, perform_eda, train_model, model_performance
from my_app.monitoring import Monitoring
from my_app.model import Model
from my_app.view import View
from sklearn.model_selection import train_test_split

app = Flask(__name__)
app.secret_key = '5ef4c21a90e37177c7df457473080385'  # For session management

# Predefined valid 7-digit login codes
VALID_CODES = ["1234567", "2345678", "3456789", "4567890", "5678901", "6789012", "7890123"]

# Initialize login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        login_code = request.form['login_code']

        if not email.endswith('@datadock.ai'):
            flash('Invalid email domain. Only @datadock.ai email addresses are allowed.', 'error')
        elif login_code in VALID_CODES:
            session['email'] = email
            session['logged_in'] = True
            flash('You are now logged in.')
            return redirect(url_for('main_app'))
        else:
            flash('Invalid login code. Please try again.', 'error')
    
    return render_template('login.html')

@app.route('/main_app')
def main_app():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    return render_template('main_app.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
