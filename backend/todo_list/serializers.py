from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import TodoList, ListItem, Folder


class ListItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListItem
        fields = ['title', 'description', 'completed', 'priority']

class TodoListSummarySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    items = ListItemsSerializer(many=True)

    class Meta:
        model = TodoList
        fields = ['title','date_updated','items',]

class FolderSummarySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = ('id', 'title',)

class FolderSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    todo_lists = TodoListSummarySerializer(many=True, read_only=True)

    class Meta:
        model = Folder
        fields = ('id', 'title','todo_lists')

class TodoListSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    items = ListItemsSerializer(many=True)
    folder = FolderSummarySerializer(required=False)
    url = serializers.HyperlinkedIdentityField(
        view_name= "todolist_detail",
        lookup_field = "pk"
    )

    class Meta:
        model = TodoList
        fields = [  
            'id',
            # 'user',
            'title',
            'date_updated',
            'items',
            'folder',
            'endpoint',
            'path',
            'url'
        ]

    # def create(self, validated_data):
    #     items_data = validated_data.pop('items')
    #     folders_data = validated_data.pop('folder')

    #     todo_list = TodoList.objects.create(**validated_data)


    #     for item_data in items_data:
    #         ListItem.objects.create(**item_data)

    #     for folder_data in folders_data:
    #         Folder.objects.create(todo_list=todo_list, **folder_data)

    #     return todo_list