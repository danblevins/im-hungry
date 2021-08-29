import os
from yelpapi import YelpAPI

def query_rest_api(food, location):
  """This queries the yelp rest api.

  Args:
      food (string): the user's choice of food
      location (string): the user's choice of location

  Returns:
      [json/dict]: A rest api call in json/ dictionary form.
  """
  yelp_api_key = YelpAPI(os.environ.get('yelp_key'))
  restaurant_query = yelp_api_key.search_query(term=food, location=location, radius=40000, limit=10, sort_by='best_match', open_now=True)
  
  return restaurant_query