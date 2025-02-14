from marshmallow import fields, post_load, Schema


class NewSchema(Schema):
    user_id = fields.Int(data_key="id")
    postition =  fields.Str()

class UserSchema(Schema):

    user_id = fields.Int(data_key="id")
    name = fields.Str()
    gender = fields.Str()
    email = fields.Str()
    status = fields.Int()
    additional_field = fields.Nested(NewSchema, many=True)  # list of NewSchema objects


    @post_load
    def creating_object(self, data, **kwargs):
        return UserDTO(**data)


class UserDTO:

    def __init__(self, user_id, name, gender, email, status, additional_field=None):
        self.user_id = user_id
        self.name = name
        self.gender = gender
        self.email = email
        self.status = status
        self.additional_field = additional_field