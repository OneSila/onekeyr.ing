from core import models
from core.models.multi_tenant import MultiTenantUserMultiAwareMixin, MultiTenantCompany

class DistributionKey(models.Model):
    """
    Optional key used by the users to give access to servers.
    This keys should be added to the server the first time 
    and our tasks should be using this private-key to make connection.

    We should generate a new key for every new company and provide instructions how to
    add them to the servers.
    """
    name = models.CharField(max_length=100)
    private_key = models.TextField()
    public_key = models.TextField()

    def __str__(self):
        return self.name



class UserKey(MultiTenantUserMultiAwareMixin, models.Model):
    """
    These are the keys that need adding to authorized_access.
    """
    name = models.CharField(max_length=100)
    public_key = models.TextField()
    active = models.BooleanField()

    def __str__(self):
        return self.name