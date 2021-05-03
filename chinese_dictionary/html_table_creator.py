def label_table():
    class ItemTable(Table):
        name = Col('Name')
        description = Col('Description')

    class Item(object):
        def __init__(self, name, description):
            self.name = name
            self.description = description
    items = [Item("EVENT", "Named events (history, war, sports, etc.)"),
            Item('FAC', 'Buildings, airports, bridges etc.'),
            Item("GPE", "Countries, cities, states"),
            Item("LANGUAGE", "Any named language"),
            Item("Law", "names of laws and regulations"),
            Item("LOC", "locations(mountains, lakes, etc)"),
            Item("Money",  "names of money (dollar, etc.)"),
            Item('NORP', 'religious/political/national group names'),
            Item("ORG", "companies and organizations"),
            Item('PERSON', "Person's name"),
            Item("PRODUCT", "Consumer Products"),
            Item("WORK_OF_ART",  "Titles of movies, books, etc.")]
    # Populate the table
    table = ItemTable(items)
    return table
