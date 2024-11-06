Feature: User registration via /client_register endpoint

  Scenario: Successfully register a new user with random data
    Given I generate random user registration data
    When I send a registration request to the /client_register endpoint
    Then the registration should succeed with a status code of 200
