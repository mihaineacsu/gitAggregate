import pprint

class QueryHandler:
    """
        Performs queries on db.
    """

    def __init__(self, db):
        self.payloads = db.payloads
        self.pp = pprint.PrettyPrinter(indent=4)

    def get_by_author(self, author):
        for payload in self.payloads.find({'commits.author.username': author[0]}):
            self.pp.pprint(payload)
