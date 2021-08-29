from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from gql.transport.requests import RequestsHTTPTransport

from utils.getCredentials import get_credentials

def query_graphql(food, location):
  """This queries the yelp graphql api.

  Args:
      food (string): the user's choice of food
      location (string): the user's choice of location

  Returns:
      [json/dict]: A graphql call in json/ dictionary form.
  """
  client = get_credentials()

  str_graphql = ("""{{search(term: "{}",
                location: "{}",
                radius: 40000,
                limit: 10,
                sort_by: "best_match") {{
            business {{
                name
                price
                rating
                review_count
                location {{
                    address1
                    city
                    state
                    country
                }}
                categories {{
                    alias
                }}
            }}
        }}
    }}
  """).format(food, location)
  c = client.execute(gql(str_graphql))

  return query