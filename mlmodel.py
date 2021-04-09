# flask app to hold the ner model
# to run locally
# pip install -U pip setuptools wheel
# pip install spacy
import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_trf")
zh_nlp = spacy.load("zh_core_web_trf")
from flask import Flask, render_template, request, jsonify
from chinese_dictionary import add_pinyin_hashed
from chinese_dictionary import label_creator
app = Flask(__name__)

@app.route('/')
def show_user_input_form():
	return render_template('predictorform.html')


@app.route('/results', methods=['POST'])

def results():
    labels = label_creator.label_creator()
    form = request.form
    if request.method == 'POST':
      #write your function that loads the model
      try:
        language = request.form['language']
        data = request.form['data']
        if language == "English":
          doc = nlp(data)
        elif language == "Chinese":
          doc = zh_nlp(data)
      except:
        return render_template('predictorform.html')
      prediction = []
      words = []
      ent_to_keep = ["PERSON", "NORP", "FAC", "ORG", "GPE", "LOC", "PRODUCT",
       "EVENT", "WORK_OF_ART", "LANGUAGE", "MONEY", "LAW"]
      for ent in doc.ents: 
          entity = (ent.label_, ent.text)
          if ent.label_ in ent_to_keep:
            prediction.append(entity)
      if language == "Chinese":
        prediction = add_pinyin_hashed.add_pinyin(prediction)
            
            # characters = ent.text
            # for character in characters:
            #   print(character)
            #   pronunciation = add_pinyin_hashed.add_pinyin(character)
            #   print(pronunciation)
            #   chinese_character = (character, pronunciation)
            #   prediction.append(chinese_character)
         
    options = {"ents": ent_to_keep}
    html = displacy.render(doc, style="ent", options=options, page=True)
    # return jsonify(data=data, prediction=prediction, html = html)


    return render_template('resultsform.html', data = data,
     prediction = prediction, html = html, labels = labels)




if __name__ == "__main__":
    app.run(debug = True)

