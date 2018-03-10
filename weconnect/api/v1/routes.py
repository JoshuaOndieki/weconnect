from flask import Blueprint
from flask_restful import Api
from weconnect import resources as r


v1 = Blueprint('v1', __name__)
api = Api(v1)
add = api.add_resource


add(r.All, '/all')  # GET
# User Routes
add(r.UserRegistration, '/auth/register')           # POST
add(r.UserLogin, '/auth/login')                     # POST
add(r.UserLogout, '/auth/logout')                   # POST
add(r.UserResetPassword, '/auth/reset-password')    # POST

# Business Routes
add(r.Business, '/businesses')                          # GET, POST
add(r.BusinessHandler, '/businesses/<int:businessId>')  # GET, PUT, DEL

# Review Routes
add(r.Reviews, '/businesses/<int:businessId>/reviews')   # GET, POST
