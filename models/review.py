from models.base_model import BaseModel

class Review(BaseModel):
    """ Class representing a review """
    place_id = ""
    user_id = ""
    text = ""
