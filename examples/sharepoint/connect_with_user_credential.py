"""
Demonstrates how to authenticate with user credentials (username and password) in non-interactive mode


"""
from office365.sharepoint.client_context import ClientContext
from tests import test_site_url, test_username, test_password

ctx = ClientContext(test_site_url).with_user_credentials(test_username, test_password)
web = ctx.web.get().execute_query()
print(web.url)
