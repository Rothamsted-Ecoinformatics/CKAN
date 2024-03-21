**Deployment and Other Instructions**

To Restart Server:
			  
		service supervisor stop
 		service nginx stop 
	
 		_(check any services using port 80)_   lsof -i :80 
	
 		_Kill if any processes are running on port 80_  kill -9 <pid>
	

  		service supervisor start
	
 		service nginx start

 

Log File for CKAN:

  		 /etc/ckan/default/uwsgi.ERR

Git Information:

  	path: /usr/lib/ckan/default
	
  	branch: master
	
 	pull command: git pull origin master
	
  	push command: git push origin master
	
**Files to edit:**


  Add or edit new metadata values:
	
  	 /usr/lib/ckan/default/src/ckanext-extrafields/ckanext/extrafields/plugin.py
		
  	 /usr/lib/ckan/default/src/ckanext-extrafields/ckanext/extrafields/templates/package/snippets/package_basic_fields.html
		
   	 /usr/lib/ckan/default/src/ckanext-extrafields/ckanext/extrafields/templates/package/snippets/additional_info.html
		
   	 /usr/lib/ckan/default/src/ckanext-extrafields/ckanext/extrafields/templates/package/snippets/package_metadata_fields.html
		

  Styling Information:
	
  	 /usr/lib/ckan/default/src/ckan/ckan/public/base/css/main.css
