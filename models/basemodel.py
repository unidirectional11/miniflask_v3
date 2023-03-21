from pydantic import BaseModel
from datetime import datetime


class Base(BaseModel):

    url: str
    created: datetime
    edited: datetime


if __name__ == "__main__":
    data = {
        "created": "2014-12-10T16:36:50.509000Z",
        "edited": "2014-12-10T16:36:50.509000Z",
        "url": "https://swapi.dev/api/people/1",
    }

    obj = Base(**data)
    breakpoint()