from flask import Flask, render_template, request

app = Flask(__name__)

def get_response(user_input):
    user_input = user_input.lower()

    # ROOM DETAILS
    if "single room" in user_input:
        return "Single Room: ₹1500 per night | 1 Bed | Free WiFi"

    elif "double room" in user_input:
        return "Double Room: ₹2500 per night | 2 Beds | Free WiFi + TV"

    elif "deluxe room" in user_input:
        return "Deluxe Room: ₹4000 per night | AC | Breakfast Included"

    elif "rooms available" in user_input or "room availability" in user_input:
        return "Yes, Single, Double, and Deluxe rooms are available."

    # PRICE QUERIES
    elif "price" in user_input or "cost" in user_input or "rate" in user_input:
        return (
            "Room Prices:\n"
            "• Single Room – ₹1500\n"
            "• Double Room – ₹2500\n"
            "• Deluxe Room – ₹4000"
        )

    # FACILITIES
    elif "facilities" in user_input or "amenities" in user_input:
        return (
            "Our Facilities:\n"
            "• Free WiFi\n"
            "• AC Rooms\n"
            "• Restaurant\n"
            "• Parking\n"
            "• 24/7 Room Service"
        )

    # CHECK-IN / CHECK-OUT
    elif "check in" in user_input:
        return "Check-in time is 12:00 PM."

    elif "check out" in user_input:
        return "Check-out time is 11:00 AM."

    # LOCATION
    elif "location" in user_input or "address" in user_input:
        return "We are located in Hyderabad, near HITEC City."

    # CONTACT
    elif "contact" in user_input or "phone" in user_input:
        return "You can contact us at 📞 9876543210."

    # FOOD
    elif "food" in user_input or "restaurant" in user_input:
        return "Yes, we have an in-house restaurant serving Veg & Non-Veg food."

    # BOOKING
    elif "booking" in user_input or "book room" in user_input:
        return "For booking, please call 9876543210 or visit our reception."

    # GREETINGS
    elif "hello" in user_input or "hi" in user_input:
        return "Hello 👋 Welcome to our Hotel! How can I help you?"

    else:
        return "Sorry, I didn’t understand. Please ask about rooms, price, facilities, or booking."

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["message"]
        response = get_response(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

