from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def analyze_password(password):
    score = 0
    feedback = []

    # 1. Length Check
    if len(password) >= 8:
        score += 20
    else:
        feedback.append("Increase length to at least 8 characters.")

    # 2. Lowercase Check
    if re.search(r"[a-z]", password):
        score += 20
    else:
        feedback.append("Add lowercase letters.")

    # 3. Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 20
    else:
        feedback.append("Add uppercase letters.")

    # 4. Number Check
    if re.search(r"\d", password):
        score += 20
    else:
        feedback.append("Include at least one number.")

    # 5. Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>+=\-_]", password):
        score += 20
    else:
        feedback.append("Include a special character (e.g., @, #, $).")

    # Determine Label
    if score <= 40:
        label = "Weak"
    elif score <= 60:
        label = "Medium"
    elif score <= 80:
        label = "Strong"
    else:
        label = "Very Strong"

    # Professional explanation
    if score == 100:
        explanation = "Excellent! Your password follows security best practices."
    else:
        explanation = " ".join(feedback)

    return score, label, explanation

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-strength', methods=['POST'])
def check_strength():
    data = request.json
    password = data.get("password", "")
    
    if not password:
        return jsonify({"error": "Password is empty"}), 400

    score, label, explanation = analyze_password(password)
    
    return jsonify({
        "percentage": score,
        "label": label,
        "explanation": explanation
    })

if __name__ == '__main__':
    app.run(debug=True)