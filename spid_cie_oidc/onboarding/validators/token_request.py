
from typing import Literal

from pydantic import BaseModel, HttpUrl


class TokenRequest(BaseModel):
    client_id: HttpUrl
    client_assertion: str
    client_assertion_type: Literal['urn:ietf:params:oauth:client-assertion-type:jwt-bearer']


class TokenAuthnCodeRequest(TokenRequest):
    # TODO: is 1*VSCHAR
    code: str
    # TODO: is 43*128unreserved, where unreserved = ALPHA / DIGIT / "-" / "." / "_" / "~"
    code_verifier: str
    grant_type: Literal['authorization_code']


class TokenRefreshRequest(TokenRequest):
    grant_type: Literal['refresh_token']
    refresh_token: str