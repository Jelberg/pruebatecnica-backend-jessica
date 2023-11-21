from marshmallow import Schema, fields

class TaskSchema(Schema):
    #id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    completed = fields.Boolean()