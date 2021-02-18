#install dependencies
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_trf')
zh_nlp = spacy.load('zh_core_web_trf')
#zh_nlp = spacy.load('zh_core_web_sm')
#nlp = spacy.load('en_core_web_md')
import streamlit

def main():
	labels = {"ents": ["PERSON", "NORP", "FAC", "ORG",
                    "GPE", "LOC", "PRODUCT", "EVENT", "WORK_OF_ART",
                    "LANGUAGE", "MONEY", "LAW"]}
	raw_text = st.text_area("Enter Text Here and press the Analyze button",  height=400)
	doc = nlp(raw_text)
	html = displacy.render(doc, style="ent", options = labels)
	html = html.replace("\n\n", "\n")
	st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""
if __name__ == "__main__":
    main()