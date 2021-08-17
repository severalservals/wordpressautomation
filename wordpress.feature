Feature: Profile
	Scenario: Change Display Name
		Given I log in to Wordpress and navigate to the profile page
        When I change the display name to a new value and save
        Then The new display name should display in the display name field