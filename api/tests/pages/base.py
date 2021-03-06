from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils.timezone import now
from oauth2_provider.models import AccessToken, get_application_model

from home.factories import RootPageFactory

Application = get_application_model()
UserModel = get_user_model()


class ContentAPIBaseTestCase(TestCase):
    """
    TestCase superclass for testing content api related logic.
    It includes the logic necessary to authenticate requests.
    """

    def setUpAuthData(self):
        """
        Creates User, Application and Access Token for authenticating against the content api.
        """
        self.nhsuk_frontend_user = UserModel.objects.create_user("nhsuk-frontend-user")

        self.nhsuk_frontend_application = Application(
            name="Test NHS.UK Frontend Application",
            user=self.nhsuk_frontend_user,
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_CLIENT_CREDENTIALS,
        )
        self.nhsuk_frontend_application.save()
        self.nhsuk_frontend_token = AccessToken.objects.create(
            user=self.nhsuk_frontend_user,
            token='tokstr',
            application=self.nhsuk_frontend_application,
            expires=now() + timedelta(days=365),
            scope='read'
        )

    def setUpPages(self):
        """
        Creates the root Page and the default Site.
        """
        RootPageFactory()

    def setUp(self):
        super().setUp()
        self.setUpAuthData()
        self.setUpPages()

    def get_auth_header(self, token):
        return {
            'HTTP_AUTHORIZATION': 'Bearer ' + token,
        }

    def get_content_api_response(self, page_id=None, page_path=None, auth_headers=None):
        """
        Can be used to request the page with id == `page_id` or with path == `page_path`.
        It uses the given `auth_headers` to authenticate or the default one if not specified.
        """
        if auth_headers is None:
            auth_headers = self.get_auth_header(
                self.nhsuk_frontend_token.token
            )

        if page_id:
            url = reverse('wagtailapi:pages:detail', args=(page_id, ))
        elif page_path:
            url = reverse('wagtailapi:pages:detail_by_path', args=(page_path, ))

        return self.client.get(url, **auth_headers)

    def get_preview_content_api_response(self, page_id, revision_id=None, auth_headers=None):
        """
        Can be used to request the page with id == `page_id` and optionally revision == `revision_id`.
        It uses the given `auth_headers` to authenticate or the default one if not specified.
        """
        if auth_headers is None:
            auth_headers = self.get_auth_header(
                self.nhsuk_frontend_token.token
            )

        url = reverse('wagtailapi:preview-pages:detail', args=(page_id, ))
        if revision_id:
            url = '{}?revision-id={}'.format(url, revision_id)

        return self.client.get(url, **auth_headers)
