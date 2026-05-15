Feature: SauceDemo login
    @skip
    Scenario: Login with multiple users
        Given user launches saucedemo site
        When user enters username
        And user enters password
        And user clicks login button
        Then user should see products page