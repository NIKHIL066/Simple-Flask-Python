from flask import Flask,render_template,url_for,redirect

template_path='C:\\Python36\\Flask_Project_2\\template'
app=Flask(__name__,template_folder=template_path)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/user/<name>')
def user(name):
    if name == 'index':
        return redirect(url_for('index'))
    elif name == 'home':
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
    
 """
 In this code , the usage of redirect, url_for,variable is shown.
 To run the code type localhost:5000/user/home -- it renders the home page
                      localhost:5000/user/index -- it renders the index page
 """
