import urllib.request,json
from .models import Quote

quote_url = "http://quotes.stormconsultancy.co.uk/random.json"

def get_quote():
  """
  Function to consume http request and return a Quote class instance
  """
  with urllib.request.urlopen(quote_url) as url:
    get_quotes_data = url.read()
    get_quotes_response = json.loads(get_quotes_data)

    quote_results={}

    if get_quotes_response['quote']:
      quote_results['id'] = get_quotes_response['id']
      quote_results['author'] = get_quotes_response['author']
      quote_results['quote'] = get_quotes_response['quote']
    
  return quote_results