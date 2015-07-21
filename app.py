from flask import Flask, render_template
import util

app=Flask(__name__)

@app.route('/')
@app.route('/<city>')
def root(city='nyc'):
    w=util.get_weather(city)
    t=util.toFahrenheit(w)
    if t>95:
        pepper='Ghost Pepper'
        image='ghost-pepper'
    elif 50<t<=95:
        pepper='Jalapeno Pepper'
        image='Jalapeno'
    else:
        pepper='Sweet Bell Pepper'
        image='Bell-pepper'
    return render_template('weather.html', weather=t, pepper=pepper, image=image)

@app.route('/sloth')
def sloth():
    return render_template('sloth.html',image=util.flickr())


if __name__=='__main__':
    app.debug=True
    app.run()
