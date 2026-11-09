# PalmerPenguinsM10.py
# Devin Dollard
# 11/18/2026
# Analyze Palmer Penguin observations using exception handling

import math

import penguin as penguin_

# Constants for the penguin species
SP_CHINSTRAP = "Chinstrap"
SP_GENTOO = "Gentoo"
SP_ADELIE = "Adelie"

NUM_CHINSTRAP = 68
NUM_GENTOO = 123
NUM_ADELIE = 151


def calculate_percentage(count, total):
    return count / total * 100


def classify_species(percent):
    if percent < 25:
        return "small"
    elif percent < 40:
        return "medium"
    else:
        return "large"


def get_position_description(selected_species, largest_species, smallest_species):
    if selected_species == largest_species:
        return "largest"
    elif selected_species == smallest_species:
        return "smallest"
    else:
        return "middle-sized"


def display_species_statistics(names, counts, percentages):
    for index, species in enumerate(names):
        print(f"{species}: {counts[index]} ({percentages[index]:.2f}%)")


def read_penguin_row(row_number):
    penguin_row = ""

    try:
        # open the CSV file and skip the header row
        with open("PalmerPenguins.csv", "r") as penguin_file:
            penguin_file.readline()

            current_row = 1

            # search for the requested data row
            for row in penguin_file:
                if current_row == row_number:
                    penguin_row = row.strip()
                    break

                current_row += 1
    except FileNotFoundError:
        print("Error: PalmerPenguins.csv was not found.")

    if penguin_row == "":
        raise ValueError(f"Penguin observation {row_number} "
                         f"could not be retrieved.")

    # return the requested row as a string
    return penguin_row


# Create a Function to Display the Penguin Observation
def display_penguin_observation(sample_num, sp, bill_len, bill_dep, body_m, gender):
    print("\nSample Penguin Observation")
    print(f"{'Sample Number:':<15} {sample_num}")
    print(f"{'Species:':<15} {sp}")
    print(f"{'Bill length:':<15} {bill_len:.1f} mm")
    print(f"{'Bill depth:':<15} {bill_dep:.1f} mm")
    print(f"{'Body mass:':<15} {body_m} g")
    print(f"{'Sex:':<15} {gender}")


def process_penguin_row(row_number):
    try:
        penguin_row = read_penguin_row(row_number)
        print("\nSample dataset row:")
        print(penguin_row)

        penguin_data = penguin_row.split(",")
        print(penguin_data)

        sample_number = int(penguin_data[0])
        species = penguin_data[1]
        bill_length = float(penguin_data[2])
        bill_depth = float(penguin_data[3])
        flipper_length = int(penguin_data[4])
        body_mass = int(penguin_data[5])
        sex = penguin_data[6]

        display_penguin_observation(
            sample_number, species, bill_length, bill_depth, body_mass, sex)
    except ValueError as excpt:
        print(f"Error: {excpt}")
    except IndexError:
        print("Error: The penguin observation is incomplete.")


