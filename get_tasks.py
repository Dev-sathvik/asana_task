import asana
from asana.rest import ApiException
from pprint import pprint
import os

configuration = asana.Configuration()
configuration.access_token = os.getenv("ASANA_PAT")
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tasks_api_instance = asana.TasksApi(api_client)
opts = {
    'limit': 5, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    #'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    #'assignee': "14641", # str | The assignee to filter tasks on. If searching for unassigned tasks, assignee.any = null can be specified. *Note: If you specify `assignee`, you must also specify the `workspace` to filter on.*
    'project': "1211436899216107", # str | The project to filter tasks on.
}

try:
    # Get multiple tasks
    api_response = tasks_api_instance.get_tasks(opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling TasksApi->get_tasks: %s\n" % e)