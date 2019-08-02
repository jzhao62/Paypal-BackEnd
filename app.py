from flask import Flask
from flask import Flask, render_template
from werkzeug.datastructures import ImmutableOrderedMultiDict
from flask import Response,url_for
from flask import jsonify
from flask_cors import CORS
from flask import request
import paypalrestsdk
from flask import Flask,redirect, abort
from sample.CaptureIntentExamples import *
import threading
app = Flask(__name__)
CORS(app)







orders = [];
notes = [
  {'id': 1, 'label': 'LabelOne', 'author': 'Shyam'},
  {'id': 2, 'label': 'LabelTwo', 'author': 'Brad'},
  {'id': 3, 'label': 'LabelThree', 'author': 'Someone'},
];



user = [
	{'id' : 1, 'name' : 'admin', 'pwd': 'admin'},
	{'id': 2, 'name': 'usr1', 'pwd': '123'},
	{'id': 3, 'name': 'usr2', 'pwd': '456'}

]


inventory = [
	{'id': 1, 'category': "meat", 'description': "A", 'price': 2.99, 'qty': 1},
	{'id': 2, 'category': "meat", 'description': "B", 'price': 2.99,'qty': 1},
	{'id': 3, 'category': "meat", 'description': "C",'price': 6.99, 'qty': 1},
	{'id': 4, 'category': "meat", 'description': "D", 'price': 12.99, 'qty': 1},
	{'id': 5, 'category': "fruit", 'description': "E", 'price': 29.99, 'qty': 1},
	{'id': 6, 'category': "fruit", 'description': "F", 'price': 29.99, 'qty': 1},
	{'id': 7, 'category': "veggie", 'description': "G", 'price': 49.99, 'qty': 1},
	{'id': 8, 'category': "veggie", 'description': "H", 'price': 79.99, 'qty': 1},
];




@app.route('/api/get_menu', methods=['GET'])
def get_menus():
	if(request.method == 'GET'):
		return jsonify(inventory)




@app.route('/api/all', methods=['GET'])
def get_query_string():
	if(request.method == 'GET'):
		return jsonify(notes)






#
# @app.route('/api/user', methods = ['GET', 'PUT', 'DELETE','ADD'])
# def user_api():
#
# 		usr = request.args.get('username');
# 		pwd = request.args.get('password');
#
# 		if (request.method == 'GET'):
#
#
# 		if (request.method == 'PUT'):
# 			print('updating specific item');
# 			print(request.data)
# 			return jsonify({'task': 'GG'})
# 		if(request.method == 'DELETE'):
# 			print('deleting specific item');
# 			print(request.data)
# 			return jsonify({'task': 'GG'})
# 		if (request.method == 'ADD'):
# 			print('adding user');
# 			print(request.data)
# 			return jsonify({'task': 'GG'})




@app.route('/api/order', methods=['POST'])
def forward_transaction():
	if (request.method == 'POST'):
		print(request.data);
		if(request.data != []):
			print('redirecting for payment')
			return redirect(url_for('approve_purchase'));
		else:
			data = 'GG'
			response = app.response_class(
				response=json.dumps(data),
				status=204,
				mimetype='application/json'
			)
			return response




@app.route('/approve')
def approve_purchase():
	response = CreateOrder().create_order()
	approval_url = ""
	order_id = "";
	if response.status_code == 201:
		order_id = response.result.id
		for link in response.result.links:
			print('\t{}: {}\tCall Type: {}'.format(str(link.rel).capitalize(), link.href, link.method))
			if(link.rel.capitalize() == 'Approve'):
				approval_url = str(link.href)
		print 'Created Successfully\n'
		print 'Copy approve link and paste it in browser. Login with buyer account and follow the instructions.\nOnce approved hit enter...'
		orders.append(order_id);
		print (orders);

		# redirect(approval_url);
		response = app.response_class(
			response=json.dumps(approval_url),
			status=201,
			mimetype='application/json'
		)

		print(response)

		return jsonify(approval_url, 201);


	else:
		print 'Link is unreachable'
		exit(1)



@app.route('/success')
def xsuccess():
	# try:
	# 	return render_template("success.html")
	# except Exception, e:
	# 	return(str(e))
	return 'success '


@app.route('/express')
def express():
	try:
		return render_template("express.html")
	except Exception, e:
		return(str(e))


if __name__ == '__main__':
    app.run()



