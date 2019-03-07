from flask import jsonify, request,json,abort
from . models import User
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from re import search

from . methods import UserList


userlist = UserList()


def create_new_user():

	data = request.get_json()

	if not data or not data['firstname'] or not data['lastname'] or not data['othername'] \
	or not data['username'] or not data['email'] or not data['password'] or not data['phonenumber'] \
	or not data['registered']:

		abort(400)

	firstname,lastname,othername,username,email,password,phonenumber = \
	data.get('firstname'), data.get('lastname'), \
	data.get('othername'), data.get('username'), \
	data.get('email'), data.get('password'), data.get('phonenumber')



	user_id = userlist.generate_user_id()

	isadmin = False
	registered = date_today = datetime.now().strftime('%d%m%y %H%M')

	new_user  = User(user_id, firstname,lastname,othername,username,email, \
		password,phonenumber,registered,isadmin)

	if email == '' or username == '' or password == '':
		return jsonify({"message" : "email, username and password cannot be empty"}),200

	new_user.password = generate_password_hash(password)

	if new_user.email:
		for usie in userlist.user_list:
			if new_user.email == usie['email']:
				return jsonify({"message" : "email already taken"}),200
	if new_user.username:
		for usie in userlist.user_list:
			if new_user.username == usie['username']:
				return jsonify({"message" : "username already taken"}),200
	userlist.add_a_user(new_user),201

	curr_user = userlist.user_list[-1]
	return jsonify({"user" : {
		"username": curr_user['username']

		} }),201


def getall_users():
	return jsonify({"users" : userlist.get_all_users()})

def sign_in_user():
	data = request.get_json()

	usernme = data.get('username')
	print(usernme)
	passcode = data.get('password')
	print(passcode)


	if usernme == '' or passcode == '':
		return jsonify({"message" : "password or username can not be empty"}),400
	if not type(usernme) == str:
		return jsonify({"message": "useranme must be a string"})
	usernme = (usernme).strip()

	if not type(passcode) == str:
		return jsonify({"message": "useranme must be a string"})
	passcode = (passcode).strip()
	#passcode = generate_password_hash(passcode)
	for user in userlist.user_list:
		print(user['username'])
		print(usernme)
		print(user['password'])
		print(passcode)
		if user['username'] == usernme and check_password_hash(user['password'],passcode):

			print(user['username'])
			print(usernme)
			print(passcode)
			
			return jsonify({"message" : "your welcome {} your loged in ".format(usernme)}),200
		#print(userlist.user_list)
		else:
			return jsonify({"message" : "The user doesnot exist"}),201


def index_page():
	return jsonify({"message": "Your welcome to ireporter"}),200

