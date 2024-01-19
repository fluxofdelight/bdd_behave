Feature: OCRA URI generation

    Background:
    Given I go to the "OCRA" page

    @smoke @check
    Scenario: Verify the correct URI generation on the OCRA page
      Given the following data exist:
        | issuer      | label     | secret           | algorithm | otp_length_ocra |
        | test_issuer | test_name | QQQQQQQQQQQQQQQQ | SHA512    | 8               |
      When I clear the "Issuer" field and enter the "issuer" in it
      * I clear the "Label" field and enter the "label" in it
      * I clear the "Secret key (base32)" field and enter the "secret" in it
      * I select the "algorithm" in the "Algorithm" drop-down
      * I select the "otp_length_ocra" in the "OCRA Length" drop-down
      Then I remember current OTP to make sure that new OTP generates
      * I remember current URI to make sure that new URI generates
      * I click on the "Generate OTP" button to generate new OTP and URI
      * I make sure that the new OTP generates
      * I make sure that the new URI generates
      * I make sure that the URI has this value:
        """
        otpauth://ocra/test_issuer%3Atest_name?secret=QQQQQQQQQQQQQQQQ&algorithm=SHA512&digits=8
        """
