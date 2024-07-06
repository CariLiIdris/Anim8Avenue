from config.mysqlconnection import connectToMySQL
from flask import flash # type: ignore

class GroupPost:
  from config import DB
  def __init__(self, data):
    self._id = data['_id']
    self.content = data['content']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

    self.author_id = data['author_id']
    self.group_id = data['group_id']

  def to_dict(self):
    return {
      '_id': self._id,
      'content': self.content,
      'created_at': self.created_at,
      'updated_at': self.updated_at,
      'author_id': self.author_id,
      'group_id': self.group_id
    }

# C
  @classmethod
  def createGroupPost(cls, data):
    query = '''
              INSERT INTO groupPosts (content, group_id, author_id)
              VALUES (
                    %(content)s,
                    %(group_id)s,
                    %(author_id)s
                    );
            '''
    return connectToMySQL(cls.DB).query_db(query, data)

# R
# Get all group posts
  @classmethod
  def getAllGroupPosts(cls):
    query = '''
              SELECT * FROM groupPosts;
            '''
    results = connectToMySQL(cls.DB).query_db(query)
    groupPosts = []

    for groupPost in results:
      groupPosts.append( cls(groupPost) )
    return groupPosts
  
# Get group post by ID
  @classmethod
  def getGroupPostByID(cls, postID):
    query = '''
              SELECT * FROM groupPosts
              WHERE _id = %(_id)s;
            '''
    data = { '_id': postID }
    result = connectToMySQL(cls.DB).query_db(query, data)
    if result:
      return cls(result[0])
    return None

# U
  @classmethod
  def updateGroupPostByID(cls, postID, data):
    query = '''
              UPDATE groupPosts
              SET content=%(content)s
              WHERE _id = %(_id)s;
            '''
    data['_id'] = postID
    return connectToMySQL(cls.DB).query_db(query, data)

# D
  @classmethod
  def deleteGroupPostByID(cls, postID):
    query = '''
              DELETE FROM groupPosts 
              WHERE _id = %(_id)s;
            '''
    data = {'_id': postID}
    return connectToMySQL(cls.DB).query_db(query, data)