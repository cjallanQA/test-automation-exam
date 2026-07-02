Feature: Exercise 2 - Infinite Scroll

  Scenario: My infinite scroll check with additional content load
    Given I open the-internet homepage
    When I open the "Infinite Scroll" page from the homepage
    Then I should see content as soon as the page loads
    When I scroll to load more content blocks
    Then I should reach the last loaded content block
