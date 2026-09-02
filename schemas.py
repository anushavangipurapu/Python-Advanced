from marshmallow import Schema, fields, validate


class EmployeeSchema(Schema):

    id = fields.Int(dump_only=True)

    name = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=100)
    )

    email = fields.Email(
        required=True
    )

    department = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=100)
    )

    salary = fields.Float(
        required=True,
        validate=validate.Range(min=0)
    )