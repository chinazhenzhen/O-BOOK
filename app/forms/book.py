#利用wtforms进行

from wtforms import Form,StringField,IntegerField
from wtforms.validators import Length,NumberRange,DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(),Length(min=1,max=30)])
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)  #default 默认值