from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/", method= ['POST', 'GET'])
def render_main():
    return render_template('home.html')

@app.route("/response", method= ['POST', 'GET'])
def render_response():
    if request.method == 'POST':
        favorite_color = request.form['color'] #get user's input for color input
        if favorite_color == 'pink':
            response = "That's my favorite color!"
        else:
            response = "Ok."
    return render_template('response.html', responseFromServer=response)
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
