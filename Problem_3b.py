def read_weather_data(filename):
    try:
        with open(filename, 'r') as file:
            weather_data = []
            for line in file:
                date, temp = line.strip().split(',')
                weather_data.append({'date': date, 'temperature': float(temp)})
            return weather_data
    
    except FileNotFoundError:
        return []
        

def calculate_average_temperature(weather_data):
    total_temp = sum(item['temperature'] for item in weather_data)
    avg_temp = total_temp / len(weather_data)
    return avg_temp



def main():
    weather_data1 = read_weather_data('weather_2020.txt')
    weather_data2 = read_weather_data('weather_2022.txt')
    if not weather_data1 or not weather_data2:
        print("No weather data available.")
        return
    
    while True:
        print("\n1. Calculate Average Temperature\n2. Quit")
        choice = input("Enter your choice ")

        if choice == '1':
            avg_temp1 = calculate_average_temperature(weather_data1)
            print(f"\nAverage Temperature for the year 2020: {avg_temp1:.2f}°C")
            avg_temp2 = calculate_average_temperature(weather_data2)
            print(f"Average Temperature for the year 2022: {avg_temp2:.2f}°C")
            if avg_temp1 > avg_temp2:
                print(f"\nThe year 2020 had the highest average temp which was {avg_temp1}°C")
            elif avg_temp2 > avg_temp1:
                print(f"\nThe year 2022 had the highest average temp which was {avg_temp2}°C")


        elif choice == '2':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()