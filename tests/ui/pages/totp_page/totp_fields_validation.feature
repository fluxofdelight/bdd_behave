Feature: TOTP fields validation

  Background:
    Given I go to the "TOTP" page
    And The default OTP Length is "6" digits


  @smoke
  Scenario Outline: Verify "Code Length" fields validation positive <value>
    When I clear the "Code Length" field
    # bug in the next step
    Then The "Generate OTP" button becomes "disabled"
    And I enter the "<value>" in the "Code Length" field
    And The "Generate OTP" button becomes "active"
    And I click on the "Generate OTP" button to generate new OTP
    And I make sure that new OTP "has" "<value>" length

    Examples:
      | value |
      |   1   |
      |   6   |
      |   8   |
      |   9   |


  @negative
  Scenario Outline: Verify "Code Length" fields validation negative <value>
    When I clear the "Code Length" field
    # bug in the next step
    Then The "Generate OTP" button becomes "disabled"
    And I enter the "<value>" in the "Code Length" field
    But The "Generate OTP" button still has "disabled" state
    And I wait until the next OTP will be generated
    # bug in the next step
    And I make sure that new OTP "has" "default" length

    Examples:
      | value |
      |  -1   |
      |  0    |
      |  10   |
      |  100  |
      |  ''   |