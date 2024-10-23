import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from flask import Response, request
import mysql.connector
import logging

# import ckanext.customapi.cli as cli
# import ckanext.customapi.helpers as helpers
# import ckanext.customapi.views as views
# from ckanext.customapi.logic import (
#     action, auth, validators
# )

def hello_world(context, data_dict):
    # This function returns a simple 'Hello World' message
    return "Hello World"


def fetchUsers(context, data_dict):
    # Get the 'input_val' from the data_dict (which is passed via the API request)
    input_val = data_dict.get('input_val', None)  # Defaults to None if not provided
    if not input_val:
        return {'success': False, 'message': 'Missing required parameter: input_val'}
    try:
        # Establish database connection
        mydb = mysql.connector.connect(
            host="promessa.rothamsted.ac.uk",
            user="pma_user",
            password="t5[2E;P!NTbs",
            database="CKAN"
        )
        logging.warning("Database connection successful")
    except mysql.connector.Error as err:
        logging.error(f"Database connection error: {err}")
        return {'success': False, 'message': f"Database connection error: {err}"}
    try:
        mycursor = mydb.cursor()
       # Prepare SQL query
        query = "SELECT * FROM `ckanstafflist` WHERE `fullname` LIKE %s"
        mycursor.execute(query, ('%' + input_val + '%',))
        # Fetch all the matching records
        myresult = mycursor.fetchall()
        # Log the results
        logging.warning(f"Query results: {myresult}")
        # Close the cursor and the database connection
        mycursor.close()
        mydb.close()

        return {
            'success': True,
            'data': myresult  # Return the results as part of the API response
        }
    except Exception as e:
        logging.error(f"Error executing query: {e}")
        return {'success': False, 'message': f"Error executing query: {e}"}

def fetchFunders(context, data_dict):
    # Get the 'input_val' from the data_dict (which is passed via the API request)
    input_val = data_dict.get('input_val', None)  # Defaults to None if not provided
    if not input_val:
        return {'success': False, 'message': 'Missing required parameter: input_val'}
    try:
        # Establish database connection
        mydb = mysql.connector.connect(
            host="promessa.rothamsted.ac.uk",
            user="pma_user",
            password="t5[2E;P!NTbs",
            database="CKAN"
        )
        logging.warning("Database connection successful")
    except mysql.connector.Error as err:
        logging.error(f"Database connection error: {err}")
        return {'success': False, 'message': f"Database connection error: {err}"}
    try:
        mycursor = mydb.cursor()
       # Prepare SQL query
        query = "SELECT * FROM `funderinfo` WHERE `awardNumber` LIKE %s"
        mycursor.execute(query, ('%' + input_val + '%',))
        # Fetch all the matching records
        myresult = mycursor.fetchall()
        # Log the results
        logging.warning(f"Query results: {myresult}")
        # Close the cursor and the database connection
        mycursor.close()
        mydb.close()

        return {
            'success': True,
            'data': myresult  # Return the results as part of the API response
        }
    except Exception as e:
        logging.error(f"Error executing query: {e}")
        return {'success': False, 'message': f"Error executing query: {e}"}    

def fetchSubjects(context, data_dict):
    # Get the 'input_val' from the data_dict (which is passed via the API request)
    input_val = data_dict.get('input_val', None)  # Defaults to None if not provided
    if not input_val:
        return {'success': False, 'message': 'Missing required parameter: input_val'}
    try:
        # Establish database connection
        mydb = mysql.connector.connect(
            host="promessa.rothamsted.ac.uk",
            user="pma_user",
            password="t5[2E;P!NTbs",
            database="CKAN"
        )
        logging.warning("Database connection successful")
    except mysql.connector.Error as err:
        logging.error(f"Database connection error: {err}")
        return {'success': False, 'message': f"Database connection error: {err}"}
    try:
        mycursor = mydb.cursor()
       # Prepare SQL query
        query = "SELECT * FROM `subjectslist` WHERE `subject` LIKE %s LIMIT 50"
        mycursor.execute(query, ('%' + input_val + '%',))
        # Fetch all the matching records
        myresult = mycursor.fetchall()
        # Log the results
        logging.warning(f"Query results: {myresult}")
        # Close the cursor and the database connection
        mycursor.close()
        mydb.close()

        return {
            'success': True,
            'data': myresult  # Return the results as part of the API response
        }
    except Exception as e:
        logging.error(f"Error executing query: {e}")
        return {'success': False, 'message': f"Error executing query: {e}"}
    
class CustomapiPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    
    # plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.IActions)
    # plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    # plugins.implements(plugins.ITemplateHelpers)
    # plugins.implements(plugins.IValidators)
    

    # IConfigurer
    def get_actions(self):
        # Register your custom action 'hello_world'
        return {
            'hello_world': hello_world,
            'fetchUsers': fetchUsers,
            'fetchFunders': fetchFunders,
            'fetchSubjects': fetchSubjects
            
        }
        
    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "customapi")

    
    # IAuthFunctions

    # def get_auth_functions(self):
    #     return auth.get_auth_functions()

    # IActions

    # def get_actions(self):
    #     return action.get_actions()

    # IBlueprint

    # def get_blueprint(self):
    #     return views.get_blueprints()

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers

    # def get_helpers(self):
    #     return helpers.get_helpers()

    # IValidators

    # def get_validators(self):
    #     return validators.get_validators()
    

