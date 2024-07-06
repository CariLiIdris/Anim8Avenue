from config.mysqlconnection import connectToMySQL
from flask import flash # type: ignore

class Group:
  from config import DB
  def __init__(self, data):
    self._id = data['_id']
    self.name = data['name']
    self.description = data['description']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

    self.owner_id = data['owner_id']

  def to_dict(self):
    return {
      '_id': self._id,
      'name': self.name,
      'description': self.description,
      'created_at': self.created_at,
      'updated_at': self.updated_at,
      'owner_id': self.owner_id
    }

# C
  @classmethod
  def createGroup(cls, data):
    query = '''
              INSERT INTO `groups` (name, description, owner_id)
              VALUES (
                    %(name)s,
                    %(description)s,
                    %(owner_id)s
                    );
            '''
    return connectToMySQL(cls.DB).query_db(query, data)

# R
# Get all groups
  @classmethod
  def getAllGroups(cls):
    query = '''
              SELECT * FROM `groups`;
            '''
    results = connectToMySQL(cls.DB).query_db(query)
    groups = []

    for group in results:
      groups.append( cls(group) )
    return groups
  
# Get show by ID
  @classmethod
  def getGroupByID(cls, groupID):
    query = '''
              SELECT * FROM `groups`
              WHERE _id = %(_id)s;
            '''
    data = { '_id': groupID }
    result = connectToMySQL(cls.DB).query_db(query, data)
    if result:
      return cls(result[0])
    return None

# U
  @classmethod
  def updateGroupByID(cls, groupID, data):
    query = '''
              UPDATE `groups`
              SET name=%(name)s, description=%(description)s
              WHERE _id = %(_id)s;
            '''
    data['_id'] = groupID
    return connectToMySQL(cls.DB).query_db(query, data)

# D
  @classmethod
  def deleteGroupByID(cls, groupID):
    query = '''
              DELETE FROM `groups` 
              WHERE _id = %(_id)s;
            '''
    data = {'_id': groupID}
    return connectToMySQL(cls.DB).query_db(query, data)