
def get_graphql_query_output(restaurant_query):
  """This prepares the yelp graphql api output for the web page.

  Args:
      restaurant_query (json/dict): This is the output from the api call in json/ dictionary form.

  Returns:
      list: A list of restaurants with their descriptions.
  """
  output = []
  
  for index_restaurant in range(len(restaurant_query['search']['business'])):
    temp_dict = {}
    temp_list = []

    temp_dict['name'] = restaurant_query['search']['business'][index_restaurant]['name']
    temp_dict['price'] = restaurant_query['search']['business'][index_restaurant]['price']
    temp_dict['rating'] = restaurant_query['search']['business'][index_restaurant]['rating']
    temp_dict['num_rating'] = restaurant_query['search']['business'][index_restaurant]['review_count']
    temp_dict['address'] = (
        restaurant_query['search']['business'][index_restaurant]['location']['address1'] + ', ' 
        + restaurant_query['search']['business'][index_restaurant]['location']['city'] + ', ' 
        + restaurant_query['search']['business'][index_restaurant]['location']['state'] + ', ' 
        + restaurant_query['search']['business'][index_restaurant]['location']['country']
    )

    for category in range(len(restaurant_query['search']['business'][index_restaurant]['categories'])):
        try:
            temp_list.append(category['search']['business'][index_restaurant]['categories'][category]['alias'])
            temp_dict['category'] = ' / '.join(temp_list)
        except:
            temp_dict['category'] = 'N/A'
    output.append(temp_dict)

  return output
  