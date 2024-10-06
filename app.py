from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "pass1234"

debug = DebugToolbarExtension(app)

@app.route("/")
def get_home():
    """ Generates the Homepage Description """
    return render_template("index.html")

@app.route("/madlib_form")
def get_madlib():
    """ Generates and shows the form for user input """
    prompts = story.prompts

    return render_template("madlib_form.html", prompts=prompts)


@app.route("/madlib_story")
def get_story():
    """ Creates the final Story Based on the User inputs """
    complete_story = story.generate(request.args)

    return render_template("madlib_story.html", completed_madlib = complete_story)