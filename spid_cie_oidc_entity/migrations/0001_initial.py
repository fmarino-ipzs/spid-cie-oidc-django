# Generated by Django 4.0.2 on 2022-02-05 11:39

from django.db import migrations, models
import spid_cie_oidc_entity.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FederationEntityConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('sub', models.URLField(help_text='URL that identifies this Entity in the Federation. This value and iss are the same in the Entity Configuration.', max_length=255)),
                ('default_exp', models.PositiveIntegerField(default=33, help_text='how many minutes from now() an issued statement must expire')),
                ('default_signature_alg', models.CharField(default='RS256', help_text='default signature algorithm, eg: RS256', max_length=16)),
                ('authority_hints', models.JSONField(blank=True, default=list, help_text='only required if this Entity is an intermediary')),
                ('jwks', models.JSONField(default=spid_cie_oidc_entity.models.FederationEntityConfiguration._create_jwks, help_text='a list of public keys')),
                ('trust_marks', models.JSONField(blank=True, default=list, help_text='which trust marks MUST be exposed in its entity configuration')),
                ('trust_marks_issuers', models.JSONField(blank=True, default=dict, help_text='which issuers are allowed to issue trust marks for the descendants. Example: {"https://www.spid.gov.it/certification/rp": ["https://registry.spid.agid.gov.it", "https://intermediary.spid.it"],"https://sgd.aa.it/onboarding": ["https://sgd.aa.it", ]}')),
                ('entity_metadatas', models.JSONField(default=dict, help_text='federation_entity metadata, eg: {"federation_entity": { ... },"openid_provider": { ... },"openid_relying_party": { ... },"oauth_resource": { ... }}')),
                ('http_timeout', models.PositiveIntegerField(default=5, help_text='in seconds')),
                ('verify_https_cert', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=False, help_text='If this configuration is active. At least one configuration must be active')),
            ],
            options={
                'verbose_name': 'Federation Entity Configuration',
                'verbose_name_plural': 'Federation Entity Configurations',
            },
        ),
    ]