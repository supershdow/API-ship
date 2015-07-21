from flask import Flask, render_template
import util

app=Flask(__name__)

@app.route('/')
@app.route('/<city>')
def root(city='nyc'):
    w=util.get_weather(city)
    t=util.toFahrenheit(w)
    if t>110:
        pepper='Ghost Pepper'
    elif 50<t<=110:
        pepper='Jalapeno Pepper'
    else:
        pepper='Sweet Bell Pepper'
    return render_template('weather.html', weather=t, pepper=pepper)

if __name__=='__main__':
    app.debug=True
    app.run()
