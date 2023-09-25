from marshmallow import Schema,fields, validate


class TareaSchema(Schema):  # Validar los datos del producto del cliente
    descripcion = fields.String(
        required=True,
        error_messages={"required": "La descripción es obligatoria"},
        validate=validate.Length(min=5, error="La descripción debe tener al menos 5 letras"),
    )