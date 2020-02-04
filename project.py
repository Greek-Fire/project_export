#!/usr/bin/python
import json
import sys
try:
    import requests
except ImportError:
    print "Please install the python-requests module."
    sys.exit(-1)

AT_API = 'https://at.example.net/api/v2/'
USERNAME = "admin"
PASSWORD = "redhat"
SSL_VERIFY = False   # Ignore SSL for now

def get_json(url):
    # Performs a GET using the passed URL location
    r = requests.get(url, auth=(USERNAME, PASSWORD), verify=SSL_VERIFY)
    return r.json()

def get_results(url):
    jsn = get_json(url)
    if jsn.get('error'):
        print "Error: " + jsn['error']['message']
    else:
        if jsn.get('results'):
            return jsn['results']
        elif 'results' not in jsn:
            return jsn
        else:
            print "No results found"
    return None

def display_all_results(url):
    results = get_results(url)
    if results:
        print json.dumps(results, indent=4, sort_keys=True)

def grab_project_names(url):
    temp_ids = [] 
    j = get_json(url) 
    for temp in j['results']:
          temp_ids.append(temp['name'])
    print temp_ids
      
      

def main():
  #display_all_results('https://at.example.net/api/v2/projects/')
  grab_project_names(AT_API + 'projects/')


if __name__ == "__main__":
    main()
