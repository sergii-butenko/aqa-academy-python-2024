def test_negative_login(git_hub_ui_app):
    """ Summary: Test negative login attemp
    Steps:
    1. Navigate to login page
    2. Enter wrong creds
    3. Click login/signin button

    Expected result
    Error saying BLA appeared
    """
    #1 Navigate to login page
    git_hub_ui_app.login_page.navigate_to()
    
    #2. Enter wrong creds
    git_hub_ui_app.try_login(username='ksdnkjfnd', password='ksdnkjfnd')

    # Expected result
    assert git_hub_ui_app.login_page.check_wrong_creds_message()