from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

#Clase utilizada para después validar formulario y mandar mensaje de error
class ValidatorForm(FlaskForm):
    nombre = StringField('Nombre', validators=[ DataRequired(message="El nombre es requerido, no apodos")])
    apellidos = StringField('Apellidos', validators=[ DataRequired(message="El primer apellido es requerido")])
    mail = StringField('Mail', validators=[ DataRequired(message="El mail es requerido, no spam")])
    telefono = FloatField('Télefono', validators=[ DataRequired(message="El teléfono es requerido, para comunidad de WhatsApp")])
    
    
    submit = SubmitField('Guardar')