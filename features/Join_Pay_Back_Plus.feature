Feature: join payback plus

  Scenario: to Validate user is able launch the browser
    Given Chrome is opened and Payback app is opened
    When user cliks on login icon
    And user enters mobile number "9153336666"
    And user enters pin "1032"
    When user selects Check Box on reCAPTCHA
    Then User clicks on login button


  Scenario: to Validate user is able click join Payback plus button
  Given Chrome is opened and Payback app is opened
  When User clicks on join payback plus button
  Then It shows payback plus page


  Scenario:Validate user can access the Email Id
    Given Chrome is opened and Payback app is opened
    When user cliks on login icon
    And user enters mobile number "9153336666"
    And user enters pin "1032"
    When user selects Check Box on reCAPTCHA
    Then User clicks on login button
   Given Chrome is opened and Payback app is opened
    When user clicks on join payback plus button
    Then  User enters email Id "jananikhila@gmail.com"


   Scenario: Validate user can access the Mobile number
    Given Chrome is opened and Payback app is opened
     When user clicks on join payback plus button
     And user removes the default mobile number
     And user enters mobile number "9014634163"
     Then user clicks the confirm button


  Scenario:Validate user can access the invalid Email Id
    Given Chrome is opened and Payback app is opened
    When user clicks on join payback plus button
    Then user removes the default email Id
    And  User enters invalid invalid email Id "harshinib1313@gmail.com"




