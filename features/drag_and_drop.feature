Feature: Exercise 1 - Drag and Drop

  Scenario: My drag and drop check for A and B
    Given I open the-internet homepage
    When I open the "Drag and Drop" page from the homepage
    And I swap box A with box B
    Then the left column header should be "B"
    And the right column header should be "A"
