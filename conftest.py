import pytest
from src.applications.ui.github_ui import GitHubUI
from src.applications.api.github_api import GitHubAPIClient
from selenium import webdriver

# hook for pytest plugin
def pytest_html_report_title(report):
    report.title = "AQA Python Academy!"

# fixture for tests
@pytest.fixture
def git_hub_ui_app():
    driver = webdriver.Firefox()

    #1. Prestep. Navigate to GithubAPP
    githubui_app = GitHubUI(browser=driver)
    githubui_app.open()
    
    # generators in python
    yield githubui_app

    # PostStep. Close the App
    githubui_app.close() 


@pytest.fixture
def git_hub_api_client():
    # create file with users data
    # _file = create_file({'user': 'serg'})
    git_hub_api_client = GitHubAPIClient()

    yield git_hub_api_client

    # remove file with users data
    # remove_file(_file)
    