# flask app to hold the ner model
# to run locally
# pip install -U pip setuptools wheel
# pip install spacy
import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_trf")
zh_nlp = spacy.load("zh_core_web_trf")
from flask import Flask, render_template, request, jsonify
from chinese_dictionary import add_pinyin
app = Flask(__name__)

@app.route('/')
def show_user_input_form():
	return render_template('predictorform.html')


@app.route('/results', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
      #write your function that loads the model
      language = request.form['language']
      data = request.form['data']
      if language == "English":
        doc = nlp(data)
      elif language == "Chinese":
      	doc = zh_nlp(data)
      prediction = []
      words = []
      ent_to_keep = ["PERSON", "NORP", "FAC", "ORG", "GPE", "LOC", "PRODUCT",
       "EVENT", "WORK_OF_ART", "LANGUAGE", "MONEY", "LAW"]
      for ent in doc.ents: 
          entity = (ent.label_, ent.text)
          if ent.label_ in ent_to_keep:
            prediction.append(entity)
            if language == "Chinese":
              pronunciation = add_pinyin.add_pinyin(ent.text)
              prediction.append(pronunciation)
    # return jsonify(data=data, prediction= prediction)
    return render_template('resultsform.html', data = data,
     prediction = prediction)


if __name__ == "__main__":
    app.run(debug = True)

