from django.contrib import admin

from .models import (
    FederationDescendant,
    FederationDescendantContact,
    FederationEntityProfile,
    FederationEntityAssignedProfile,
    FederationDescendantJwk,
)


class FederationDescendantContactAdminInline(admin.TabularInline):
    model = FederationDescendantContact
    extra = 0
    readonly_fields = ("created", "modified")
    raw_id_fields = ("entity",)


class FederationDescendantJwkAdminInline(admin.StackedInline):
    model = FederationDescendantJwk
    extra = 0
    readonly_fields = ("created", "modified")
    raw_id_fields = ("jwk",)


@admin.register(FederationDescendant)
class FederationDescendantAdmin(admin.ModelAdmin):
    list_display = ("sub", "name", "status", "is_active", "created")
    list_filter = ("type", "created", "modified", "is_active")
    search_fields = ("sub",)
    readonly_fields = (
        "created",
        "modified",
        "entity_statement_as_json",
    )
    inlines = (
        FederationDescendantJwkAdminInline,
        FederationDescendantContactAdminInline,
    )


@admin.register(FederationDescendantJwk)
class FederationDescendantJwkAdmin(admin.ModelAdmin):
    list_display = ("descendant", "jwk", "created")
    list_filter = ("created", "modified")
    search_fields = (
        "descendant__sub",
        "kid",
    )


@admin.register(FederationEntityProfile)
class FederationEntityProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "profile_id")
    list_filter = ("created", "modified")
    search_fields = ("name", "profile_id", "created", "modified")
    readonly_fields = ("trust_mark_template_as_json",)


@admin.register(FederationEntityAssignedProfile)
class FederationEntityAssignedProfileAdmin(admin.ModelAdmin):
    list_display = ("descendant", "profile", "issuer", "created")
    raw_id_fields = ("descendant", "profile", "issuer")
    list_filter = ("created", "modified")
    search_fields = ("descendant__sub", "descendant__name", "profile")
    readonly_fields = (
        "trust_mark_as_json", "trust_mark", "created", "modified"
    )