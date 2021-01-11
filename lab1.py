import requests

// Reading text content from a http request
// stolen from Jortega https://stackoverflow.com/users/7551712/jortega
// From StackOverflow
// From https://stackoverflow.com/a/58036567
print(requests.get("https://raw.githubusercontent.com/bui1/cmput404lab1/master/lab1.py").text)
