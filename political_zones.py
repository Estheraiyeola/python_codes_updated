"""Returns the Geopolitical zone of a state"""
geopolitical_zone = {
    "NORTH_CENTRAL": ["Benue", "FCT", "Kogi", "Kwara", "Nasarawa", "Niger", "Plateau"],
    "NORTH_EAST": ["Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe"],
    "NORTH_WEST": ["Kaduna", "Kastina", "Kano", "Kebbi", "Sokoto", "Jigawa", "Zamfara"],
    "SOUTH_EAST": ["Abia", "Anambra", "Ebonyi", "Enungu", "Imo"],
    "SOUTH_SOUTH": ["Akwa-Ibom", "Bayelsa", "Cross-River", "Delta", "Edo", "Rivers"],
    "SOUTH_WEST": ["Ekiti", "Lagos", "Osun", "Ondo", "Ogun", "Oyo"]
}


def get_political_zone(required_state):
    global geopolitical_zone
    for key in geopolitical_zone.keys():
        for pair in geopolitical_zone[key]:
            if pair == required_state:
                return key


def collect_state():
    state = input("Enter the state you're looking for: ")
    return state


def function_to_get_political_zone():
    required_state = collect_state()
    return get_political_zone(required_state)


print(function_to_get_political_zone())
