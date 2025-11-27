from flask import Flask #Flask library se Flask class ko import kar rahe ho , Jisse hum web app bana sakte hain.

app = Flask(__name__) # app naam ka ek Flask application bana rahe h , __name__ se Flask ko pata chalta hai ki ye file main program hai.

#home page
@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>My Portfolio</title>
        <style>
            body { 
                font-family: Arial; 
                background: #f2f2f2; 

                text-align: center;
                padding: 40px;
            }
            .box {
                background: white;
                padding: 20px;
                width: 60%;
                margin: auto;
                border-radius: 10px;
                box-shadow: 0px 0px 10px #aaa;
            }
            h1 { color: #333; }
            h2 { color: #666; }
            a { 
                text-decoration: none; 
                color: blue; 
                font-size: 18px; 
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>Welcome to My Portfolio</h1>
            <h2>I created this website using Flask</h2>
            <br>
            <a href="/about">Go to About Page</a>
        </div>
    </body>
    </html>
    """

#about page
@app.route("/about")
def about():
    return """
    <html>
    <head>
        <title>About Me</title>
        <style>
            body { 
                font-family: Arial; 
                background: #f2f2f2; 
                text-align: center;
                padding: 40px;
            }
            .box {
                background: white;
                padding: 20px;
                width: 60%;
                margin: auto;
                border-radius: 10px;
                box-shadow: 0px 0px 10px #aaa;
            }
            h1 { color: #333; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>This is my About Page</h1>
            <p>I am learning Python and Flask. This is my simple website.</p>
            <br>
            <a href="/">Back to Home</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
