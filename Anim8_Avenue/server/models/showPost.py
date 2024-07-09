from config.mysqlconnection import connectToMySQL
from flask import flash # type: ignore

class ShowPost: 
  from config import DB
  def __init__(self, data):
    self._id = data['_id']
    self.content = data['content']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

    self.author_id = data['author_id']
    self.show_id = data['show_id']

  def to_dict(self):
    return {
      '_id': self._id,
      'content': self.content,
      'created_at': self.created_at,
      'updated_at': self.updated_at,
      'author_id': self.author_id,
      'show_id': self.show_id
    }

# C
  @classmethod
  def createShowPost(cls, data):
    query = '''
              INSERT INTO showPosts (content, author_id, show_id)
              VALUES (
                %(content)s,
                %(author_id)s,
                %(show_id)s
              );
            '''
    return connectToMySQL(cls.DB).query_db(query, data)

# R
  @classmethod
  def getShowPostByID(cls, postID):
    query = '''
              SELECT * FROM showPosts
              WHERE _id = %(_id)s;
            '''
    data = { '_id': postID }
    result = connectToMySQL(cls.DB).query_db(query, data)
    if result:
      return cls(result[0])
    return None

  @classmethod
  def getAllShowPosts(cls):
    query = '''
              SELECT * FROM showPosts
            '''
    results = connectToMySQL(cls.DB).query_db(query)
    showPosts = []

    for showPost in results:
      showPosts.append( cls(showPost) )
    return showPosts

# U
  @classmethod
  def updateShowPostByID(cls, postID, data):
    query = '''
              UPDATE showPosts
              SET content=%(content)s
              WHERE _id = %(_id)s;
            '''
    data['_id'] = postID
    return connectToMySQL(cls.DB).query_db(query, data)

# D
  @classmethod
  def deleteShowPostByID(cls, postID):
    query = '''
              DELETE FROM showPosts
              WHERE _id = %(_id)s
            '''
    data = { '_id': postID }
    return connectToMySQL(cls.DB).query_db(query, data)