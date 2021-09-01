# ner_for_esl
## A quick summary of the API
This API grew out of (one of) my frustrations as a chinese student. When I read the newspaper, I know most of the important characters, but I often don't know proper nouns, such as peoples' names, cities, company names, and so on. Thus I often get lost in the text. At the same time, I see that my ESL students have the same struggle in English. This API is designed to help language learners resolve the problem of unknown vocabulary, especially in terms of proper nouns (see detailed motivation below).
I originally hosted the API as an EC2 instance on AWS, however it was limited to 12 months of free tier usage so I have terminated the instance.

## Further background on the ner_for_esl project
for more information, you can also see my article at https://chatbotslife.com/practical-nlp-for-language-learning-9b3a259fe7b5?sk=9a00138f2189baac2f9d3d4b2e81b955

English Learning and the Wheel of Fortune Corpus

How many words do you need to know in order to be able to speak a language? It’s a vague question and there’s a lot of disagreement about the details of what a “word” is and what it actually means to “know” a word, but here are some benchmarks English teachers use that can give you some idea on the topic:
* 1000: the core vocabulary items in English
* 2000: the number of vocabulary items you need to take care of most daily business
* 8,000 - 10,000: the number of vocabulary items you need to read the majority of texts/ go to university
* 20,000 - 40,000: the number of vocabulary items an average native speaker knows
* 170,000 vocabulary items in current use 
* 1,000,000: the approximate number of existent English vocabulary items, mostly obsolete

Anecdotally, a lot of ESL students are in the 1000-4000 word range, which should be enough for them to get by in life, but they often get stuck on 'easy' texts, even though they know most of the basic words. One reason for this is plain old proper nouns that don’t make sense if you just studied in English class (“Best Buy”, “Eliza”). I prefer the linguist Ray Jackendoff’s explanation of  this phenomena as the  “Wheel of Fortune” corpus; it means that if you show a native speaker a phrase like
   _ _ E A_ _A S T    O F    _ _ A _ _ IONS   
they can somehow yell out “BREAKFAST OF CHAMPIONS,” but non-native speakers have no chance of doing this or of understanding it after they have seen it. Also, as Jackendorf points out, Wheel of Fortune was on TV forever, but they never ran out of phrases to use.

The purpose of this repo is to help students by identifying and highlighting  tricky vocabulary items, including
* People’s names (in general / common names)
* People’s names (celebrities, figures in the news)
* Place names (cities/states/countries (“Atlanta”) and general (“Lake Meade”)
* Organizations (“Trader Joe’s”, “House of Representatives”)
* Titles (“New York Times”, “Men in Black”, “Song of Myself”)
* ??? 

Using a large off the shelf, English NER model from Spacy we can get about 90% accuracy in finding the following items, and we are working on improving the accuracy and the user interface of both models.

* EVENT		Named hurricanes, battles, wars, sports events, etc
* FAC			Buildings, airports, highways, bridges, etc.
* GPE			Countries, cities, states.
* LANGUAGE		Any named language.
* LAW			Named documents made into laws.
* LOC			Non-GPE locations, mountain ranges, bodies of water.
* MONEY		Monetary values, including unit.
* NORP      		Nationalities or religious or political groups.
* PERSON     	 	People, including fictional.
* PRODUCT		Objects, vehicles, foods, etc. (Not services).
* ORG			Companies, agencies, institutions, etc.
* WORK_OF_ART	Titles of books, songs, etc.

This is a work in progress, so if you have any suggestions or comments, please contact me at mateoias@hotmail.com 
