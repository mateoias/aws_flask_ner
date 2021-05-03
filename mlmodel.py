# flask app to hold the ner model
# to run locally
# pip install -U pip setuptools wheel
# pip install spacy
from flask import Flask, render_template, request, jsonify
from flask_table import Table, Col
import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_trf")
zh_nlp = spacy.load("zh_core_web_trf")
from chinese_dictionary import add_pinyin_hashed
from chinese_dictionary import label_creator
app = Flask(__name__)

@app.route('/')
def show_user_input_form():
	return render_template('index.html')

@app.route('/about')
def show_about_page():
  return render_template('about.html')
  
@app.route('/results', methods=['POST'])

def results():
    table = label_table()
    # labels = label_creator.label_creator()
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
        return render_template('index.html')
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
     prediction = prediction, html = html, table = table)


def label_table():
    from flask_table import Table, Col

    class ItemTable(Table):
        name = Col('Name')
        description = Col('Description')

    class Item(object):
        def __init__(self, name, description):
            self.name = name
            self.description = description
    items = [Item("EVENT", "  Named events (history, war, sports, etc.)"),
             Item('FAC', '  Buildings, airports, bridges etc.'),
             Item("GPE", "  Countries, cities, states"),
             Item("LANGUAGE", "  Any named language"),
             Item("LAW", "  Names of laws and regulations"),
             Item("LOC", "  Locations(mountains, lakes, etc)"),
             Item("MONEY",  "  Names of money (dollar, etc.)"),
             Item('NORP', '  Religious/political/national group names'),
             Item("ORG", "  Companies and organizations"),
             Item('PERSON', "  Person's name"),
             Item("PRODUCT", "  Consumer Products"),
             Item("WORK_OF_ART", "  Movie titles, books, etc.")]
    # Populate the table
    table = ItemTable(items)
    return table



if __name__ == "__main__":
    app.run(debug = True)

