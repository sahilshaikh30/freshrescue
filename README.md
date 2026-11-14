# FreshRescue

**Save Stock. Recover Revenue. Reduce Waste.**

A Python console system that helps small retailers manage perishable stock. It tracks batches by expiry date, flags what is at risk, recommends discounts, and estimates how much revenue can still be recovered. Built to solve a real problem: perishable products often expire unsold because nobody acts on them in time.

## Features
- **Inventory management:** add, view, search, update, and remove stock batches
- **Expiry risk analysis:** classifies every batch as Expired, Critical, High, Medium, or Low risk
- **Smart discount advisor:** suggests a discount based on risk level and shows the new price and expected revenue
- **Stock recovery advisor:** recommends an action per batch (urgent sale, bundle, promotion, safe disposal)
- **Business analytics:** inventory value, at-risk stock value, and estimated recoverable revenue
- **Dashboard:** expiry status counts, financial overview, priority alerts, and business recommendations

## How the risk levels work
| Days remaining | Risk level | Suggested discount | Recovery action |
|---|---|---|---|
| 0 or less | Expired | Do not sell | Discard safely |
| 1 to 2 | Critical | 40% | Urgent sale |
| 3 to 5 | High | 25% | Discount or bundle |
| 6 to 10 | Medium | 10% | Promotional sale |
| More than 10 | Low | None | Normal sale |

## Tech used
- Python 3
- Standard library only (no installs needed)

## How to run
1. Make sure Python 3 is installed
2. Download or clone this repo
3. Run:
   ```
   python freshrescue.py
   ```
4. Start with **Inventory Management** to add a few batches, then try the analysis options

## What I practiced
- Storing records as tuples in a list, and converting them to lists to update one field
- Using a set to keep category names consistent
- Nested menus with `while` loops and `try/except` for invalid input
- Looping through records to calculate totals, risk counts, and revenue estimates
- Turning business rules into code (discount tiers, expiry risk levels)

## Known issues
- Data is stored in memory only, so all batches are lost when the program closes
- Days remaining is typed in manually, so it can go out of sync with the expiry date
- Dates are not validated; they are stored as plain text
- Invalid input inside a menu (for example, text instead of a number) returns you to the main menu, and a batch ID may be skipped if this happens while adding a batch
- Prices and quantities accept whole numbers only
- There is no check that the selling price is higher than the cost price
- Discount percentages are fixed in the code and cannot be changed by the user

## Planned improvements
- Calculate days remaining automatically from the expiry date using `datetime`
- Save and load inventory using SQLite or a CSV file
- Validate dates and every numeric input with `try/except`
- Break the code into functions to remove repeated sections
- Let the user set their own discount rules
- Analyze stock and waste trends over time with pandas
