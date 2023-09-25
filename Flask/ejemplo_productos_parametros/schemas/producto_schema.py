from marshmallow import Schema, fields, validate


class ProductoSchema(Schema):  # Validar los datos del producto del cliente
    nombre = fields.String(
        required=True,
        error_messages={"required": "El nombre es obligatorio"},
        validate=validate.Length(min=4, error="El nombre debe tener al menos 4 letras"),
    )
    precio = fields.Number(
        required=True,
        error_messages={"required": "El precio es obligatorio"},
        validate=validate.Range(min=0, error="El precio no puede ser negativo"),
    )