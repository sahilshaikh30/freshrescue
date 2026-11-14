# ============================================================
# FRESHRESCUE
# Perishable Inventory Recovery & Waste Prevention System
# Save Stock. Recover Revenue. Reduce Waste.
# ============================================================

# Each stock batch is stored as a tuple in the inventory list.
# Tuple positions:
# 0: Batch ID, 1: Product Name, 2: Category, 3: Quantity,
# 4: Cost Price per Unit, 5: Selling Price per Unit,
# 6: Manufacturing Date, 7: Expiry Date, 8: Days Remaining.
#
# Inventory is held in memory, so records reset when the program exits.
# Dates and days remaining are entered manually and must be kept in sync.

inventory = []
next_batch_id = 1001

# A set keeps category names consistent and prevents spelling variations.
valid_categories = {
    "Bakery", "Dairy", "Fruits", "Vegetables",
    "Beverages", "Packaged Food", "Other"
}


# ============================================================
# MAIN MENU
# ============================================================

while True:
    print("""
    ========================================
                  FRESHRESCUE
    ========================================
           Save Stock. Recover Revenue.
                  Reduce Waste.
    ========================================

    1. Inventory Management
    2. Expiry Risk Analysis
    3. Smart Discount Advisor
    4. Stock Recovery Advisor
    5. Business Analytics
    6. Business Dashboard
    7. Exit

    ========================================
    """)

    try:
        choice = int(input("Enter your choice: "))

        # ====================================================
        # OPTION 1: INVENTORY MANAGEMENT
        # Add, view, search, update and remove stock batches.
        # ====================================================

        if choice == 1:
            while True:
                print("""
                =================================
                   INVENTORY MANAGEMENT
                =================================
                1. Add New Stock Batch
                2. View All Stock
                3. Search Stock Batch
                4. Update Stock Batch
                5. Remove Stock Batch
                6. Back to Main Menu
                =================================
                """)

                option = int(input("Enter your option: "))

                # OPTION 1: ADD A NEW STOCK BATCH
                if option == 1:
                    batch_id = next_batch_id
                    next_batch_id += 1

                    prod_name = input("Enter Product Name: ")
                    while True:
                        caty = input(
                            "Enter Category (Bakery, Dairy, Fruits, Vegetables, "
                            "Beverages, Packaged Food, Other): "
                        ).strip().title()

                        if caty in valid_categories:
                            break
                        else:
                            print("Please enter a category from the given list.")

                    while True:
                        quan = int(input("Enter Quantity: "))
                        if quan > 0:
                            break
                        else:
                            print("Quantity must be greater than zero!")

                    while True:
                        cost = int(input("Enter Cost Price per Unit: "))
                        if cost > 0:
                            break
                        else:
                            print("Cost price must be greater than zero!")

                    while True:
                        sel = int(input("Enter Selling Price per Unit: "))
                        if sel > 0:
                            break
                        else:
                            print("Selling price must be greater than zero!")

                    manu_date = input("Enter Manufacturing Date (DD-MM-YYYY): ")
                    exp_date = input("Enter Expiry Date (DD-MM-YYYY): ")
                    rem_day = int(input("Enter Days Remaining: "))

                    stock = (
                        batch_id, prod_name, caty, quan, cost,
                        sel, manu_date, exp_date, rem_day
                    )
                    inventory.append(stock)

                    print(f"Stock batch added successfully! Batch ID: {batch_id}")

                # OPTION 2: VIEW ALL STOCK BATCHES
                elif option == 2:
                    if not inventory:
                        print("No stock batches available!")
                    else:
                        for stock in inventory:
                            print(f"""
Batch ID: {stock[0]}
Product Name: {stock[1]}
Category: {stock[2]}
Quantity: {stock[3]}
Cost Price per Unit: ₹{stock[4]}
Selling Price per Unit: ₹{stock[5]}
Manufacturing Date: {stock[6]}
Expiry Date: {stock[7]}
Days Remaining: {stock[8]}
----------------------------------------
""")

                # OPTION 3: SEARCH FOR A BATCH USING ITS ID
                elif option == 3:
                    if not inventory:
                        print("No stock batches available!")
                    else:
                        batch_id = int(input("Enter Batch ID: "))
                        found = False

                        for stock in inventory:
                            if batch_id == stock[0]:
                                found = True
                                print(f"""
========== STOCK BATCH DETAILS ==========
Batch ID: {stock[0]}
Product Name: {stock[1]}
Category: {stock[2]}
Quantity: {stock[3]}
Cost Price per Unit: ₹{stock[4]}
Selling Price per Unit: ₹{stock[5]}
Manufacturing Date: {stock[6]}
Expiry Date: {stock[7]}
Days Remaining: {stock[8]}
==========================================
""")
                                break

                        if not found:
                            print("Stock batch not found!")

                # OPTION 4: UPDATE AN EXISTING STOCK BATCH
                elif option == 4:
                    if not inventory:
                        print("No stock batches available!")
                    else:
                        batch_id = int(input("Enter Batch ID: "))
                        found = False

                        for index, stock in enumerate(inventory):
                            if batch_id == stock[0]:
                                found = True
                                # Convert the tuple to a list so one field can be changed.
                                new_stock = list(stock)

                                while True:
                                    print("""
                                    1. Update Product Name
                                    2. Update Category
                                    3. Update Quantity
                                    4. Update Cost Price
                                    5. Update Selling Price
                                    6. Update Manufacturing Date
                                    7. Update Expiry Date
                                    8. Update Days Remaining
                                    9. Back
                                    """)

                                    new_choice = int(input("Enter your choice: "))

                                    if new_choice == 1:
                                        new_stock[1] = input("Enter the new product name: ")

                                    elif new_choice == 2:
                                        while True:
                                            new_category = input(
                                                "Enter new category (Bakery, Dairy, Fruits, "
                                                "Vegetables, Beverages, Packaged Food, Other): "
                                            ).strip().title()

                                            if new_category in valid_categories:
                                                new_stock[2] = new_category
                                                break
                                            else:
                                                print("Please enter a category from the given list.")

                                    elif new_choice == 3:
                                        new_quantity = int(input("Enter product's new quantity: "))
                                        if new_quantity > 0:
                                            new_stock[3] = new_quantity
                                        else:
                                            print("Quantity must be greater than zero!")

                                    elif new_choice == 4:
                                        new_cost = int(input("Enter product's new cost price: "))
                                        if new_cost > 0:
                                            new_stock[4] = new_cost
                                        else:
                                            print("Cost price must be greater than zero!")

                                    elif new_choice == 5:
                                        new_selling_price = int(input("Enter product's new selling price: "))
                                        if new_selling_price > 0:
                                            new_stock[5] = new_selling_price
                                        else:
                                            print("Selling price must be greater than zero!")

                                    elif new_choice == 6:
                                        new_stock[6] = input("Enter new manufacturing date (DD-MM-YYYY): ")

                                    elif new_choice == 7:
                                        new_stock[7] = input("Enter new expiry date (DD-MM-YYYY): ")

                                    elif new_choice == 8:
                                        new_stock[8] = int(input("Enter latest days remaining: "))

                                    elif new_choice == 9:
                                        break

                                    else:
                                        print("Invalid choice!")

                                # Convert the updated list back into a tuple and save it.
                                inventory[index] = tuple(new_stock)
                                print("Stock batch updated successfully!")
                                break

                        if not found:
                            print("Batch ID doesn't exist!")

                # OPTION 5: REMOVE A STOCK BATCH
                elif option == 5:
                    if not inventory:
                        print("No stock batches available!")
                    else:
                        batch_id = int(input("Enter Batch ID to remove: "))
                        found = False

                        for stock in inventory:
                            if batch_id == stock[0]:
                                found = True
                                print(f"Product: {stock[1]} | Batch ID: {stock[0]}")
                                answer = input("Are you sure you want to remove this batch? (yes/no): ")

                                if answer.lower() == "yes":
                                    inventory.remove(stock)
                                    print("Stock batch removed successfully!")
                                else:
                                    print("Stock batch removal cancelled!")
                                break

                        if not found:
                            print("Batch ID doesn't exist!")

                # OPTION 6: RETURN TO THE MAIN MENU
                elif option == 6:
                    break

                else:
                    print("Invalid Inventory Management option!")

        # ====================================================
        # OPTION 2: EXPIRY RISK ANALYSIS
        # Classify every batch according to days remaining.
        # ====================================================

        elif choice == 2:
            if not inventory:
                print("No stock batches available!")
            else:
                print("""
                ========================================
                     EXPIRY RISK ANALYSIS
                ========================================
                """)

                for stock in inventory:
                    if stock[8] <= 0:
                        condition = "Expired"
                    elif stock[8] <= 2:
                        condition = "Critical"
                    elif stock[8] <= 5:
                        condition = "High"
                    elif stock[8] <= 10:
                        condition = "Medium"
                    else:
                        condition = "Low"

                    print(f"""
Batch ID: {stock[0]}
Product Name: {stock[1]}
Days Remaining: {stock[8]}
Expiry Risk Level: {condition}
----------------------------------------
""")

        # ====================================================
        # OPTION 3: SMART DISCOUNT ADVISOR
        # Recommend discounts based on the expiry risk level.
        # Expired products are never included in expected sales.
        # ====================================================

        elif choice == 3:
            if not inventory:
                print("No stock batches available!")
            else:
                print("""
                ========================================
                     SMART DISCOUNT ADVISOR
                ========================================
                """)

                for stock in inventory:
                    if stock[8] <= 0:
                        discount = 100
                    elif stock[8] <= 2:
                        discount = 40
                    elif stock[8] <= 5:
                        discount = 25
                    elif stock[8] <= 10:
                        discount = 10
                    else:
                        discount = 0

                    discount_amt = stock[5] * discount / 100
                    new_price = stock[5] - discount_amt
                    exp_rev = stock[3] * new_price

                    print(f"""
Batch ID: {stock[0]}
Product Name: {stock[1]}
Original Selling Price: ₹{stock[5]}
Discount: {discount}%
Discount Amount: ₹{discount_amt:.2f}
Recommended Selling Price: ₹{new_price:.2f}""")

                    if stock[8] <= 0:
                        print("Recommendation: Expired - Do not sell!")
                        print("Expected Revenue: ₹0")
                    else:
                        print(f"Expected Revenue: ₹{exp_rev:.2f}")

                    print("----------------------------------------")

        # ====================================================
        # OPTION 4: STOCK RECOVERY ADVISOR
        # Suggest the most suitable action for each batch.
        # Donation is only a possibility for safe-to-consume stock.
        # ====================================================

        elif choice == 4:
            if not inventory:
                print("No stock batches available!")
            else:
                print("""
                ========================================
                     STOCK RECOVERY ADVISOR
                ========================================
                """)

                for stock in inventory:
                    if stock[8] <= 0:
                        recovery_action = "Discard safely"
                    elif stock[8] <= 2:
                        recovery_action = "Urgent sale"
                    elif stock[8] <= 5:
                        recovery_action = "Discount or bundle"
                    elif stock[8] <= 10:
                        recovery_action = "Promotional sale"
                    else:
                        recovery_action = "Normal sale"

                    print(f"""
Batch ID: {stock[0]}
Product Name: {stock[1]}
Days Remaining: {stock[8]}
Recovery Recommendation: {recovery_action}""")

                    if stock[8] > 0:
                        print("Additional Option: Donation may be considered if the stock is safe to consume.")

                    print("----------------------------------------")

        # ====================================================
        # OPTION 5: BUSINESS ANALYTICS
        # Calculate inventory value, expiry exposure and
        # estimated revenue recovery for unexpired at-risk stock.
        # ====================================================

        elif choice == 5:
            if not inventory:
                print("No stock batches available!")
            else:
                print("""
                ========================================
                      BUSINESS ANALYTICS
                ========================================
                """)

                # Calculate overall inventory statistics.
                total_batches = len(inventory)
                total_quantity = 0
                total_cost_value = 0
                total_sales_value = 0

                for stock in inventory:
                    total_quantity += stock[3]
                    total_cost_value += stock[3] * stock[4]
                    total_sales_value += stock[3] * stock[5]

                # Calculate the value exposed to expiry risk.
                at_risk_value = 0
                recoverable_value = 0
                expired_batches = 0
                at_risk_batches = 0

                for stock in inventory:
                    if stock[8] <= 5:
                        at_risk_value += stock[3] * stock[4]
                        at_risk_batches += 1

                    if stock[8] <= 0:
                        expired_batches += 1

                    elif stock[8] <= 2:
                        new_price = stock[5] * 0.60
                        recoverable_value += stock[3] * new_price

                    elif stock[8] <= 5:
                        new_price = stock[5] * 0.75
                        recoverable_value += stock[3] * new_price

                print("\n========== INVENTORY OVERVIEW ==========")
                print(f"Total Stock Batches: {total_batches}")
                print(f"Total Inventory Quantity: {total_quantity}")
                print(f"Total Inventory Cost Value: ₹{total_cost_value:.2f}")
                print(f"Total Potential Sales Value: ₹{total_sales_value:.2f}")

                print("\n========== EXPIRY RISK ANALYSIS ==========")
                print(f"At-risk Stock Batches: {at_risk_batches}")
                print(f"Expired Stock Batches: {expired_batches}")
                print(f"At-risk Inventory Cost Value: ₹{at_risk_value:.2f}")

                print("\n========== REVENUE RECOVERY ==========")
                print(f"Potential Recoverable Revenue: ₹{recoverable_value:.2f}")
                print("Note: This is an estimate, not guaranteed revenue.")

        # ====================================================
        # OPTION 6: BUSINESS DASHBOARD
        # Present the key inventory, expiry and financial
        # indicators together with priority business actions.
        # ====================================================

        elif choice == 6:
            if not inventory:
                print("No stock batches available!")
            else:
                print("""
                ========================================
                       FRESHRESCUE DASHBOARD
                ========================================
                """)

                # Calculate the overall inventory position.
                total_batches = len(inventory)
                total_quantity = 0
                total_cost_value = 0
                total_sales_value = 0

                for stock in inventory:
                    total_quantity += stock[3]
                    total_cost_value += stock[3] * stock[4]
                    total_sales_value += stock[3] * stock[5]

                # Count batches in each expiry risk category.
                expired = 0
                critical = 0
                high = 0
                medium = 0
                low = 0

                at_risk_value = 0
                recoverable_revenue = 0

                for stock in inventory:
                    if stock[8] <= 0:
                        expired += 1
                        at_risk_value += stock[3] * stock[4]

                    elif stock[8] <= 2:
                        critical += 1
                        at_risk_value += stock[3] * stock[4]
                        new_price = stock[5] * 0.60
                        recoverable_revenue += stock[3] * new_price

                    elif stock[8] <= 5:
                        high += 1
                        at_risk_value += stock[3] * stock[4]
                        new_price = stock[5] * 0.75
                        recoverable_revenue += stock[3] * new_price

                    elif stock[8] <= 10:
                        medium += 1

                    else:
                        low += 1

                # Display the inventory and financial overview.
                print("\n========== INVENTORY OVERVIEW ==========")
                print(f"Total Batches: {total_batches}")
                print(f"Total Units: {total_quantity}")
                print(f"Inventory Cost Value: ₹{total_cost_value:.2f}")
                print(f"Potential Sales Value: ₹{total_sales_value:.2f}")

                print("\n========== EXPIRY STATUS ==========")
                print(f"Expired Batches: {expired}")
                print(f"Critical Risk: {critical}")
                print(f"High Risk: {high}")
                print(f"Medium Risk: {medium}")
                print(f"Low Risk: {low}")

                print("\n========== FINANCIAL OVERVIEW ==========")
                print(f"At-risk Inventory Value: ₹{at_risk_value:.2f}")
                print(f"Potential Recoverable Revenue: ₹{recoverable_revenue:.2f}")
                print("Note: Recoverable revenue is an estimate.")

                # Display alerts only when stock needs attention.
                print("\n========== PRIORITY ALERTS ==========")

                if expired > 0:
                    print(f"URGENT: {expired} expired batch(es) - Remove from sale.")

                if critical > 0:
                    print(f"CRITICAL: {critical} batch(es) - Arrange urgent sale.")

                if high > 0:
                    print(f"HIGH: {high} batch(es) - Apply discounts or bundle.")

                if medium > 0:
                    print(f"MEDIUM: {medium} batch(es) - Plan promotional sales.")

                if expired == 0 and critical == 0 and high == 0 and medium == 0:
                    print("All stock batches are currently at low expiry risk.")

                # Suggest actions based on the batches found.
                print("\n========== BUSINESS RECOMMENDATIONS ==========")

                if expired > 0:
                    print("Remove expired stock and arrange safe disposal.")

                if critical > 0:
                    print("Prioritize critical stock for immediate sale.")

                if high > 0:
                    print("Offer discounts or bundle high-risk products.")

                if medium > 0:
                    print("Plan promotions for medium-risk products.")

                if low > 0:
                    print("Continue normal stock rotation for low-risk products.")

                print("\n==============================================")

        # OPTION 7: EXIT THE APPLICATION
        elif choice == 7:
            print("Thank you for using FreshRescue!")
            break

        else:
            print("Invalid choice! Please select an option from 1 to 7.")

    except ValueError:
        # Handle invalid numeric input without crashing the application.
        print("Invalid input! Please enter a valid number.")
