from flask_wtf import FlaskForm
from wtforms import StringField, IntField, SubmitField
from wtforms.validators import DataRequired, Lenght, ValidationError


class ValidatorForm(FlaskForm):
    nombre = StringField('Nombre', validators=[ DataRequired(message="El nombre es requerido, no apodos")])
    apellidos = StringField('Apellidos', validators=[ DataRequired(message="El primer apellido es requerido")])
    email = StringField('E-mail', validators=[ DataRequired(message="El mail es requerido, no spam")])
    telefono = IntField('Télefono', validators=[ DataRequired(message="El teléfono es requerido, para comunidad de WhatsApp")])
    
    
    submit = SubmitField('Guardar')