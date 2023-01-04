from flask import Flask, render_template, request, flash
import re 

app = Flask(__name__)
app.secret_key = "andrei_andrei99"

@app.route("/hello")
def index():
	flash("Enter some text in the form below:")
	return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
	text = request.form["name_input"]
	for key, value, in word_dict.items():
		text = re.sub(r"\b" + key + r"\b", value, text)
	flash(text)
	return render_template("index.html")

word_dict = {
	"on fleek": "well-groomed",
	"lit AF": "extremely energetic",
 	"salty": "upset",
 	"on point": "accurate",
 	"savage": "fierce",
 	"turnt": "energized",
 	"ghost": "avoid",
 	"thicc": "full-figured",
 	"is not": "ain't",
 	"going to": "gonna",
 	"want to": "wanna", 
 	"give me": "gimme",
 	"have to": "gotta",
 	"you all": "y'all",
 	"kind of": "kinda",
 	"sort of": "sorta",
 	"I'm": "I am",
 	"you're": "you are",
 	"he's": "he is",
 	"she's": "she is",
 	"it's": "it is", 
 	"we're": "we are",
 	"they're": "they are",
 	"won't": "will not",
 	"can't": "cannot",
 	"don't": "do not",
 	"Me": "myself",
 	"he": "him",
 	"she": "her",
 	"it": "which",
 	"we": "us",
 	"they": "them",
}