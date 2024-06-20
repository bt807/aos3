def is_within_square(lat, lon, square):
    """Check if the given coordinates are within the specified square."""
    lat_min, lat_max, lon_min, lon_max = square
    return lat_min <= lat <= lat_max and lon_min <= lon <= lon_max

def read_coordinates_from_file(filename):
    """Read coordinates from a file."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    coordinates = []
    for line in lines:
        try:
            lat, lon = map(float, line.strip().split(','))
            coordinates.append((lat, lon))
        except ValueError:
            print(f"Skipping invalid line: {line.strip()}")
    return coordinates

def filter_coordinates(coordinates, square):
    """Filter coordinates to include only those within the specified square."""
    return [coord for coord in coordinates if is_within_square(coord[0], coord[1], square)]

def main():
    filename = 'coordinates.txt'
    square = (54.847830, 54.847830, 83.094392, 83.094392)  
    
    
    coordinates = read_coordinates_from_file(filename)
    
    
    filtered_coordinates = filter_coordinates(coordinates, square)
    
    
    print("Filtered Coordinates:")
    for coord in filtered_coordinates:
        print(coord)

if __name__ == '__main__':
    main()
