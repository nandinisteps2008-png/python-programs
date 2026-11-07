def calculate_score(income, loan_amount, credit_history):

    score = 500

    # Income
    if income >= 50000:
        score += 150
    elif income >= 30000:
        score += 100

    # Loan amount
    if loan_amount <= 500000:
        score += 100
    else:
        score += 50

    # Credit history
    if credit_history == "Good":
        score += 150
    elif credit_history == "Average":
        score += 100

    # Final status
    if score >= 700:
        status = "Approved"
    else:
        status = "Needs Review"

    return score, status