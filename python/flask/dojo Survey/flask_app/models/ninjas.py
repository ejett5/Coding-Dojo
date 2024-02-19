from flask_app.config.mysqlconnection import connectToMySQL

class Ninjas():
    DB = "dojo_survey_schema"
    @classmethod
    def create_ninja(cls,data):
        query = """INSERT INTO dojo (name)
        VALUES( %(first_name)s, %(last_name)s, %(age)s );
        """
        result = connectToMySQL('dojo_survey_schema').query_db(query,data)
        return result
    
    # view all ninjas information
    @classmethod
    def view_ninja(cls):
        query = "SELECT * FROM ninja;"
        results = connectToMySQL(cls.DB).query_db(query)
        Ninjas = []
        for Ninjas in results:
            Ninjas.append ( cls(Ninjas))
        return Ninjas