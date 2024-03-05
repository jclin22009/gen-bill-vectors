import requests

def test_search(query):
    # Replace the URL below with your Flask server URL; use localhost if running locally
    url = 'https://bill-searcher-a10dbe344e55.herokuapp.com/search'
    params = {'query': query}

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        print("Search Results:")
        results = response.json()
        for i, result in enumerate(results, start=1):
            print(f"{i}. {result['title']} (similarity: {result['similarity']:.2f})")
    else:
        print("Error:", response.status_code, response.text)

if __name__ == '__main__':
    while True:
        query = input("Enter a search query (or type 'exit' to exit): ")
        if query.lower() == 'exit':
            print("Exiting search...")
            break
        test_search(query)
        print("\n")
