import requests

def test():
    url="https://graph.facebook.com/v19.0/me?fields=id%2Cname&access_token=EAAGMh8rfDZCUBO2rZA2MRmLTlUBHyFZBTUmCTZBZBZCNsu7TsokRY0r3ZAXMpUCWOfYWIwbujo0kjqSoOvVOkDymU7LWZCtfelb1wTXMKxNruZBcRc1m4o9a3lnP8PH2tqZBX8GTUJLWL7xb5ltvgpshz2dZCZAFksa66YNXmaoo06TZCMcFO9sPE1Rx6pNZBRYCCSrZBscBlOLMvghuf3CuZCZCAJT8tTV1RBIcO886rzNlZCvjgkSTvk6q6wZCLZAilxKzCy9eWxvSM8SwZBwZDZD"
    d=requests.get(url)
    print(d.content)
