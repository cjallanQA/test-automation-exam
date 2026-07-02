Feature: Exercise 3 - Dynamic Content

  Scenario: My dynamic content check after refresh
    Given I open the-internet homepage
    When I open the "Dynamic Content" page from the homepage
    And I record the dynamic content rows
    And I refresh the page
    Then I should see which dynamic rows changed
