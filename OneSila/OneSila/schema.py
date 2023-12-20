from django.conf import settings

import strawberry
import strawberry_django

from strawberry import auto
from strawberry_django import auth, mutations
from strawberry_django.optimizer import DjangoOptimizerExtension

from core.schema.countries import CountryQuery
from core.schema.languages import LanguageQuery
from core.schema.multi_tenant import MultiTenantQuery, MultiTenantMutation, MultiTenantSubscription


#
# Actual Query and Mutation declarations
#

@strawberry.type
class Query(CountryQuery, LanguageQuery, MultiTenantQuery):
    pass


@strawberry.type
class Mutation(MultiTenantMutation):
    pass


@strawberry.type
class Subscription(MultiTenantSubscription):
    pass

#
# Schema itself.
#


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscription,
    extensions=[DjangoOptimizerExtension()]
)
