# This script it is just to test if the api of naive bias model is working or not!
import requests

text = input("Enter your description:\n")
api_url = f"http://127.0.0.1:5000/text-classify/{text}"
response = requests.get(api_url).json()

if __name__ == "__main__":
    print(response)