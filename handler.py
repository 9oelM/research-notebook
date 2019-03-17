import json
import requests 

def crawler(event, context):
    r = requests.get('https://apis.zigbang.com/v3/items2?lat_south=37.44033750792432&lat_north=37.69179044252958&lng_west=126.87271708120215&lng_east=127.08344785550588&room=[01,02,03,04,05]')
    response = {
        "statusCode": 200,
        "body": json.dumps(json.dumps(r.text))
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """