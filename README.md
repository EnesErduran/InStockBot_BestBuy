# Best Buy Bot for Items over $200

## Features
- Refreshes link until "Add to Cart" button is available
- Automate entire checkout process
- Due to items over $200 requiring extra steps and information on checkout, the steps for automating those purchases differ.

## Prerequisites
- Sign up for a Best Buy account
- Add all billing/shipping info to your account (must only have one card on the account)

## Dependencies
- Selenium
	- `pip install selenium`
- Undetected Chrome Driver
    - 'pip install undetected-chromedriver'
    - You have to use undetected-chromedriver instead of the regular one due to websites blocking the regular one
- [Google Chrome](https://www.google.com/chrome/)


## Running the Bot
1. Make sure you have [Python 3.9](https://www.python.org/downloads/release/python-390/)
2. Edit the info.py file with all your information
3. Navigate to your project directory and run the bot.py script from your preferred environment
4. Feel free to change the Best Buy links in the bot.py file to any item on bestbuy.com


