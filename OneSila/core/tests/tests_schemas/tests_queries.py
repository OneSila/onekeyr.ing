from strawberry.relay import from_base64, to_base64
from django.test import TestCase, TransactionTestCase
from django.contrib.auth import get_user_model
from model_bakery import baker
from core.models import MultiTenantCompany
from strawberry_django.test.client import TestClient
from django.urls import reverse_lazy


class TransactionTestCaseMixin:
    def setUp(self):
        self.multi_tenant_company = baker.make(MultiTenantCompany)
        self.user = baker.make(get_user_model(), multi_tenant_company=self.multi_tenant_company)

    def to_global_id(self, *, model_class, instance_id):
        type_name = f"{model_class.__name__}Type"
        return to_base64(type_name, instance_id)

    def stawberry_test_client(self, **kwargs):
        test_client = TestClient('/graphql/')
        with test_client.login(self.user):
            return test_client.query(**kwargs)
