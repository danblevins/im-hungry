from flask import Flask, redirect, url_for, render_template, request, json

from queryGraphQL import query_graphql
from getGraphQLQueryOutput import get_graphql_query_output
from queryRestAPI import query_rest_api
from getRestAPIQueryOutput import get_rest_api_query_output

app = Flask(__name__)

### Web Pages ###
@app.route("/", methods=['POST', 'GET'])
def index():
  """This is the flask app.

  Returns:
      render_template: The index.html web page, output, food, location, and message
  """
  output = []
  food = request.form.get("Food", 'Food')
  location = request.form.get("Location", 'City, State or Zipcode')

  if food in ['Food',''] and location in ['City, State or Zipcode','']:
    message = ''
    output = ''
  else:
    try:
      message = 'View your results below! (Results loaded using GraphQL)'
      query = query_graphql(food, location)
      output = get_graphql_query_output(query)
    except:
      message = 'View your results below! (Results loaded using RestAPI)'
      query = query_rest_api(food, location)
      output = get_rest_api_query_output(query)

  return render_template("index.html", output=output, food=food, location=location, message=message)

if __name__ == '__main__':
    app.run(debug=False)