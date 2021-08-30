from pytest_bdd import scenario, when, then, parsers
from steps.common_actions import PageActions

actions = PageActions()


@scenario('../features/campaign page.feature', 'User is verifying the list of safety features')
def test_safety():
    pass

@scenario('../features/campaign page.feature', 'User is verifying the list of testimonials')
def test_testimonials():
    pass

@scenario('../features/campaign page.feature', 'User is verifying the Innovation')
def test_innovation():
    pass

@scenario('../features/campaign page.feature', 'User is verifying the list of Models')
def test_models():
    pass

@scenario('../features/campaign page.feature', 'User is verifying the Top Panel')
def test_top_panel():
    pass


@when(parsers.parse('user clicks on {button} in {page}'))
def click_action(button, page):
    actions.click_button(button, page)


@then(parsers.parse('the below options should be available in the {page}:\n{options}'))
def list_check(page, options):
    actions.check_list(page, options)
