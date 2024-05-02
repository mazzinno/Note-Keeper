from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if len(password) < 7:
            flash('Password must be at least 7 characters long.', category='error')
        else:
            flash('Account Created!', category='success')
    return render_template('loginpage.html')


@auth.route('/signup')
def signup():
    return render_template('signup.html')
