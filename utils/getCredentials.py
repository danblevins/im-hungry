import os
from yelpapi import YelpAPI
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from gql.transport.requests import RequestsHTTPTransport

def get_credentials():
  """This gets the yelp credentials.

  Returns:
      object: a Client object connected to the yelp api.
  """
  yelp_api_key = os.environ.get('yelp_key')
  header = {'Authorization': 'bearer {}'.format(yelp_api_key),
          'Content-Type':"application/json"}
  transport = RequestsHTTPTransport(url='https://api.yelp.com/v3/graphql', headers=header, use_json=True)
  client = Client(transport=transport, fetch_schema_from_transport=True)

  return client