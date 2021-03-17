# flask app to hold the ner model
# to run locally
# pip install -U pip setuptools wheel
# pip install spacy
import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_trf")

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def show_user_input_form():
  return render_template('predictorform.html')

@app.route('/results', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
      #write your function that loads the model
      data = request.form['data']
      doc = nlp(data)
      prediction = []
      words = []
      ent_to_keep = ["PERSON", "NORP", "FAC", "ORG", "GPE", "LOC", "PRODUCT",
       "EVENT", "WORK_OF_ART", "LANGUAGE", "MONEY", "LAW"]
      for ent in doc.ents: 
          entity = (ent.text, ent.label_)
          if ent.label_ in ent_to_keep:
            prediction.append(entity)
 
    return render_template('resultsform.html', data = data,
     prediction = prediction)


if __name__ == "__main__":
    app.run(debug = True)

