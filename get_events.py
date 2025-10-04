import asana
from asana.rest import ApiException
from pprint import pprint
from get_initial_sync import fetch_init, fetch_latest
import time
from update_tasks import update_task
import os

from dotenv import load_dotenv
load_dotenv()
ACCESS_TOKEN = os.getenv("ASANA_PAT")
#print(ACCESS_TOKEN)

try:
    # Get events on a resource
    init_sync = fetch_init()

    cur_task_gid = 0
    while True:
        time.sleep(10)
        init_sync, data = fetch_latest(init_sync)
        pprint(data)
        for event in data:
            if event['action'] == 'added' and event['parent']['resource_type'] == 'project' and event['resource']['name'] != "":
                print(event['parent']['name'], event['resource']['name'])
                newtask_name = event['parent']['name'] + " - " + event['resource']['name']
                cur_task_gid = event['resource']['gid']
                update_task(newtask_name, event['resource']['gid'])
            elif event['action'] == 'changed' and event['resource']['resource_type'] == 'task':
                update_task(event['resource']['name'], cur_task_gid)

except ApiException as e:
    print("Exception when calling EventsApi->get_events: %s\n" % e)