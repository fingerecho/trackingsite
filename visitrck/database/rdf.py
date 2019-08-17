import sys
import requests
import json
sys.path.append("..")
import settings

def query(sparql_query, format_mimetype='application/sparql-results+json'):
    auth = (settings.SPARQL_AUTH_USR, settings.SPARQL_AUTH_PWD)
    data = {'query': sparql_query}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': format_mimetype
    }
    try:
        r = requests.post(settings.SPARQL_QUERY_URI, auth=auth, data=data, headers=headers, timeout=1)
        return r.text
    except Exception as e:
        raise e


def query_turtle(sparql_query):
    data = {'query': sparql_query, 'format': 'text/turtle'}
    auth = (settings.SPARQL_AUTH_USR, settings.SPARQL_AUTH_PWD)
    headers = {'Accept': 'text/turtle'}
    r = requests.post(settings.SPARQL_QUERY_URI, data=data, auth=auth, headers=headers, timeout=1)
    try:
        return r.text
    except Exception as e:
        raise


def insert(g, named_graph_uri=None):
    if named_graph_uri:
        data = {'update': 'INSERT DATA { GRAPH <' + named_graph_uri + '> { ' + g.serialize(format='nt').decode("utf-8") + ' } }'}
    else:  # insert into default graph
        data = {'update': 'INSERT DATA { ' + g.serialize(format='nt').decode("utf-8") + ' }'}
    auth = (settings.SPARQL_AUTH_USR, settings.SPARQL_AUTH_PWD)
    headers = {'Accept': 'text/turtle'}
    try:
        r = requests.post(settings.SPARQL_UPDATE_URI, headers=headers, data=data, auth=auth, timeout=1)
        if r.status_code != 200 and r.status_code != 201:
            raise Exception('The INSERT was not successful. The SPARQL database\' error message is: ' + r.text)
        return True
    except requests.ConnectionError as e:
        raise Exception()


def update(sparql_update_query, format_mimetype='application/sparql-results+json'):
    auth = (settings.SPARQL_AUTH_USR, settings.SPARQL_AUTH_PWD)
    data = {'update': sparql_update_query}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': format_mimetype
    }
    try:
        r = requests.post(settings.SPARQL_UPDATE_URI, auth=auth, data=data, headers=headers, timeout=1)
        return r.text
    except Exception as e:
        raise e

# def cleardb():
#     update("")