import socket

import requests

try:
    r = requests.get('http://checkip.amazonaws.com')
    print(r.text.strip())
    r.raise_for_status()

except requests.exceptions.HTTPError as err:
    raise SystemExit(err)

except requests.exceptions.ConnectionError as ce:
    # network problem Requests will raise a "ConnectionError"
    print(ce)

except requests.exceptions.Timeout as to:
    # Maybe set up for a retry, or continue in a retry loop
    print(to)

except requests.exceptions.TooManyRedirects as tmr:
    # Tell the user their URL was bad and try a different one
    print(tmr)

except requests.exceptions.RequestException as re:
    # catastrophic error. bail.
    raise SystemExit(re)
