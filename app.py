from flask import *
app=Flask(__name__)

@app.route('/')
def index():
    email=request.cookies.get('useremail')
    if email:
        return render_template('profile.html',useremail=email)
    return render_template('index.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        print(email+" "+password)
        if email=='ram@gmail.com' and password=='abcd1234':
            resp=make_response(redirect('/profile'))
            resp.set_cookie('useremail',email)
            return resp
        else:
            return render_template('login.html',loginfailedStatus=True)
    elif request.method=='GET':
        email=request.cookies.get('useremail')
        if email:
            return render_template('profile.html',useremail=email)
        return render_template('login.html',loginfailedStatus=False)

@app.route('/profile')
def profile():
    email=request.cookies.get('useremail')
    if email:
        return render_template('profile.html',useremail=email)
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    resp=make_response(redirect('/login'))
    resp.delete_cookie('useremail')
    return resp


if __name__=='__main__':
    app.run(debug=True)