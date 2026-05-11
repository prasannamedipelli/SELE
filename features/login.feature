Feature: SauceDemo login

    Scenario Outline: Login with multiple users
        Given user launches saucedemo site
        When user enters username "<username>"
        And user enters password "secret_sauce"
        And user clicks login button
        Then user should see products page
        Examples:
            | username                |
            | standard_user           |
            | problem_user            |
            | performance_glitch_user |