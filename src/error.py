try:
	from __init__ import *
except:
	from src import *

from flask import jsonify



def my_error(status=404 ,description="",fullError=""):
	#In case the error was totally ready
	if fullError != "":
		status = fullError["status"]
		description = fullError["description"]
		#return jsonify({"success": False, 
		#"error": status,"message": description}),status

	if status not in [400,401,403,404,405,422,500]:
		raise Exception("status is "+str(status)
			+ ", not in [[400,401,403,404,405,422,500]]")
	if status == 400: message = "bad request"
	elif status == 401: message = "unauthorized"
	elif status == 403: message = "forbidden"
	elif status == 404: message = "not found"
	elif status == 405: message = "method not allowed"
	elif status == 422: message = "unprocessible"
	else : message = "internal server error"

	error_dict = {"success": False, 
		"error": status,"message": message,}

	if description == "": return jsonify(error_dict),status
	
	error_dict["description"] = description
	return jsonify(error_dict),status
	


def data_type_error(function_name,variable_name,expected_type_name,input):
	raise Exception("MoRBs:"+str(function_name)+":ERROR: '"+
		str(variable_name)+"' is supposed to have "+
		"the type of '"+str(expected_type_name)+"', but found type of '"+ 
		str(type(input))+"' instead")

def missing_data_error(function_name,variable_name):
	raise Exception("MoRBs:"+str(function_name)+":ERROR:missing_data_error:'"+
		variable_name+"' is missing")

#range is supposed to be a array
def not_in_range_error(function_name,variable_name,range):
	raise Exception("MoRBs:"+str(function_name)+":ERROR:not_in_range_error:'"+
		variable_name+"' is not in this range "+str(range))
	


