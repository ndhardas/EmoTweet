
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from test import do_calculation, get_happy, get_sad, indv_pol
from flask_bootstrap import Bootstrap #new

app = Flask(__name__)
Bootstrap(app) #new
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        username = ""

        if username != request.form["username"]:
            username = str(request.form["username"])
            result = do_calculation(username)
            happy = get_happy(username)

            sad = get_sad(username)
            indv_pol("lol")
            print(happy)
            print(sad)

            #result = "lol"
            return '''
                <html>
                    <head>
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                    </head>
                    <body style="background-color:LIGHTCYAN;">
                        <div class="text-center">
                        <p>  </p>
                        <img src="https://image.flaticon.com/icons/png/512/23/23681.png" height="30" width="30">
                        <p class="h2"> EmoTweet</p>
                        <p>User: {username}</p>
                        <p>{result}</p>
                        <p>{happy}</p>
                        <p>{sad}</p>
                            <p><a href="/" class="text-primary">Run again</a>
                        </div>
                        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
                    </body bg color = "42EAF5">
                </html>
            '''.format(result=result, happy=happy, sad=sad, username=username)
        else:

            errors += "<p class=\"text-danger\"> Please enter a username. </p>\n".format(request.form["username"])

    return '''
        <html>
            <head>
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
            </head>
            <body style="background-color:LIGHTCYAN;">
                <div class="text-center">
                    <p>  </p>
                    <img src="https://image.flaticon.com/icons/png/512/23/23681.png" height="30" width="30">
                    <p class="h2"> EmoTweet</p>
                    <p>Enter a username without the '@':</p>
                    <form method="post" action=".">

                            <div class="input-group flex-nowrap">
                                <div class = "c">
                                    <span class="input-group-text" id="basic-addon1">@</span>
                                </div>
                                <input name = "username" type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1">
                            </div>

                        <p>{errors}</p>
                        <p><input type="submit" value="Calculate" class="btn btn-outline-dark style="background-color:CORNFLOWERBLUE;" /></p>
                        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
                    </form>
                </div>
            </body>
        </html>
    '''.format(errors=errors)

