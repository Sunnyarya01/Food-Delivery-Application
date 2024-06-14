# API Configuration
from flask import jsonify, request
from flask_restful import Resource

from backend.models import Address, User
from backend.config import Constants
from backend.database import db

class UserResource(Resource):
    def post(self):
        data = request.get_json()
        address = Address(
            line1=data['address']['line1'],
            line2=data['address']['line2'],
            pincode=data['address']['pincode'],
            city=data['address']['city'],
            state=data['address']['state']
        )
        user = User(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            password=data['password'],
            role=Constants.CUSTOMER,
            address = [address]
        )

        db.session.add(user)
        db.session.commit()

        return user.json(), 201
    
    def get(self):
        users = User.query.all()
        return jsonify([user.json() for user in users])
    
    def get(self, id):
        user = User.query.get(id)
        return user.json()
    
    def put(self, id):
        pass

    def delete(self, id):
        user = User.query.get(id)
        addresses = user.address
        for address in addresses:
            db.session.delete(address)
    
        db.session.delete(user)
        db.session.commit()
        return user.json()