from flask import Flask, render_template
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('./../cd2020.crt', './../cd2020.key')

app = Flask(__name__)

@app.route('/') 
def hello_world():
    return 'Hello, From Flask!'

@app.route('/drawROC')
def drawROC():
    return render_template("drawROC.html")
    
if __name__== '__main__': 
	app.run(ssl_context=context)