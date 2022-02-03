from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime
import math
from flask import flash
from flask_app.models import dojos
from flask_app.models import ninjas


class Dojos:
    db_name = 'dojos_and_ninjas'

    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.dojos = {}





    @classmethod
    def ninja_with_dojo(cls, data):
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON ninjas.dojos_id= dojos.id "
        results = connectToMySQL(cls.db_name).query_db(query, data)
        dojos = []
        for row in results:
            dojo = (cls(row))
            ninja_data = {
                'id': row['id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "age": row['age'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
            }
            dojo.ninja = ninjas.Ninjas(ninja_data)
            dojos.append(dojo)
        return dojos

    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON ninjas.dojos_id= dojos.id  WHERE ninjas.id = %(dojo_id)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        dojo = cls(results[0])
        ninja_data = {
            "id": results[0]['users.id'],
            "first_name": results[0]['first_name'],
            "last_name": results[0]['last_name'],
            "age": results[0]['age'],
            "created_at": results[0]['users.created_at'],
            "updated_at": results[0]['users.updated_at'],
        }
        dojo.ninja = ninjas.Ninjas(ninja_data)
        return dojo

    @classmethod
    def add_dojo(cls, data):
        query = 'INSERT INTO dojos (`name`, `created_at`,`updated_at`,) VALUES (%(name)s NOW(), NOW());'
        return connectToMySQL(cls.db_name).query_db(query, data)