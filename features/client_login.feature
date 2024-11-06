Feature: User login via /client_login endpoint

  Scenario: Successfully login with valid credentials
    Given I generate random login data
    When I send a login request to the /client_login endpoint
    Then I should receive a token and a status code of 200
