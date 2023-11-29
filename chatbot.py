import requests
from flask import Flask, request

app=Flask(__name__)
@app.route('/',methods=['POST'])
def index():
    data=request.get_json()
    source_currency=data['queryResult']['parameters']['unit-currency']['currency']
    
    amount=data['queryResult']['parameters']['unit-currency']['amount']
    target_currency=data['queryResult']['parameters']['currency-name']
    print(source_currency)
    print(amount)
    print(target_currency)
    cf=fetch_conversion_factor(source_currency, target_currency)
    final_amount=amount*cf
    response={
        'fulfillmentText': f"{final_amount} {target_currency}"
    }
    print(final_amount)
    return "hello"
def fetch_conversion_factor(source, target):
    url="https://api.currencyapi.com/v3/latest?apikey=cur_live_IjjYgZIv5eZLc8DjVkDyrqoBoFexHZEU0UR00Xld".format(source,target)
    response=requests.get(url)
    response=response.json()
    print(response)
    return response['{}_{}'.format(source,target)]
if __name__=="__main__":
    app.run(debug=True)