from urllib.request import Request, urlopen
from urllib.parse import urlencode


def lambda_handler(event, context):

    print("Starting top-100 spider")

    values = {
        'project' : '560372',
        'spider' : 'top100'
    }
    data = urlencode(values)
    payload = data.encode('ascii') # data should be bytes

    headers = {
        'Authorization': 'Basic MWIzODU5MTdkZGRmNGRlMTk2N2QyZTRjMGQwYWNmZDM6',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    req = Request(
        url="https://app.scrapinghub.com/api/run.json",
        method="POST",
        data=payload,
        headers=headers
    )

    with urlopen(req) as response:
        res = response.read()


