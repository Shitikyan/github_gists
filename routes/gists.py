from fastapi import APIRouter

from models.response import Response
from services.error import GistGetError
from services.gist_request import get_gist_request_date_by_username, update_gist_request_date, create_gist_request
from services.github import get_gists_since

router = APIRouter()


@router.get("/{username}")
async def get_gists(username: str):
    # Create or update in DB
    prev_request_date = get_gist_request_date_by_username(username)
    if prev_request_date:
        update_gist_request_date(username)
    else:
        create_gist_request(username)

    # Make github call
    try:
        gists = get_gists_since(username, prev_request_date)
    except GistGetError as e:
        return Response(data=None, code=e.http_status_code, message=e.http_message)

    return Response(data=gists, code=200, message="")
