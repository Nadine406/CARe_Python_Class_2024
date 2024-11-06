#YOUR CODE FOR EX_1 INTERMEDIATE HERE
#Define the initial dictionary with microbial species and their sample counts
species_dict = {"Bacteria": 20,"Archaea": 15,"Fungi": 10}

#Calculate the total number of samples collected across all species
total_samples = sum(species_dict.values())
print(f"Total number of samples collected: {total_samples}")

#Use a list comprehension to find species with sample counts greater than 15
species_above_15 = [species for species, count in species_dict.items() if count > 15]
print(f"Species with more than 15 samples: {species_above_15}")


#Define a function to add a new species or increase the count if it already exists
def add_species(species_dict, new_species, sample_count):
    if new_species in species_dict:
        species_dict[new_species] += sample_count  # Increment count if species exists
    else:
        species_dict[new_species] = sample_count  # Add new species with the specified count


#Use a while loop to continuously prompt the user for new species to add
while True:
    new_species = input("Enter a new species name to add (or type 'stop' to end): ")
    if new_species.lower() == 'stop':
        break  # Exit the loop if the user types 'stop'

    # Get the number of samples collected for the new species
    while True:
        try:
            sample_count = int(input(f"Enter the number of samples collected for {new_species}: "))
            if sample_count < 0:
                print("Sample count cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer for the sample count.")

    # Call the function to add or update the species with the provided sample count
    add_species(species_dict, new_species, sample_count)

#Print the final dictionary after all user inputs
print("Final species dictionary with updated sample counts:")
print(species_dict)
