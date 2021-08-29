from pytest_bdd import scenario, when, then, parsers
from steps.Actions.common_actions import PageActions

@scenario('../features/campaign page.feature', 'User is verifying the list of safety features')
def test_safety():
    pass