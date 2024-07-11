from config.mysqlconnection import connectToMySQL
from flask import flash

class Show:
    from config import DB

    def __init__(self, data):
        self._id = data['_id']
        self.name = data['name']
        self.description = data['description']
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.owner_id = data['owner_id']
        self.category = data.get('category')
        self.image_url = data.get('image_url')

    def to_dict(self):
        return {
            '_id': self._id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'owner_id': self.owner_id,
            'category': self.category,
            'image_url': self.image_url
        }

    # Create
    @classmethod
    def createShow(cls, data):
        query = '''
                INSERT INTO shows (name, description, owner_id, category, image_url)
                VALUES (
                %(name)s, 
                %(description)s, 
                %(owner_id)s, 
                %(category)s, 
                %(image_url)s);
                '''
        return connectToMySQL(cls.DB).query_db(query, data)

    # Get all shows
    @classmethod
    def getAllShows(cls):
        query = '''
                SELECT * FROM shows;
                '''
        results = connectToMySQL(cls.DB).query_db(query)
        shows = [cls(show) for show in results]
        return shows

    # Get show by ID
    @classmethod
    def getShowByID(cls, showID):
        query = '''
                SELECT * FROM shows
                WHERE _id = %(_id)s;
                '''
        data = {'_id': showID}
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result:
            return cls(result[0])
        return None

    @classmethod
    def updateShowByID(cls, showID, data):
      query = '''
              UPDATE shows
              SET name=%(name)s, description=%(description)s, category=%(category)s
              WHERE _id = %(_id)s;
              '''
      data['_id'] = showID
      connectToMySQL(cls.DB).query_db(query, data)

      if 'image_url' in data and data['image_url']:
        query = '''
                UPDATE shows
                SET image_url=%(image_url)s
                WHERE _id = %(_id)s;
                '''
        connectToMySQL(cls.DB).query_db(query, data)
      return True

    # Delete
    @classmethod
    def deleteShowByID(cls, showID):
        query = '''
                DELETE FROM shows 
                WHERE _id = %(_id)s;
                '''
        data = {'_id': showID}
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def getAllCategories(cls):
        query = '''
                SELECT DISTINCT category FROM shows;
                '''
        results = connectToMySQL(cls.DB).query_db(query)
        categories = [result['category'] for result in results]
        return categories