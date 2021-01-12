import requests

# How to print the version of an installed module
# stolen from damienfrancois https://stackoverflow.com/users/1763614/damienfrancois
# From StackOverflow
# From https://stackoverflow.com/a/20180564
print(requests.__version__)

# Reading text content from a http request
# stolen from Jortega https://stackoverflow.com/users/7551712/jortega
# From StackOverflow
# From https://stackoverflow.com/a/58036567
print(requests.get("https://raw.githubusercontent.com/bui1/cmput404lab1/master/lab1.py").text)
