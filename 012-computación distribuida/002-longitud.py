import os

def cut_file(filename, num_slices):
    # Get the size of the file
    file_size = os.path.getsize(filename)

    # Calculate the size of each slice
    slice_size = file_size // num_slices

    with open(filename, 'rb') as file:
        for i in range(num_slices):
            # Read the slice from the file
            data = file.read(slice_size)

            # Create a new file for the slice
            slice_filename = f"{filename}.slice{i+1}"
            with open(slice_filename, 'wb') as slice_file:
                slice_file.write(data)

            print(f"Slice {i+1} created: {slice_filename}")

    print("File slicing complete.")

# Example usage
file_path = 'registros.csv'
num_slices = 5
cut_file(file_path, num_slices)
