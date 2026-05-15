Feature: Window Handling
Scenario: Handle new browser window
Given user opens window paractice page
When user clicks open new window button
Then user switches to child window
And user verifies child window title
And user switces back to parent windows