from flask_app.config.mysqlconnection import connectToMySQL

class Dojo():
    DB = "dojos_ninja_schema"
    def __dojo__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    #making method to create new dojo
    @classmethod
    def create_user(cls,data):
        query = """INSERT INTO dojo (name)
        VALUES( %(name)s);
        """
        result = connectToMySQL('dojos_ninja_schema').query_db(query,data)
        return result
    
    # view all dojos information
    @classmethod
    def view_dojo(cls):
        query = "SELECT * FROM dojo;"
        results = connectToMySQL(cls.DB).query_db(query)
        Dojo = []
        for Dojo in results:
            Dojo.append( cls(Dojo))
        return Dojo
    

