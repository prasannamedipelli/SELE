Feature: Selenium Downloads Navigation
@skip
Scenario: Verify Downloads link navigation
Given user launches browser
When user switches to selenium iframe
And user clicks Downloads link
Then Downloads page should open