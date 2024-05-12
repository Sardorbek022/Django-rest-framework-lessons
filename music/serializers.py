from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from music.models import (
    Album, Artist, Song
)

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist 
        fields = '__all__'
        

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        # fields = '__all__'
        fields = ('id', 'title', 'albom', 'cover', 'source')
    
    def validate_source(self, value):
        if not value.endswith('.mp3'):
            raise ValidationError(detail='Mp3 File is required')
        
        return value