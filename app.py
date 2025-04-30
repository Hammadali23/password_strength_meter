import streamlit as st

def check_password(password):             
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("🔐 Password must be at least 8 characters long.")   

    if any(c.isupper() for c in password):
        score += 1 
    else:
        tips.append("🔠 Include at least one uppercase letter.")   

    if any(c.islower() for c in password):
        score += 1  
    else:
        tips.append("🔡 Include at least one lowercase letter.")   

    if any(c.isdigit() for c in password):  # corrected here
        score += 1
    else: 
        tips.append("🔢 Add at least one number (0-9).")  

    if any(c in "!@#$%^&*" for c in password):
        score += 1
    else: 
        tips.append("❗ Use a special character (!@#$%^&*).")    

    return score, tips 

def main():
    st.title("🔐 Password Strength Meter")  # corrected title
    password = st.text_input("Enter Password", type="password")

    if password:
        score, tips = check_password(password)

        if score == 5:
            st.success("✅ Strong password! Secure and safe.")
        elif score >= 3:
            st.warning("⚠️ Moderate password. You can improve it:")
        else:
            st.error("❌ Weak password! Follow these tips:")

        for tip in tips:
            st.write("- " + tip)

main()
