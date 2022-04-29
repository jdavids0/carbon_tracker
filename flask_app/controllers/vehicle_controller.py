from flask import render_template, request, redirect, session, flash, url_for, jsonify
# url_for generates a URL to an endpoint using the method passed in as an argument
from flask_app import app
import requests

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.user import User
from flask_app.models.vehicle import Vehicle

# returns base_url and uri_string
BASE_URL = "https://www.carboninterface.comp/api/v1"

### INITIAL FOOTPRINT ROUTES

@app.route('/zeronow/new/vehicle')
def new_footprint():
    if 'user_id' not in session:
        flash('Please register or login to use Zero Now!')
        return redirect ('/')

    vehicles = Vehicle.get_user_vehicles()
    
    return render_template ('new_vehicle.html', vehicles = vehicles)

@app.route('/zeronow/create', methods=['POST'])
def new_vehicle():
    if not Vehicle.validate_vehicle(request.form):
        return redirect('/zeronow/new')

    query_data = {
        'vehicle_makes' : request.form['vehicle_makes'],
        'vehicle_model' : request.form['vehicle_model'],
        'vehicle_year' : request.form['vehicle_year']
    }

    # API request to Carbon Interface for Vehicle Make, returning make_id
    v_makes = requests.get(f'{BASE_URL}/vehicle_makes',
        headers={"Content-Type":"application/json",
                "Authorization" : f"Bearer: IBLKMnDgx21tRNU1nt1OQg"})
    data = v_makes.json()
    make_id = ''
    for layer in data:
        if layer["data"]["attributes"]["name"] == 'vehicle_make':
            make_id = layer["data"]["id"]
            break

    # API request to Carbon Interface for Vehicle model, returning model_id
    v_models = requests.get(f'{BASE_URL}/vehicle_makes/{make_id}/vehicle_models',
            headers={"Content-Type":"application/json",
                "Authorization" : f"Bearer: IBLKMnDgx21tRNU1nt1OQg"})
    data = v_models.json()
    model_id = ''
    for layer in data:
        if layer["data"]["attributes"]["year"] == 'vehicle_year' and layer["data"]["attributes"]["name"] == 'vehicle_model':
            model_id = layer["data"]["id"]
            break

    return redirect ('/zeronow/dashboard')

# ADD TRIP ROUTES
@app.route('/zeronow/trip')
def new_trip():
    
    return render_template ('trip.html')



# LEADERBOARD ROUTE

@app.route('/zeronow/leaderboard')
def leaderboard():
    if 'user_id' not in session:
        flash('Please register or login to use Zero Now!')
        return redirect ('/')

    # CODE
    return render_template ('view_all.html')