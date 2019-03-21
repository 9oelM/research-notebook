import json
import requests 

def getJson(file):
    with open(file) as f:
        data = json.load(f)
    return data

def toJson(response):
    return response.json()

def getIdAndType(data):
    processed = []
    for room in enumerate(data['list_items']):
        processed.append(
            { 'id': room[1]['simple_item']['item_id'], 
              'type': room[1]['section_type']
            }
        )
    return processed
    
def getSubInfo(data):
    detailedItemURL = 'https://apis.zigbang.com/v3/items'
    detailedItemURLPayload = {'detail':'true', 'item_ids': []}
    
    for counter, piece in enumerate(data):
        detailedItemURLPayload['item_ids'] = '[%d]' % piece['id']
        resp = requests.get(detailedItemURL, params=detailedItemURLPayload)
        item = resp.json()['items'][0]['item'] # it's a single element array
        
        info = ['agent_lat', 'agent_lng', 'deposit', 'rent', 'manage_cost', 'floor', 'floor_all', 'building_type', 'near_subways', 'options', 'parking', 'room_type', 'size_m2']
        for subinfo in info:
            piece.update({
                subinfo: item[subinfo]
            })
    return data