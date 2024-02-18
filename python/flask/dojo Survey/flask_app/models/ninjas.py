from flask_app.config.mysqlconnection import connectToMySQL

class Ninjas():
    @classmethod
    def create_ninja(cls,data):
        query = """INSERT INTO dojo (name)
        VALUES( %(name)s);
        """
        result = connectToMySQL('dojos_ninja_schema').query_db(query,data)
        return result
    
    # view all ninjas information
    @classmethod
    def view_ninja(cls):
        query = "SELECT * FROM ninja;"
        results = connectToMySQL(cls.DB).query_db(query)
        Ninjas = []
        for ninja in results:
            Ninjas.append ( cls(Ninjas))
        return Ninjas