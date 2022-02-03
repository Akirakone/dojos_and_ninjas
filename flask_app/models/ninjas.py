from flask_app.config.mysqlconnection import connectToMySQL

class Ninjas:
    db_name = 'dojos_and_ninjas'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojos=[]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        query_results = connectToMySQL(cls.db_name).query_db(query)
        
        ninjas = []
        for each_row in query_results:
            new_user = cls(each_row)
            ninjas.append()

        return ninjas

   

    @classmethod
    def add_ninja(cls, data):
        query = "INSERT INTO ninjas (`first_name`,`last_name`,`age`,`dojos`) VALUES (%(first_name)s,%(last_name)s,%(age)s, %(dojos)s);"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result

