Feature: Exercise 4 - Horizontal Slider

  Scenario: My slider check using keyboard arrows
    Given I open the-internet homepage
    When I open the "Horizontal Slider" page from the homepage
    And I set the slider to "3.5" using keyboard input
    Then the slider value should be "3.5"
