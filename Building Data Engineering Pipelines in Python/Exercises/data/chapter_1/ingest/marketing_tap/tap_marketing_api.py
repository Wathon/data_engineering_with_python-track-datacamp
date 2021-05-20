import requests
import singer

api_netloc = "localhost:5000"
api_key = "scientist007"
shops_template = f"http://{api_netloc}/{api_key}/diaper/api/v1.0/shops"
items_template = f"http://{api_netloc}/{api_key}/diaper/api/v1.0/items/"

# Complete the JSON schema
schema = {'properties': {
    'brand': {'type': 'string'},
    'model': {'type': 'string'},
    'price': {'type': 'number'},
    'currency': {'type': 'string'},
    'quantity': {'type': 'integer', 'minimum': 1},
    'date': {'type': 'string', "format": "date"},
    'countrycode': {'type': 'string', 'pattern': "^[A-Z]{2}$"},
    'store_name': {'type': 'string'}},
    '$schema': 'http://json-schema.org/draft-07/schema#'
}

# Write the schema to stdout.
singer.write_schema(stream_name='products', schema=schema, key_properties=[])


# Return the set of items scraped from a specific store as a list
def retrieve_store_items(store_name, items_endpoint=items_template):
    return requests.get(f"{items_endpoint}{store_name}").json()["items"]


def main():
    for shop in requests.get(shops_template).json()["shops"]:
        singer.write_records(stream_name='products',
                             # Add the name of the store to every record.
                             records=({'store_name': shop, **item}
                                      for item in retrieve_store_items(shop)))


if __name__ == "__main__":
    main()

