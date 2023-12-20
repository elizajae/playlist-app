"""Forms for playlist app."""

from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import InputRequired, Length
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    
    name = StringField('Name', validators=[InputRequired(), Length(min=1, max=50)])
    description = StringField('Description', validators=[InputRequired(), Length(min=1, max=50)])
    submit = SubmitField('Add Playlist')

class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Title', validators=[InputRequired(), Length(min=1, max=50)])
    artist = StringField('Artist', validators=[InputRequired(), Length(min=1, max=50)])
    submit = SubmitField('Add Song')
    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song to add', coerce=int)
    submit = SubmitField('Add Song')
