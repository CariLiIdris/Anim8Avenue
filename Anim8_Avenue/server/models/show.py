from config.mysqlconnection import connectToMySQL
from flask import flash # type: ignore

class Show:
  DB = 'anim8AveSchema'
  def __init__(self, data):
    self._id = data['_id']
    self.name = data['name']
    self.description = data['description']
    self.created_at = data["created_at"]
    self.updated_at = data["updated_at"]
    
    self.owner_id = data['owner_id']

    def to_dict(self):
      return {
        '_id': self._id,
        'name': self.name,
        'description': self.description,
        'created_at': self.created_at,
        'updated_at': self.updated_at,
        'owner_id': self.user_id
      }
    
# C
  @classmethod
  def createShow(cls, data):
    query = '''
              INSERT INTO shows (name, description, owner_id)
              VALUES (
                    %(name)s,
                    %(description)s,
                    %(owner_id)s
                    );
            '''
    return connectToMySQL(cls.DB).query_db(query, data)

# R
# Get all shows
  @classmethod
  def getAllShows(cls):
    query = '''
              SELECT * FROM shows;
            '''
    results = connectToMySQL(cls.DB).query_db(query)
    shows = []

    for show in results:
      shows.append( cls(show) )
    return shows
  
  @classmethod
  def getShowByID(cls, showID):
    query = '''
              SELECT * FROM shows
              WHERE _id = %(_id)s;
            '''
    data = { '_id': showID }
    result = connectToMySQL(cls.DB).query_db(query, data)
    if result:
      return cls(result[0])
    return None

# U
  @classmethod
  def updateShowByID(cls, showID, data):
    query = '''
              UPDATE shows
              SET name=%(name)s, description=%(description)s
              WHERE _id = %(_id)s;
            '''
    data['_id'] = showID
    return connectToMySQL(cls.DB).query_db(query, data)

# D
  @classmethod
  def deleteShowByID(cls, showID):
    query = '''
              DELETE FROM shows 
              WHERE _id = %(_id)s;
            '''
    data = {'_id': showID}
    return connectToMySQL(cls.DB).query_db(query, data)