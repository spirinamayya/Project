from flask import Flask, render_template
import pandas as pd

data = pd.read_csv('static/file1/menu.csv')


app = Flask(__name__)



@app.route('/')
def index():
    df = data.head(7)
    return render_template('index.html')


@app.route('/plot1')
def returnPage():
    return render_template("plot1.html")


@app.route('/table')
def onTable():
    return render_template('tablem.html')


@app.route('/plot2')
def returnPage2():
    return render_template("plot2.html")

@app.route('/plot3')
def returnPage3():
    return render_template("plot3.html")

@app.route('/plot4')
def returnPage4():
    return render_template("plot4.html")

@app.route('/plot5')
def returnPage5():
    return render_template("plot5.html")

@app.route('/plot6')
def returnPage6():
    return render_template("plot6.html")

@app.route('/plot7')
def returnPage7():
    return render_template("plot7.html")

@app.route('/plot8')
def returnPage8():
    return render_template("plot8.html")




if __name__ == '__main__':
    app.run()
