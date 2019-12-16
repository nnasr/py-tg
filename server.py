from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app, version='1.0', title='Occurrences API', description=
          'An API that generates any number of occurrences for any number of drugs of interest')


class Occurrence(object):
    def __init__(self):
        self.occurrences = []

    def get(self, id):
        for o in self.occurrences:
            if o['id'] == id:
                return o
        api.abort(404, "Occurrences {} do not exist".format(id))


if __name__ == '__main__':
    app.run(debug=True)
