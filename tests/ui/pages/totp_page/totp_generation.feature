Feature: TOTP generation

  Background:
    Given I go to the "TOTP" page
    When I already have a generated OTP

  @smoke
  Scenario: Default TOTP generation
    Then I have already pressed "TOTP" button
    * I have already generated OTPs in the OTP range section
    * I have already pressed "Format" button
    * I have already pressed "Repeat" button
    * I have already progress bar with a timer

  @smoke
  Scenario: Verify that OTP changes after default interval
    Given The default OTP lifetime is "30" seconds
    Then I wait until the next OTP will be generated

  @smoke
  Scenario: Verify that OTP changes after clicking on the "Generate OTP" button, if the "Repeat" button is turned off
    When I have already pressed "Repeat" button
    And I click on the "Repeat" button to turn it off
    And Now the "Repeat" button have an unpressed state
    And I remember current OTP to make sure that new OTP generates
    And I wait until the next OTP period to be able to generate new one
    Then I click on the "Generate OTP" button to generate new OTP
    And I make sure that the new OTP generates
