import numpy as np

from plot import calculate_3d_plot, calculate_2d_plot


def main():
    phi = np.linspace(0, 2 * np.pi, 100)

    # User selection for 2d current plot or 3d magnetic field plot
    print("Please select an option:\n")
    print("\t1. Calculate 2d current plot")
    print("\t2. Calculate 3d magnetic field plot")
    print("\t3. Both")
    print("\t4. None")

    # Get user input
    selection = input("\nEnter the number of your selection: ")

    # Convert user input to integer
    selection = int(selection)

    if selection == 1:
        print("You selected Option A")
        calculate_2d_plot(phi)
    elif selection == 2:
        print("You selected Option B")
        calculate_3d_plot(phi)
    elif selection == 3:
        print("You selected Option C")
        calculate_2d_plot(phi)
        calculate_3d_plot(phi)
    elif selection == 4:
        print("You selected Option D")
        print("Exiting program")
        exit()
    else:
        print("Invalid selection. Please try again.")


if __name__ == '__main__':
    main()
