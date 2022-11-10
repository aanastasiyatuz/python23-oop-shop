class BaseSerializer:
    class Meta:
        fields = []
        objects = []

    def serialize_obj(self, obj):
        representation = {}
        for field in self.Meta.fields:
            # field = 'title'
            # obj.title == getattr(obj, 'title')
            data = getattr(obj, field)
            representation[field] = data
        return representation

    def serialize_objects(self):
        representation = []
        for obj in self.Meta.objects:
            obj_repr = self.serialize_obj(obj)
            representation.append(obj_repr)
        return representation
