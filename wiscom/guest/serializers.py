from rest_framework import serializers
from datetime import datetime  # datetime 모듈 추가

from .models import Guest


class CommentSerializer(serializers.ModelSerializer):
    created_at=serializers.SerializerMethodField()
    class Meta:
        model = Guest
        # fields = ('name', 'comment')
        fields = ['id','content', 'created_at']

    def get_created_at(self, obj):
        return datetime.now().strftime("%Y-%m-%d")