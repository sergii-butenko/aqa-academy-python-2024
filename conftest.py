import pytest
from src.applications.ui.github_ui import GitHubUI
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
    githubui_app.open() # webdriver method - BAD
    
    # generators in python
    yield githubui_app

    # PostStep. Close the App
    githubui_app.close() # webdriver method - BAD