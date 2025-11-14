from . import models, serializers as ss

class GetChoicesMixin():
    @action(detail=False, methods=["get"])
    def get_choices(self, request):
        serializer = self.get_serializer()
        choices_dict = {}
        for field_name, target_field in serializer.fields.items():
            if not isinstance(target_field, ChoiceField):
                continue
            choices_dict[field_name] = getattr(target_field, "choices", None)
        return Response(choices_dict, status=status.HTTP_200_OK)

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def retrieve(self, request, pk=None):
        from django.shortcuts import get_object_or_404
        #queryset = self.get_queryset()
        #instance = get_object_or_404(queryset, pk=pk)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.action == "retrieve": # list, create, retrieve, update, partial_update, destroy
            return YourModelDetailSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=['post'], serializer_class=ss.HogeSerializer)
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response({'status': 'password set'})

