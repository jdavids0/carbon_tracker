from flask_app import app

from flask_app.controllers import user_controller, carbon_controller

if __name__ == "__main__":
    app.run (debug=True, port=5001)

# Carbon Interface API key IBLKMnDgx21tRNU1nt1OQg