from pydantic import BaseModel


class Mouse(BaseModel):
    name : str
    company : str
    cost: int
    rating : float
    description : str
    photo : str


class Keyboard(BaseModel):
    name : str
    company : str
    cost: int
    rating : float
    description : str
    photo : str


class Headphone(BaseModel):
    name : str
    company : str
    cost: int
    rating : float
    description : str
    photo : str


class Microphone(BaseModel):
    name : str
    company : str
    cost: int
    rating : float
    description : str
    photo : str

class Device(BaseModel):
    type : str
    cost: int