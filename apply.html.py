```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apply for Loan</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            margin: 0;
        }

        header {
            background: #173b7a;
            color: white;
            text-align: center;
            padding: 20px;
        }

        .container {
            max-width: 550px;
            margin: 30px auto;
            padding: 30px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }

        h2 {
            text-align: center;
            color: #173b7a;
        }

        label {
            display: block;
            margin-top: 15px;
            font-weight: bold;
        }

        input, select {
            width: 100%;
            padding: 12px;
            margin-top: 7px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
        }

        button {
            width: 100%;
            padding: 13px;
            margin-top: 25px;
            background: #173b7a;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background: #2856a0;
        }

        .back {
            display: block;
            text-align: center;
            margin-top: 20px;
            color: #173b7a;
            text-decoration: none;
        }
    </style>
</head>

<body>

<header>
    <h1>Loan Application Credit Scoring</h1>
</header>

<div class="container">

    <h2>Loan Application Form</h2>

    <form action="{{ url_for('apply') }}" method="POST">

        <label>Full Name</label>
        <input type="text" name="name" placeholder="Enter your name" required>

        <label>Account Number</label>
        <input type="text" name="account_number"
               placeholder="Enter your account number" required>

        <label>Phone Number</label>
        <input type="tel" name="phone"
               placeholder="Enter your phone number"
               pattern="[0-9]{10}" maxlength="10" required>

        <label>Loan Amount (₹)</label>
        <input type="number" name="amount"
               placeholder="Enter loan amount" min="1" required>

        <label>Monthly Income (₹)</label>
        <input type="number" name="income"
               placeholder="Enter monthly income" min="1" required>

        <label>Credit History</label>
        <select name="credit_history" required>
            <option value="">Select Credit History</option>
            <option value="Good">Good</option>
            <option value="Average">Average</option>
            <option value="Poor">Poor</option>
        </select>

        <button type="submit">Submit Application</button>

    </form>

    <a href="{{ url_for('dashboard') }}" class="back">
        Back to Home
    </a>

</div>

</body>
</html>
```