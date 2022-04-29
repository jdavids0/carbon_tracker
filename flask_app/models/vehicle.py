from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import app
from flask_app.models import user
from flask_app.models.library import cars

from flask import flash

db = "carbon_tracker"

class Vehicle:
    def __init__(self, data):
        self.id = data['id']
        self.vehicle_make = data['vehicle_make']
        self.vehicle_model = data['vehicle_model']
        self.vehicle_year = data['vehicle_year']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = []

    @staticmethod
    def validate_vehicle(form_data):
        is_valid = True

        if form_data['vehicle_makes'] == 'none':
            flash('Please submit a valid make')
            is_valid = False

        if form_data['vehicle_model'] == 'none':
            flash('Please submit a valid model')
            is_valid = False

        if form_data['vehicle_year'] == '':
            flash ('Please submit a valid year')
            is_valid = False

        return is_valid

    @classmethod
    def add_new_vehicle(cls):
        query = "INSERT INTO vehicles (vehicle_make, vehicle_model, vehicle_year, created_at, updated_at, user_id) VALUES (%(vehicle_make)s, %(vehicle_model)s, %(vehicle_year)s, NOW(), NOW(), %(user_id)s)"

        return connectToMySQL(db).query_db(query)

    @classmethod
    def get_user_vehicles (cls):
        query = "SELECT * FROM vehicles JOIN users on vehicles.users_id = users.id;"

        results = connectToMySQL(db).query_db(query)

        all_vehicles = []
        for row in results:
            vehicle = cls(row)
            user_data = {
                'id': row['user.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['created_at'],
                'updated_at' : row['updated_at'],
            }
            vehicle.user = user.User(user_data)
            all_vehicles.append (vehicle)

        return all_vehicles

class Trip:
    def __init__(self, data):
        self.user_id = data['user_id']
        self.vehicle.id = data['vehicle_id']
        self.distance_unit = data['distance_unit']
        self.distance_value = data['distance_value']