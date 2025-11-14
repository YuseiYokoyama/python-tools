from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

class CustomerDetailSerializer(WritableNestedModelSerializer):
    contact_set = ContactSerializer(many=True, read_only=False, required=False)
    delete_contact_set = serializers.PrimaryKeyRelatedField(
        #INFO info of contact.flg_delete is collected to delete_contact_set
        many=True, queryset=models.Contact.objects.all(), write_only=True, required=False
    )
    class Meta:
        model = models.Customer
        fields = '__all__'

    def update(self, customer, validated_data):
        res = super().update(customer, validated_data)
        delete_contact_set = validated_data.pop('delete_contact_set', [])
        delete_contact_pk_set = [contact.pk for contact in delete_contact_set]
        models.Contact.objects.filter(customer=customer, pk__in=delete_contact_pk_set).delete()
        return res

    def to_internal_value(self, data):

        def overwrite_customer(): # allow ContactSerializer.customer empty
            customer_id = data.get("id")
            for data_contact in data.get("contact_set", []):
                data_contact["customer"] = customer_id # allow ContactSerializer.customer empty

        def collect_delete_contact_set():
            if not data.get("delete_contact_set"):
                data["delete_contact_set"] = []
            new_contact_set = []
            for data_contact in data.get("contact_set", []):
                if str_to_bool(data_contact.get("flg_delete", "False")) and data_contact["pk"]:
                    data["delete_contact_set"].append(data_contact["pk"]) # collect delete_contact_set
                else:
                    new_contact_set.append(data_contact)
            data["contact_set"] = new_contact_set

        overwrite_customer()
        collect_delete_contact_set()
        return super().to_internal_value(data)

