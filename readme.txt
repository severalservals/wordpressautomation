This solution has only one test. More would have been nice, but I've only used 
Python a little, Behave and Gherkin not at all, and it took some time to come 
up to speed with them. Since those are the tools AWeber uses, I thought the 
tradeoff would be worth it as long as my test demonstrated an understanding of
general test automation principles. 

The test logs in to Wordpress, updates the public display name and verifies 
that the updated display name is shown in the display name cell on the sidebar. 

The test uses a randomly generated value for the new display name so it's 
rerunnable. 

Chromedriver will need to be in your local path for the test to work. 

You can execute the test by calling
    behave
from the root solution directory. 