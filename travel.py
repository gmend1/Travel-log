"""Code for my project."""
import random


"""
Travel Log

A simple program that allows users to record travel experiences,
including state, city, rating, and written reflections.
"""


def normalize_state(state_input, state_map):
    """
    Convert user input into a standardized state name.

    Parameters
    ----------
    state_input : str
        User-provided state name or abbreviation.
    state_map : dict
        Dictionary mapping abbreviations/aliases to full state names.

    Returns
    -------
    str
        Standardized state name.
    """
    # It will take away extra spaces and lowercases everything
    state_input = state_input.strip().lower()

   # If you use a known nickname for the state it will change to full name
    if state_input in state_map:
        return state_map[state_input]

    # Otherwise it will format to title
    return state_input.title()


def get_rating():
    """
    Prompt user for a rating between 1 and 10.

    Parameters
    ----------
    None

    Returns
    -------
    float
        Valid rating entered by the user.
    """
    while True:
        try:
            # Used float instead of integers to allow decimals
            rating = float(input("Rating (1 - 10): "))

            # Doesn't allow user to go below 1 or over 10
            if 1 <= rating <= 10:
                return rating

            print("Rating must be between 1 and 10.")

        except ValueError:
            print("Enter a number.")


def get_state(state_map):
    """
    Prompt user for a state and normalize it.

    Parameters
    ----------
    state_map : dict
        Mapping of state abbreviations to full names.

    Returns
    -------
    str
        Standardized state name.
    """
    state_input = input("State: ")
    return normalize_state(state_input, state_map)


def display_travel_log(travel):
    """
    Display all travel entries in a readable format.

    Parameters
    ----------
    travel : list of dict
        List of travel entries.
    """
    print("")
    print("Travel Log:")
    print("-" * 15)

    # Loop through each trip and display details
    for trip in travel:
        print("State:", trip["state"])
        print("City:", trip["city"])
        print("Rating:", trip["rating"])
        print("Experience:", trip["experience"])
        print("<->" * 10)


def calculate_average_rating(travel):
    """
    Compute the average rating from all trips.

    Parameters
    ----------
    travel : list of dict
        List of travel entries, each potentially containing a rating.

    Returns
    -------
    float
        Average rating of all non-None values.
        Returns 0 if no valid ratings exist.
    """
    ratings = []

    # Collect only valid ratings
    for trip in travel:
        rating = trip["rating"]

        if rating is not None:
            ratings.append(rating)

    # Handle case where no ratings exist
    if not ratings:
        return 0

    return sum(ratings) / len(ratings)


def add_trip(travel, state_map):
    """
    Add a new travel entry based on user input.

    Parameters
    ----------
    travel : list of dict
        The travel log being updated.
    state_map : dict
        Mapping of state abbreviations to full names.
    """
    state = get_state(state_map)
    city = input("City: ").strip().title()
    rating = get_rating()
    experience = input("Experience: ")

    # Store trip as dictionary
    travel.append({
        "state": state,
        "city": city,
        "rating": rating,
        "experience": experience
    })


def main():
    """
    Run the main program loop.

    Initializes travel log, collects user input,
    and displays final results.
    """
    travel = [
        {
            "state": "California",
            "city": "San Diego",
            "rating": None,
            "experience": None
        }
    ]

    state_map = {
        "ca": "California",
        "california": "California",
        "ny": "New York",
        "new york": "New York",
        "tx": "Texas",
        "texas": "Texas"
    }

    print("Current Destination: San Diego, California")

    # Prompt user for initial San Diego entry
    for trip in travel:
        if trip["city"] == "San Diego":
            trip["rating"] = get_rating()
            trip["experience"] = input("Your experience in San Diego: ")

    # Allow user to add more trips
    while True:
        print("")
        add = input("Do you want to add a new city? (y/n): ").lower()

        if add != "y":
            break

        add_trip(travel, state_map)

    # Display results
    display_travel_log(travel)

    print("")
    print("Average rating:", calculate_average_rating(travel))


# List of all U.S. states
states = [
    "Alabama", "Alaska", "Arizona", "Arkansas",
    "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]


def travel_random():
    """
    Print a randomly selected U.S. state as a travel suggestion.
    """
    state = random.choice(states)

    print("")
    print("Ready for an Adventure?")
    print("-" * 23)
    print("Your next destination is: " + state + "!")


if __name__ == "__main__":
    main()
    travel_random()