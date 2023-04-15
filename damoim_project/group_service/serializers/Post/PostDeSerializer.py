from rest_framework.serializers import Serializer, CharField


class PostFormDeSerialier(Serializer):
    image = CharField(max_length=None, allow_null=True, allow_blank=True)
    contents = CharField(allow_null=False, allow_blank=False)
    def create(self, user_id:int, group_id:int):
        valid_data = self.validated_data
        valid_data.update({
            "group_id" : group_id,
            "user_id" : user_id
        })
        return valid_data

