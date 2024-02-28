from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, url_for
import re
from flask_bcrypt import Bcrypt
from flask_app.models import user_model
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA]+$')


    #CREATE TREES
class Tree:
        db = 'login_and_registration' #WHAT DATABASE ARE YOU USING FOR THIS PROJECT?
        def __init__(self, data):
            self.id =           data["id"]
            self.host_id =      data["user_id"]
            self.specie =       data["specie"]
            self.location =     data['location']
            self.date_found =   data["date_found"]
            self.zip =          data['zip']
            self.note =         data['note']
            self.created_at =   data["created_at"]
            self.updated_at =   data["updated_at"]
            self.host =         None
    #WHAT CHANGES NEED TO BE MADE FOR THIS PROJECT ^?
    #WHAT NEEDS TO BE ADDED FOR CLASS ASSOCIATION ^?



    #---@@@ CREATE TREES MODELS @@@---#
    #---@@@ CREATE TREES MODELS @@@---#
        @classmethod
        def create_trees(cls, data):
            if not cls.validate_trees_data(data):
                return False

            query = '''
                INSERT INTO trees (specie, location, date_found, zip, note, user_id)
                VALUES (%(specie)s, %(location)s, %(date_found)s, %(zip)s, %(note)s, %(user_id)s)
                ;'''

            return connectToMySQL(cls.db).query_db(query, data)



    #---@@@ READ TREES MODELS @@@---#
        @classmethod
        def get_all_trees_W_hosts(cls):
            query = '''
                SELECT * FROM trees JOIN users ON users.id = trees.user_id; '''
            results = connectToMySQL(cls.db).query_db(query)
            treess = []
            if not results:
                return treess
            for result in results:
                this_trees = cls(result)
                this_trees.host = user_model.User.instantiate_user(result)
                treess.append(this_trees)
            return treess



        @classmethod
        def get_trees_for_user(cls, user_id):
            query = '''
                SELECT * FROM trees JOIN users ON users.id = trees.user_id
                WHERE users.id = %(user_id)s;
            '''
            results = connectToMySQL(cls.db).query_db(query, {'user_id': user_id})
            treess = []
            for result in results:
                this_trees = cls(result)
                this_trees.host = user_model.User.instantiate_user(result)
                treess.append(this_trees)
            return treess




    #---@@@ READ ONE SINGLE TREES MODELS @@@---#
        @classmethod
        def read_one_tree(cls, data):
            query = '''
                SELECT * FROM trees JOIN users ON users.id = trees.user_id
                WHERE trees.id = %(id)s;
            '''
            results = connectToMySQL(cls.db).query_db(query, data)
            result = results[0]
            trees = cls(result)
            trees.host = user_model.User.instantiate_user(result)
            return trees if result else None
            # return cls(result[0]) if result else None






    #---@@@ FETCH TREES AND CHECK FOR UNIQUENESS MODELS@@@---#
        @classmethod
        def is_name_unique(cls, specie):
            query = '''
                SELECT * FROM trees
                WHERE specie = %(specie)s
            '''
            result = connectToMySQL(cls.db).query_db(query, {'specie': specie})
            return not result  # If the result is empty, the name is unique






    #---@@@ UPDATE TREES MODELS @@@---#
        @classmethod
        def update_tree(cls, trees_data):
            query = '''
                UPDATE trees
                SET specie = %(specie)s,
                    location = %(location)s,
                    date_found = %(date_found)s,
                    zip = %(zip)s,
                    note = %(note)s
                WHERE id = %(id)s
            '''

            connectToMySQL(cls.db).query_db(query, trees_data)





    #---@@@ DELETE TREES MODELS @@@---#
        @classmethod
        def delete_tree(cls, data):
            query = '''
                        DELETE FROM trees WHERE id = %(id)s
                    '''
            results = connectToMySQL(cls.db).query_db(query, data)

            if results == None:
                return 'Successfully Deleted'
            else:
                return 'Failed to Delete'




    #---@@@ VALIDATION USER @@@---#
    #---@@@ VALIDATION USER @@@---#
        @classmethod
        def validate_trees_data(cls, data):
            is_valid = True
            if len(data['specie']) < 2:
                flash('specie must be 2 or more characters')
                is_valid = False

            if len(data['location']) < 5:
                flash('Description must be 5 or more characters')
                is_valid = False

            date_regex = re.compile(r'^\d{4}-\d{2}-\d{2}$')
            if not date_regex.match(data['date_found']):
                flash('Invalid date format, please use YYYY-MM-DD.')
                is_valid = False

            if len(data['zip']) > 0:
                flash('Zip Code is required')
                is_valid = False
            elif len(data['zip']) < 5 or len(data['zip']) > 5:
                flash('Invalid ZIP Code.')
                is_valid = False

                    # flash('ZIP code must be numeric.')
                    #is_valid = False

            if len(data['note']) > 50:
                flash('Notes must be 50 characters or fewer.')
                is_valid = False

            return is_valid



        #test
        @classmethod
        def purchase_tree(cls, trees_id, quantity):
            # Start a database transaction
            connection = connectToMySQL(cls.db)
            connection.autocommit = False

            try:
                # Check if there is enough stock available
                query_check_stock = 'SELECT quantity FROM trees WHERE id = %s FOR UPDATE'
                current_quantity = connection.query_db(query_check_stock, (trees_id,))[0]['quantity']

                if current_quantity < quantity:
                    # Not enough stock available
                    raise ValueError('Not enough stock available')

                # Perform the purchase and update quantity
                query_update_quantity = 'UPDATE trees SET quantity = quantity - %s WHERE id = %s'
                connection.query_db(query_update_quantity, (quantity, trees_id))

                # Commit the transaction
                connection.commit()

                return quantity
            except ValueError as ve:
                # Handle the specific ValueError for stock availability
                print(f"Error during purchase: {ve}")
                return 0
            except Exception as e:
                # Handle any other exceptions
                print(f"Error during purchase: {e}")
                connection.rollback()
                return 0
            finally:
                # Ensure autocommit is set back to True
                connection.autocommit = True
