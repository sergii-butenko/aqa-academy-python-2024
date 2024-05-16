def test_check_search_repo(git_hub_api_client):
    """
    1. send API request to find the repo named BLA
    2. Analyse the responce 
    
    Expected result:
    number of found repos == SOMENUMBER
    """

    # 1. send API request to find the repo named BLA
    repos_number, response = git_hub_api_client.search_repos("sergii")
    
    #2. Analyse the responce 
    # equal to 
    # if response.status != 200:
    #   raise Excpetion("Bad request") 
    response.raise_for_status()

    assert repos_number == 352
