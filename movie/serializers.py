from rest_framework import serializers

from movie.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'posterUrl', 'plot')


class MovieDetailSerializer(serializers.ModelSerializer):
    watched = serializers.SerializerMethodField()

    def get_watched(self, obj):
        user = self.context.get('request').user
        if obj.watched_user.filter(id=user.id).exists():
            return True
        else:
            return False

    class Meta:
        model = Movie
        fields = ('title', 'plot', 'genre', 'keywords', 'runtime', 'watched', 'posterUrl')
