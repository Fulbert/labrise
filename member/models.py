from django.db import models

class Member(models.Model):
    # can link to a member (enable to create non-member pilot)
    user = models.OneToOneField('auth.User',default=0)
    organizations = models.ManyToManyField('Organization', blank=True,null=True)

    favorite_points = models.ManyToManyField('space.Point',blank=True,null=True)
    gears = models.ManyToManyField('gear.Gear',blank=True,null=True)

    def __str__(self):
        return self.user.get_username()

class Organization(models.Model):
    group = models.OneToOneField('auth.Group',blank=True,null=True)
    organization_type = models.ManyToManyField('OrganizationType')
    owners = models.ManyToManyField('Member',blank=True,null=True)

    auto_accept = models.BooleanField(default=False)
    is_open = models.BooleanField(default=True)

    name = models.CharField(max_length=50)
    desc = models.TextField(blank=True,null=True)

    addresses = models.ManyToManyField('space.Address',blank=True,null=True)

    def __str__(self):
        return self.name

class OrganizationType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class OrganizationQueue(models.Model):
    organization = models.ForeignKey('Organization')
    member = models.ForeignKey('Member')

def create_member(backend, user, response, *args, **kwargs):
    if not hasattr(user, 'member'):
        member = Member(user_id=user.id)
        member.save()