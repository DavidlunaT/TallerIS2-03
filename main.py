def display_membership_plans():
    print("Membership Plans:")
    print("1. Basic - $30/month (Includes: Gym Access)")
    print("2. Premium - $50/month (Includes: Gym Access, Sauna, Locker)")
    print("3. Family - $90/month (Includes: Full Facility Access for 4 Members)")
    return input("Select a membership plan (1-3): ")

def get_addons(for_family=False, num_members=1):
    print("\nAvailable Add-Ons:")
    print("1. Personal Training Session - $20/session")
    print("2. Group Classes - $15/month")
    print("3. Swimming Pool Access - $10/month")
    
    total_addon_cost = 0

    for i in range(num_members):
        if for_family:
            print(f"\nAdd-ons for Member {i+1}:")
        sessions = int(input("  Personal Training Sessions: "))
        group = input("  Group Classes (y/n): ").lower() == 'y'
        swim = input("  Swimming Pool Access (y/n): ").lower() == 'y'

        cost = sessions * 20
        if group:
            cost += 15
        if swim:
            cost += 10
        total_addon_cost += cost

    return total_addon_cost

def calculate_total_cost(plan_choice, addon_cost):
    if plan_choice == '1':
        base_cost = 30
    elif plan_choice == '2':
        base_cost = 50
    elif plan_choice == '3':
        base_cost = 90
    else:
        print("Invalid membership choice.")
        return

    total_cost = base_cost + addon_cost

    # Apply family discount
    if plan_choice == '3' and addon_cost > 50:
        discount = total_cost * 0.10
        total_cost -= discount
        print(f"\nGroup Discount Applied: -${discount:.2f}")

    print(f"\nBase Membership Cost: ${base_cost:.2f}")
    print(f"Add-ons Cost: ${addon_cost:.2f}")
    print(f"Total Monthly Cost: ${total_cost:.2f}")

def main():
    plan_choice = display_membership_plans()
    if plan_choice == '3':
        addon_cost = get_addons(for_family=True, num_members=4)
    else:
        addon_cost = get_addons()

    calculate_total_cost(plan_choice, addon_cost)

if __name__ == "__main__":
    main()
