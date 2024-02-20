from flask_app.config.mysqlconnection import connectToMySQL

class Player():
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_player(cls, data):
        query = """ INSERT INTO players (first_name, last_name, email, password)
        VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """

    @classmethod
    def view_player(cls):
        query = "SELECT * FROM players;"
        results = connectToMySQL(cls.db).query_db(query)
        for player in results:
            player.append( cls(player))
        return player