<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Applications - LoanEase</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f7fc;
            padding: 25px;
        }

        h1 {
            color: #12345a;
        }

        .table-container {
            overflow-x: auto;
        }

        table {
            width: 100%;
            background: white;
            border-collapse: collapse;
        }

        th, td {
            padding: 14px;
            border: 1px solid #ddd;
            text-align: left;
        }

        th {
            background: #12345a;
            color: white;
        }

        a {
            display: inline-block;
            margin-top: 20px;
            color: #087f8c;
        }
    </style>
</head>

<body>

<h1>My Loan Applications</h1>

<div class="table-container">
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Loan Amount</th>
                <th>Monthly Income</th>
                <th>Purpose</th>
                <th>Status</th>
            </tr>
        </thead>

        <tbody>
            {% for item in applications %}
            <tr>
                <td>{{ item['id'] }}</td>
                <td>{{ item['name'] }}</td>
                <td>₹{{ "%.2f"|format(item['amount']) }}</td>
                <td>₹{{ "%.2f"|format(item['income']) }}</td>
                <td>{{ item['purpose'] }}</td>
                <td>{{ item['status'] }}</td>
            </tr>
            {% else %}
            <tr>
                <td colspan="6">No applications found.</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>

<a href="{{ url_for('dashboard') }}">Back to Dashboard</a>

</body>
</html>