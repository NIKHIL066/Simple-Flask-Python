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
