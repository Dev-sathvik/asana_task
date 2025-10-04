import asana
from asana.rest import ApiException
from pprint import pprint
import os

configuration = asana.Configuration()
configuration.access_token = os.getenv("ASANA_PAT")
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
opts = {
    'limit': 5, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    #'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'workspace': "1211435629826409", # str | The workspace or organization to filter projects on.
    #'team': "14916", # str | The team to filter projects on.
    'archived': False, # bool | Only return projects whose `archived` field takes on the value of this parameter.
    #'opt_fields':
}

try:
    # Get multiple projects
    api_response = projects_api_instance.get_projects(opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects: %s\n" % e)