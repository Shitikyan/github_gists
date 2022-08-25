import datetime
import json

import requests

from config import GITHUB_URL
from services.error import GistGetError


def get_gists_since(username: str, since: datetime.datetime = None):
    query_url = f"{GITHUB_URL}/{username}/gists?since={since.isoformat()}" if since else f"{GITHUB_URL}/{username}/gists"
    r = requests.get(query_url)
    data = json.loads(r.text)
    if 'message' in data:
        raise GistGetError(http_status_code=r.status_code, http_message=data['message'])

    return data
