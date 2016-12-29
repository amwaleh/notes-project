# notes-project/app/models.py

import os
import datetime
# import mongoengine
from mongoengine import connect, Document, StringField,DateTimeField

# get the mlab URI from environment variables
uri = os.getenv('MLAB_URI')

# connect to our database at MLAB
connect(host=uri)


class Notebook(Document):
    '''
        This collection will handle our notes
    '''
    title = StringField(max_length=100, required=True)
    notes =StringField(max_length=500, required=True)
    date_modified = DateTimeField(default=datetime.datetime.now)
