Feature: Test the hungry application
  Scenario: Verify Home Page
    Given Launch the browser
    Then verify the page title
    And close the browser

  Scenario: Verify login functionality
    Given Launch the App
    When enter login credentials
    Then click login
    Then verify the page title
    And close the App

