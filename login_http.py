from flask import Flask, render_template,request,redirect,url_for

#template folder which holds the html files to be rendered
template_path='C:\\Python36\\Flask_Project_3\\template'


app=Flask(__name__,template_folder=template_path)


@app.route('/success/<key>')
def success(key):
    if key == 'root':
        return 'You have successfully logged in!!!!'
    else:
        return "Sorry!!! couldn't find the user"

#This method will run on submitting the form
@app.route('/login',methods=['POST','GET'])
def login():
    try:
        if request.method == 'POST':
            username=request.form['username']
            password=request.form['password']
            return redirect(url_for('success',key=password)) #First argument is the method name, second is the argument passed to the method
        
        else:
            username=request.args.get['username']       
            return redirect(url_for('success',name=username))
    except Exception as e:
        print('Error: {0}'.format(e))
        
if __name__=='__main__':
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True)
