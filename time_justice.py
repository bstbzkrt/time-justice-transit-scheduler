def main():
    print("==============================================")
    
    # 1. Initialize our transit database using a nested dictionary structure
    # Keys represent routes, values represent their current mobility attributes
    transit_network = {
        "Boulevard Green Spine": {"frequency_mins": 6, "accessible": True, "corridor": "Central"},
        "Gebizli Neighborhood Shuttle": {"frequency_mins": 20, "accessible": True, "corridor": "East-Suburban"},
        "University Express Link": {"frequency_mins": 8, "accessible": False, "corridor": "North-Academic"},
        "Coastal Ring Line": {"frequency_mins": 15, "accessible": True, "corridor": "West-Coast"},
        "Industrial Worker Corridor": {"frequency_mins": 30, "accessible": False, "corridor": "South-Industrial"}
    }
    
    print(" Welcome to the Eco-Transit Mobility & Equity Tool")
    print("==============================================")
    
    while True:
        print("\nAvailable Commands:")
        print("1) View entire network status")
        print("2) Analyze route efficiency & social equity")
        print("3) Update route parameters")
        print("4) Exit program")
        
        choice = input("\nEnter your selection (1-4): ").strip()
        
        if choice == "1":
            print("\n--- Current Transit Network Status ---")
            for route, data in transit_network.items():
                accessibility_status = "Fully Accessible ✅" if data["accessible"] else "Needs Infrastructure Upgrade ⚠️"
                print(f"• Route: {route}")
                print(f"  [Corridor]: {data['corridor']} | [Frequency]: Every {data['frequency_mins']} mins | [Status]: {accessibility_status}")
        
        elif choice == "2":
            print("\n--- Social Equity & Time Justice Analysis ---")
            total_routes = len(transit_network)
            accessible_count = 0
            high_frequency_count = 0
            
            for route, data in transit_network.items():
                if data["accessible"]:
                    accessible_count += 1
                if data["frequency_mins"] <= 10:
                    high_frequency_count += 1
            
            # Calculate percentages
            accessibility_pct = (accessible_count / total_routes) * 100
            
            print(f"• Total Routes Evaluated: {total_routes}")
            print(f"• Network Accessibility Score: {accessibility_pct:.1f}% of routes support inclusive infrastructure.")
            print(f"• High-Frequency Corridors (Wait times <= 10 mins): {high_frequency_count} routes.")
            print("\n💡 Planning Insight: Routes with wait times over 15 minutes disproportionately burden low-income or vulnerable commuters.")
            
        elif choice == "3":
            print("\n--- Update Route Parameters ---")
            route_name = input("Enter the exact name of the route to modify: ")
            
            if route_name in transit_network:
                new_freq = int(input("Enter new headway frequency (in minutes): "))
                is_accessible = input("Is this line step-free and universally accessible? (yes/no): ").lower() == 'yes'
                
                # Update the dictionary values
                transit_network[route_name]["frequency_mins"] = new_freq
                transit_network[route_name]["accessible"] = is_accessible
                print(f"\nSuccess: {route_name} has been updated in the mobility database!")
            else:
                print("Error: Route name not found in database. Please check spelling and try again.")
                
        elif choice == "4":
            print("\nThank you for using the Eco-Transit Tool. Happy planning!")
            break
        else:
            print("Invalid selection. Please choose a option between 1 and 4.")

if __name__ == '__main__':
    main()
