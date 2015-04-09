from django.contrib import admin
from member.models import Member, Organization, OrganizationType


class MemberAdmin(admin.ModelAdmin):
    list_display = ('pk','user')

admin.site.register(Member, MemberAdmin)
admin.site.register(Organization)
admin.site.register(OrganizationType)

