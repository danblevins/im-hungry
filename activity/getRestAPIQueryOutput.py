
def get_rest_api_query_output(restaurant_query):
  """This prepares the yelp rest api output for the web page.

  Args:
      restaurant_query (json/dict): This is the output from the api call in json/ dictionary form.

  Returns:
      list: A list of restaurants with their descriptions.
  """
  output = []

  for restaurant in range(len(restaurant_query['businesses'])):
    temp_dict = {}
    temp_list = []

    temp_dict['name'] = restaurant_query['businesses'][restaurant]['name']
    try: 
      temp_dict['price'] = restaurant_query['businesses'][restaurant]['price']
    except:
      temp_dict['price'] = 'N/A'
    temp_dict['rating'] = restaurant_query['businesses'][restaurant]['rating']
    temp_dict['num_rating'] = restaurant_query['businesses'][restaurant]['review_count']
    temp_dict['address'] = ', '.join(restaurant_query['businesses'][restaurant]['location']['display_address'])

    for category in range(len(restaurant_query['businesses'][restaurant]['categories'])):
      try:
        temp_list.append(restaurant_query['businesses'][restaurant]['categories'][category]['title'])
        temp_dict['category'] = ' / '.join(temp_list)
      except:
        temp_dict['category'] = 'N/A'
        
    output.append(temp_dict)
  
  return output