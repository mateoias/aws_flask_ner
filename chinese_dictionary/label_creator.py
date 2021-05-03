def label_creator():
  entity_labels = ["PERSON", "NORP", "FAC", "ORG",
                   "GPE", "LOC", "PRODUCT", "EVENT", "WORK_OF_ART",
                   "LANGUAGE", "MONEY", "LAW"]

  label_definitions = ["Person's name", "religious/political/national group names",
                       "Buildings, airports, bridges etc.", "companies and organizations",
                       "Countries, cities, states", "locations(mountains, lakes, etc)", "Products", "named events(history, war, sports, etc.)",
                       "Titles of movies, books, etc.", "any named language",
                       "names of money (dollar, etc.)", "names of laws and regulations"]
  labels = dict(zip(entity_labels, label_definitions))
  return labels
