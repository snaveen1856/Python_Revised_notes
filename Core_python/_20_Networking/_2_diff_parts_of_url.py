import urllib.parse

url = "https://www.javatpoint.com/python-example"

# Get tuple with parts of url
tup = urllib.parse.urlparse(url)

# Display contents of tuple
print(tup)
print("Scheme : ", tup.scheme)
print("Netloc : ", tup.netloc)
print("Path   : ", tup.path)
print("Params : ", tup.params)
print("Port   : ", tup.port)
print("URL    : ", tup.geturl())

'''
HTTP Request methods :
--------------------------
GET -- for data retrieval
POST -- to save data(create)
PUT --- to update the record
DELETE --- to delete the record

Request URL     : https://digitalcatalog.paytm.com/dcat/v1/category/17/getcategory?channel \
                           =web&version=2&child_site_id=1&site_id=1&locale=en-in
                  https://
                  digitalcatalog.paytm.com
                  /dcat/v1/category/17/getcategory ? 
                      channel=web&
                      version=2&
                      child_site_id=1&
                      site_id=1&
                      locale=en-in
Request Method  : GET
Payload         : {Json data}
'''