class GistGetError(Exception):
    def __init__(self, http_status_code, http_message):
        self.http_status_code = http_status_code
        self.http_message = http_message
