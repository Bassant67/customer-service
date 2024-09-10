import hashlib
import time
import re

# In-memory storage for simplicity
users_db = {}

def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

def validate_password(password):
    """Validate password strength."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one number."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."
    return True, "Password is strong."

def register():
    username = input("Enter a username: ")
    if username in users_db:
        print("Username already exists. Please try again.")
        return
    while True:
        password = input("Enter a password: ")
        valid, message = validate_password(password)
        if valid:
            break
        else:
            print(message)
    
    hashed_password = hash_password(password)
    users_db[username] = hashed_password
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hash_password(password)
    if username in users_db and users_db[username] == hashed_password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False

def ask_question(question):
    response = input(question + " (yes/no): ").strip().lower()
    while response not in ['yes', 'no']:
        print("Invalid response. Please answer with 'yes' or 'no'.")
        response = input(question + " (yes/no): ").strip().lower()
    return response == 'yes'

def handle_soil_problem():
    print("\nHandling soil problem...")
    if ask_question("Is the soil too dry?"):
        print("Solution: Increase the frequency of watering.")
        print("Explanation: Dry soil can harm plant growth. Regular watering keeps soil moisture balanced.")
    elif ask_question("Is the soil too wet?"):
        print("Solution: Improve drainage and reduce watering.")
        print("Explanation: Wet soil can lead to root rot. Better drainage helps maintain healthy roots.")
    else:
        print("Solution: Test the soil pH and adjust accordingly.")
        print("Explanation: Correct pH levels ensure optimal nutrient uptake by plants.")
    time.sleep(2)

def handle_algae_problem():
    print("\nHandling algae problem...")
    if ask_question("Is there excessive sunlight on the water surface?"):
        print("Solution: Reduce sunlight exposure by using shades or aquatic plants.")
        print("Explanation: Excessive sunlight promotes algae growth. Shading reduces light penetration.")
    elif ask_question("Is there nutrient runoff from nearby land?"):
        print("Solution: Implement buffer zones to reduce nutrient runoff.")
        print("Explanation: Nutrients from runoff feed algae. Buffer zones filter nutrients before they enter the water.")
    else:
        print("Solution: Use algaecides or introduce algae-eating fish.")
        print("Explanation: Algaecides kill algae, and algae-eating fish naturally control their population.")
    time.sleep(2)

def handle_water_quality():
    print("\nHandling water quality issues...")
    if ask_question("Is the water cloudy?"):
        print("Solution: Use a water clarifier and check for sediment sources.")
        print("Explanation: Cloudy water can indicate suspended particles. Clarifiers help settle particles.")
    elif ask_question("Is there a bad odor from the water?"):
        print("Solution: Aerate the water and remove decaying organic matter.")
        print("Explanation: Aeration increases oxygen levels, which helps break down organic matter causing odors.")
    else:
        print("Solution: Test the water for contaminants and treat accordingly.")
        print("Explanation: Contaminants can harm aquatic life. Regular testing ensures water safety.")
    time.sleep(2)

def handle_plant_health():
    print("\nHandling plant health problems...")
    if ask_question("Are the plants showing yellow leaves?"):
        print("Solution: Check for nutrient deficiencies and provide fertilizers.")
        print("Explanation: Yellow leaves often indicate a lack of nutrients. Fertilizers replenish essential nutrients.")
    elif ask_question("Are the plants wilting?"):
        print("Solution: Ensure adequate watering and check for pests.")
        print("Explanation: Wilting can result from water stress or pest damage. Proper watering and pest control are crucial.")
    else:
        print("Solution: Prune damaged parts and monitor plant health regularly.")
        print("Explanation: Pruning removes unhealthy parts and promotes overall plant health.")
    time.sleep(2)

def handle_erosion_control():
    print("\nHandling erosion control...")
    if ask_question("Is there visible soil erosion around the water body?"):
        print("Solution: Plant ground cover vegetation to stabilize the soil.")
        print("Explanation: Ground cover plants help hold soil in place, reducing erosion.")
    elif ask_question("Are the banks of the water body collapsing?"):
        print("Solution: Use riprap or retaining walls to reinforce the banks.")
        print("Explanation: Riprap and retaining walls provide physical barriers to prevent bank collapse.")
    else:
        print("Solution: Implement terracing or contour plowing techniques.")
        print("Explanation: These techniques reduce runoff speed and soil erosion.")
    time.sleep(2)

def handle_pest_control():
    print("\nHandling pest control...")
    if ask_question("Are there visible pests on the plants?"):
        print("Solution: Use organic or chemical pesticides as appropriate.")
        print("Explanation: Pesticides help control pest populations and protect plant health.")
    elif ask_question("Are there signs of pest damage on the plants?"):
        print("Solution: Introduce natural predators to control pest populations.")
        print("Explanation: Natural predators keep pest populations in check without chemicals.")
    else:
        print("Solution: Regularly inspect and maintain plant health to prevent infestations.")
        print("Explanation: Early detection and maintenance prevent severe pest issues.")
    time.sleep(2)

def handle_ph_balance():
    print("\nHandling pH balance...")
    if ask_question("Is the pH level too high?"):
        print("Solution: Add sulfur or acidifiers to lower the pH.")
        print("Explanation: Lowering pH creates a more acidic environment, suitable for certain plants.")
    elif ask_question("Is the pH level too low?"):
        print("Solution: Add lime or alkaline substances to raise the pH.")
        print("Explanation: Raising pH creates a more alkaline environment, suitable for certain plants.")
    else:
        print("Solution: Maintain regular testing and adjust pH levels as needed.")
        print("Explanation: Consistent monitoring ensures the optimal pH for plant growth.")
    time.sleep(2)

def handle_nutrient_management():
    print("\nHandling nutrient management...")
    if ask_question("Is there excessive nutrient buildup in the water?"):
        print("Solution: Reduce fertilizer use and implement nutrient management plans.")
        print("Explanation: Excessive nutrients can lead to algae blooms. Proper management prevents buildup.")
    elif ask_question("Are the plants showing signs of nutrient deficiency?"):
        print("Solution: Apply appropriate fertilizers to address deficiencies.")
        print("Explanation: Fertilizers provide essential nutrients needed for plant growth.")
    else:
        print("Solution: Regularly monitor nutrient levels and adjust accordingly.")
        print("Explanation: Regular monitoring helps maintain balanced nutrient levels for healthy plants.")
    time.sleep(2)

def handle_aquatic_ecosystem():
    print("\nHandling aquatic ecosystem management...")
    if ask_question("Is the biodiversity of the ecosystem declining?"):
        print("Solution: Introduce native species to restore biodiversity.")
        print("Explanation: Native species support ecosystem balance and biodiversity.")
    elif ask_question("Are there signs of ecosystem imbalance?"):
        print("Solution: Monitor and adjust the population dynamics of key species.")
        print("Explanation: Balancing species populations ensures ecosystem health.")
    else:
        print("Solution: Implement habitat restoration and conservation practices.")
        print("Explanation: Restoration and conservation improve habitat quality and support biodiversity.")
    time.sleep(2)

def handle_sediment_control():
    print("\nHandling sediment control...")
    if ask_question("Is there significant sediment buildup in the water?"):
        print("Solution: Use sediment traps and regularly dredge the water body.")
        print("Explanation: Sediment traps capture particles, and dredging removes accumulated sediment.")
    elif ask_question("Is sediment affecting water quality?"):
        print("Solution: Implement erosion control measures to reduce sediment runoff.")
        print("Explanation: Erosion control prevents sediment from entering the water, maintaining quality.")
    else:
        print("Solution: Regularly monitor sediment levels and maintain sediment control structures.")
        print("Explanation: Regular monitoring and maintenance ensure effective sediment control.")
    time.sleep(2)

def handle_invasive_species():
    print("\nHandling invasive species management...")
    if ask_question("Are there invasive species present in the ecosystem?"):
        print("Solution: Use mechanical, chemical, or biological methods to control invasive species.")
        print("Explanation: Different methods target invasive species to protect the ecosystem.")
    elif ask_question("Are the invasive species causing ecosystem damage?"):
        print("Solution: Implement management plans to mitigate damage.")
        print("Explanation: Management plans address the impact of invasive species and restore balance.")
    else:
        print("Solution: Regularly monitor and manage for early detection of invasive species.")
        print("Explanation: Early detection and management prevent widespread issues.")
    time.sleep(2)

def handle_water_filtration():
    print("\nHandling water filtration systems...")
    if ask_question("Is the water filtration system not functioning properly?"):
        print("Solution: Check and replace filters as needed.")
        print("Explanation: Replacing filters maintains effective water filtration.")
    elif ask_question("Is there a decrease in water flow rate?"):
        print("Solution: Inspect and clean the filtration system.")
        print("Explanation: Cleaning improves flow rate and system efficiency.")
    else:
        print("Solution: Regularly maintain and service the filtration system.")
        print("Explanation: Regular maintenance ensures optimal performance and water quality.")
    time.sleep(2)

def handle_fish_health():
    print("\nHandling fish health and management...")
    if ask_question("Are the fish showing signs of disease?"):
        print("Solution: Isolate and treat the affected fish with appropriate medications.")
        print("Explanation: Treating sick fish prevents disease spread and maintains fish health.")
    elif ask_question("Is the fish population declining?"):
        print("Solution: Ensure adequate food supply and suitable habitat conditions.")
        print("Explanation: Proper nutrition and habitat conditions support a healthy fish population.")
    else:
        print("Solution: Regularly monitor fish health and manage the ecosystem to support fish populations.")
        print("Explanation: Monitoring and management practices help sustain a healthy aquatic environment.")
    time.sleep(2)

def show_customer_options():
    while True:
        print("\nWelcome to ABC Algae Bloom Control!")
        print("Please select the issue you are facing:")
        print("1. Soil problem")
        print("2. Algae problem")
        print("3. Water quality issues")
        print("4. Plant health problems")
        print("5. Erosion control")
        print("6. Pest control")
        print("7. pH balance")
        print("8. Nutrient management")
        print("9. Aquatic ecosystem management")
        print("10. Sediment control")
        print("11. Invasive species management")
        print("12. Water filtration systems")
        print("13. Fish health and management")
        choice = input("Enter your choice: ").strip()
        options = {
            '1': handle_soil_problem,
            '2': handle_algae_problem,
            '3': handle_water_quality,
            '4': handle_plant_health,
            '5': handle_erosion_control,
            '6': handle_pest_control,
            '7': handle_ph_balance,
            '8': handle_nutrient_management,
            '9': handle_aquatic_ecosystem,
            '10': handle_sediment_control,
            '11': handle_invasive_species,
            '12': handle_water_filtration,
            '13': handle_fish_health
        }
        
        if choice in options:
            options[choice]()  # Call the selected function
            print("\nThank you for using ABC Algae Bloom Control!")
            
            # Ask if the user wants to address another problem
            while True:
                another_problem = input("Would you like to address another problem? (yes/no): ").strip().lower()
                if another_problem in ['yes', 'no']:
                    if another_problem == 'no':
                        print("\nThank you for approaching us. Best wishes with your problem!")
                        break
                    else:
                        break
                else:
                    print("Invalid response. Please answer with 'yes' or 'no'.")
            
            if another_problem != 'yes':
                break
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        print("Welcome to ABC Algae Bloom Control")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            register()
        elif choice == '2':
            if login():
                show_customer_options()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
