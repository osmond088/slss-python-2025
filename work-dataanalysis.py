# NYC Weather Data Analysis
# Author: Osmond


def main():
    # Get the file
    path = "data/NYC_Central_Park_weather_1869-2022.csv"
    file = open(path)

    # Print the first line of the file (header)
    header_row = file.readline()

    # Initialize counters and totals
    count = 0
    total_precipitation = 0
    total_temp_min = 0
    june_temp_max_total = 0
    june_count = 0

    # Process each line in the file
    for line in file:
        # A line is a string
        # Convert the string to a list
        # Split the line wherever a , is
        info = line.split(",")

        # Extract data from columns
        # Columns: date, precipitation, snow, snow_depth, temp_min, temp_max
        date = info[0]

        # Skip lines with missing data
        if info[1] == "" or info[4] == "" or info[5] == "":
            continue

        precipitation = float(info[1])
        temp_min = float(info[4])
        temp_max = float(info[5])

        # Count data points
        count += 1

        # Add to totals
        total_precipitation += precipitation
        total_temp_min += temp_min

        # Check if date is in June
        # Date format is YYYY-MM-DD
        # Split by - and get the month part
        date_parts = date.split("-")
        month = date_parts[1]

        if month == "06":
            june_temp_max_total += temp_max
            june_count += 1

    # Calculate averages
    avg_precipitation = total_precipitation / count
    avg_temp_min_f = total_temp_min / count

    # Convert minimum temperature to Celsius
    # Formula: (F - 32) * 5/9
    avg_temp_min_c = (avg_temp_min_f - 32) * 5 / 9

    # Calculate June average max temperature
    avg_temp_max_june = june_temp_max_total / june_count

    # Display Results
    print(f"Total data points: {count}")
    print(f"Average rainfall: {avg_precipitation} inches")
    print(f"Average minimum temperature: {avg_temp_min_c} degrees Celsius")
    print(
        f"Average maximum temperature in June: {avg_temp_max_june} degrees Fahrenheit"
    )

    # Close the file
    file.close()


if __name__ == "__main__":
    main()
