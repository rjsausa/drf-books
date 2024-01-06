from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        view_name='book-detail',
        many=True,
        read_only=True
    )
    
    class Meta:
       model = Author
       fields = ('id', 'name', 'nationality', 'books',)

class BookSerializer(serializers.HyperlinkedModelSerializer):
      author = serializers.HyperlinkedRelatedField(
            view_name='author-detail',
            read_only=True
      )

      author_id = serializers.PrimaryKeyRelatedField(
            queryset=Author.objects.all(),
            source='author'
      )

      class Meta:
            model = Book
            fields = ('id', 'author', 'author_id', 'title', 'publication_year')