def main():
    species_names = [
        SP_CHINSTRAP,
        SP_GENTOO,
        SP_ADELIE,
    ]

    species_counts = [
        NUM_CHINSTRAP,
        NUM_GENTOO,
        NUM_ADELIE,
    ]

    # Calculations
    total_species = len(species_names)
    total_penguins = sum(species_counts)
    average_penguins = total_penguins / total_species
    average_penguins_rounded_up = math.ceil(average_penguins)

    chinstrap_percent = calculate_percentage(species_counts[0], total_penguins)
    gentoo_percent = calculate_percentage(species_counts[1], total_penguins)
    adelie_percent = calculate_percentage(species_counts[2], total_penguins)

    species_percentages = [
        chinstrap_percent,
        gentoo_percent,
        adelie_percent,
    ]

    largest_count = max(species_counts)
    largest_index = species_counts.index(largest_count)
    largest_species = species_names[largest_index]
    smallest_count = min(species_counts)
    smallest_index = species_counts.index(smallest_count)
    smallest_species = species_names[smallest_index]

    # Print the formatted output
    print("Introducing the Palmer Penguins:")
    print(f"\t{SP_CHINSTRAP}!")
    print(f"\t{SP_GENTOO}!")
    print("and last but not least...")
    print(f"\t{SP_ADELIE}!")
    print(
        f"There are a total of {total_species} "
        "penguin species in this dataset."
    )

    print(f"There are a total of {total_penguins} penguins in the dataset.")
    print(
        f"The average number of penguins per species is "
        f"{average_penguins:.1f}."
    )
    print(f"The average rounded up is {average_penguins_rounded_up}.")

    display_species_statistics(
        species_names, species_counts, species_percentages)

    print(
        f"The species with the most observations is {largest_species} "
        f"with {largest_count} penguins."
    )
    print(
        f"The species with the fewest observations is {smallest_species} "
        f"with {smallest_count} penguins."
    )

    # Process a Penguin Record
    process_penguin_row(1)

    # Process Another Observation
    process_penguin_row(153)

    print("\nException Handling Demonstration")
    process_penguin_row(999)

    # Create a List of Penguin Row Numbers
    sample_rows = [1, 2, 3, 4, 5]

    # Create a List to Store Body Masses
    body_masses = []

    # Iterate through the first five rows and collect body masses
    for row_number in sample_rows:
        penguin_row = read_penguin_row(row_number)
        penguin_data = penguin_row.split(",")
        body_mass = int(penguin_data[5])
        body_masses.append(body_mass)

    print("\nSample Body Masses")
    print(body_masses)

    # Calculate and display body mass summary statistics
    observation_count = len(body_masses)
    total_body_mass = sum(body_masses)
    smallest_body_mass = min(body_masses)
    largest_body_mass = max(body_masses)
    average_body_mass = total_body_mass / observation_count

    print("\nBody Mass Summary")
    print(f"Observations: {observation_count}")
    print(f"Total body mass: {total_body_mass} g")
    print(f"Smallest body mass: {smallest_body_mass} g")
    print(f"Largest body mass: {largest_body_mass} g")
    print(f"Average body mass: {average_body_mass:.2f} g")

    # Create and display species counts using a dictionary
    species_dictionary = {
        SP_CHINSTRAP: NUM_CHINSTRAP,
        SP_GENTOO: NUM_GENTOO,
        SP_ADELIE: NUM_ADELIE,
    }

    print("\nSpecies Counts Using a Dictionary")
    for species in species_dictionary:
        count = species_dictionary[species]
        print(f"{species}: {count}")

    # Create and display a Penguin object from the first CSV observation
    penguin_row = read_penguin_row(1)
    penguin_data = penguin_row.split(",")
    sample_number = int(penguin_data[0])
    species = penguin_data[1]
    body_mass = int(penguin_data[5])

    sample_penguin = penguin_.Penguin(
        sample_number,
        species,
        body_mass,
    )
    print("\nPenguin Object Demonstration")
    sample_penguin.display_info()

    # Create a list of Penguin objects for the sample rows
    penguin_objects = []
    for row_number in sample_rows:
        penguin_row = read_penguin_row(row_number)
        penguin_data = penguin_row.split(",")
        sample_number = int(penguin_data[0])
        species = penguin_data[1]
        body_mass = int(penguin_data[5])
        penguin = penguin_.Penguin(sample_number, species, body_mass)
        penguin_objects.append(penguin)

    print("\nPenguin Objects")
    for penguin in penguin_objects:
        penguin.display_info()

    # Calculate average body mass using Penguin object attributes
    total_object_mass = 0
    for penguin in penguin_objects:
        total_object_mass += penguin.body_mass
    average_object_mass = total_object_mass / len(penguin_objects)

    print("\nObject-Based Body Mass Summary")
    print(f"Observations: {len(penguin_objects)}")
    print(f"Total body mass: {total_object_mass} g")
    print(f"Average body mass: {average_object_mass:.2f} g")

    # Add a counter for valid species selections
    valid_selections = 0

    # Ask user for species
    print("\nExplore the Palmer Penguins")
    species_choice = input(
        "Enter Chinstrap, Gentoo, Adelie, Sample, or Done. ")

    while species_choice != "Done":
        if species_choice == "Sample":
            try:
                sample_number = int(input("Enter a sample number: "))
                process_penguin_row(sample_number)
            except ValueError:
                print("Error: Please enter a valid integer sample number.")
            finally:
                print("Sample request completed.")
        elif species_choice not in species_names:
            print("That is not a valid species.")
        else:
            valid_selections += 1

            if species_choice == species_names[0]:
                selected_index = 0
            elif species_choice == species_names[1]:
                selected_index = 1
            else:
                selected_index = 2

            # Retrieve the Selected Species Data
            selected_species = species_names[selected_index]
            selected_count = species_counts[selected_index]
            selected_percent = species_percentages[selected_index]

            # Classify the Species by Its Percentage
            size_category = classify_species(selected_percent)

            # Determine the Species' Relative Position
            position_description = get_position_description(
                selected_species, largest_species, smallest_species)

            # Compare the Selected Count to the Average
            average_position = (
                "above" if selected_count > average_penguins else "below"
            )

            # Display the Selected Species Statistics
            print(
                f"\nSpecies: {selected_species}"
            )
            print(f"Count: {selected_count}")
            print(f"Percentage: {selected_percent:.2f}%")
            print(f"This species represents a {size_category} portion of the dataset.")
            print(
                f"It is the {position_description} species in the dataset."
            )
            print(
                f"Its count is {average_position} the average."
            )

        species_choice = input(
            "\nEnter Chinstrap, Gentoo, Adelie, Sample, or Done. ")

    print(f"You explored {valid_selections} valid penguin species.")


if __name__ == "__main__":
    main()
