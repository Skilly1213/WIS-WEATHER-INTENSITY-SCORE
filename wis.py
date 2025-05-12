def calculate_weather_intensity(wind_speed, precipitation, temperature):
    # Assign weights to different weather factors
    wind_factor = wind_speed * 0.4
    precipitation_factor = precipitation * 0.10
    temperature_factor = abs(temperature - 105) * 0.3  # Deviation from 70°F

    # Calculate total intensity score
    intensity_score = wind_factor + precipitation_factor + temperature_factor
    return round(intensity_score, 7)

# Example usage
wind_speed = 97 # mph
precipitation = 18  # inches
temperature = 85  # °F

score = calculate_weather_intensity(wind_speed, precipitation, temperature)
print(f"Weather Intensity Score: {score}")