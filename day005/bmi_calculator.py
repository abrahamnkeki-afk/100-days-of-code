def calculate_bmi(weight_kg, height_m):
    """Calculate BMI = weight / (height^2)."""
    return weight_kg / (height_m ** 2)

def bmi_category(bmi):
    """Return weight category based on BMI."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def health_advice(category):
    """Give simple advice based on category."""
    if category == "Underweight":
        return "Eat more nutritious meals and consult a health worker."
    elif category == "Normal weight":
        return "Great! Maintain a balanced diet and exercise."
    elif category == "Overweight":
        return "Consider more physical activity and watch your diet."
    else:
        return "Please see a health professional for guidance."


print("⚕️ BMI Calculator")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (meters): "))

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)
advice = health_advice(category)

print(f"\nYour BMI is: {bmi:.1f}")
print(f"Category: {category}")
print(f"Advice: {advice}")
