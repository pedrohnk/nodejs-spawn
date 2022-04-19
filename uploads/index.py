import sys
import json
from urllib import request

def main():
	item = json.loads(sys.argv[1])

	url = item.get('url')
	filePath = item.get('filePath')
	data = open(filePath, 'rb').read()

	requestData = request.Request(url, data)
	responseData = request.urlopen(requestData).read().decode('utf-8')
	print(responseData)

if __name__ == '__main__':
	main()

#  python3 index.py '{"filePath": "my-data.csv", "url": "http://localhost:3000"}'