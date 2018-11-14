"""
The following code renders an html on a host server.
Note: A folder named 'template' has to be created in the folder where python file is present and all the html files must be saved in that folder
"""
from flask import Flask, render_template

template_path='C:\\Python36\\Flask Projects\\template'

app=Flask(__name__,template_folder=template_path)

@app.route('/')

def index():
    try:
        return render_template('home.html')
    except Exception as e:
        print('Error: {0}'.format(e))
        exit()
if __name__ == '__main__':
    app.run(debug=True)
