from config.mysqlconnection import connectToMySQL
from flask import flash # type: ignore

class ShowPost: 
  def __init__(self, data):
    self._id = data['_id']
    self.content = data['content']
    self.created_at = data["created_at"]
    self.updated_at = data["updated_at"]

    self.shows = []

    def to_dict(self):
      return {
        '_id': self._id,
        'content': self.content,
        'created_at': self.created_at,
        'updated_at': self.updated_at,
        'shows': self.shows
      }
    
# C
  @classmethod
  def createPost(cls, data):
    query = '''
              INSERT INTO showPosts (content, shows_id)
              VALUES (
                %(content)s,
                %(shows_id)s
              );
            '''
    return connectToMySQL(cls.DB).query_db(query, data)

# R
@classmethod
def getPostByID(cls, postID):
  query = '''
            SELECT * FROM showPosts
            WHERE _id = %(_id)s;
          '''
  data = { '_id': postID }
  result = connectToMySQL(cls.DB).query_db(query, data)
  if result:
    return cls(result[0])
  return None

# U
@classmethod
def updatePostByID(cls, postID, data):
  query = '''
            UPDATE showPosts
            SET content=%(content)s, shows_id=%(shows_id)s
            WHERE _id = %(_id)s;
          '''
  data['_id'] = postID
  return connectToMySQL(cls.DB).query_db(query, data)

# D
@classmethod
def deletePostByID(cls, postID):
  query = '''
            DELETE FROM showPosts
            WHERE _id = %(_id)s
          '''
  data = { '_id': postID }
  return connectToMySQL(cls.DB).query_db(query, data)