dash = 85 * "-"


def started(msg=""):
    print(dash)
    print(f"Operations started: {msg}")


def completed():
    print("\n")
    print("Operations Completed")
    print(dash)


def error(msg=""):
    print(f"Error! {msg}")


def menu():
    print(
    """
    Please Select an option:
    
    [years]    List unique years"
    [tally]    Tally up medals"
    [ctally]   Tally up medals for each team"
    [exit]     Exit the program
    
    Your Selection:
    
    """)

    selection = str(input())
    return selection


def display_medal_tally(tally):
    print(f"| {'Gold':<10} | {tally['Gold']:<10} |")
    print(f"| {'Silver':<10} | {tally['Silver']:<10} |")
    print(f"| {'Bronze':<10} | {tally['Bronze']:<10} |")


def display_team_medal_tally(team_tally):
    for team, tally in team_tally:
        print(team)
        print(f"Gold: {tally['Gold']}, Silver: {tally['Silver']}, Bronze: {tally['Bronze']}")


def display_year(years):
    sorted_years = sorted(years, reverse=True)
    for years in sorted_years:
        print (years)
