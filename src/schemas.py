from typing import List

from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime


class UserSchema(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    email: EmailStr
    password: str = Field(min_length=6, max_length=10)


class UserResponseSchema(BaseModel):
    id: int
    username: str
    email: str
    avatar: str

    class Config:
        from_attributes : True


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RequestEmail(BaseModel):
    email: EmailStr


class ResetPasswordSchema(BaseModel):
    new_password: str
    r_new_password: str


# {{{ Image


class ImageDb(BaseModel):
    id: int
    image: str
    small_image: str
    about: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes : True


class ImageAboutUpdateSchema(BaseModel):
    image_id: int
    about: str


class ImageAboutUpdateResponseSchema(BaseModel):
    image_id: int
    message: str


class ReturnMessageResponseSchema(BaseModel):
    message: str


class SmallImageReadResponseSchema(BaseModel):
    image_id: int
    small_image_url: str
    short_about: str

    class Config:
        from_attributes : True


class ImageReadResponseSchema(BaseModel):
    image_id: int
    image_url: str
    about: str

    class Config:
        from_attributes = True


# }}}


class CommentDb(BaseModel):
    id: int
    comment: str
    emo_joy: int
    emo_anger: int
    emo_sadness: int
    emo_surprise: int
    emo_disgust: int
    emo_fear: int
    created_at: datetime
    updated_at: datetime
    image_id: int
    user_id: int

    class Config:
        orm_mode = True


class CommentCreateSchema(BaseModel):
    id: int
    text: str = Field(max_length=300)


class CommentShowSchema(BaseModel):
    comment: str


class CommentShowAllSchema(BaseModel):
    comments: List[CommentShowSchema]


class CommentUpdateSchema(BaseModel):
    comment_id: int
    image_id: int
    comment: str = Field(max_length=300)


class CommentDeleteSchema(BaseModel):
    comment_id: int
    image_id: int
