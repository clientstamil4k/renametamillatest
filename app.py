#Thank you TG_UPDATES1 for helping me in this journey !
#Must Subscribe On YouTube @TG_UPDATES1 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@TG_UPDATES1'


if __name__ == "__main__":
    app.run()
