from flask import Flask, request, render_template_string

app = Flask(__name__)

base_styles = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    body {
        margin: 0;
        padding: 0;
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .card {
        background: #fff;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
        max-width: 400px;
        width: 100%;
    }
    h1 {
        margin-bottom: 20px;
        color: #333;
    }
    input[type=number] {
        width: 100%;
        padding: 12px;
        margin: 12px 0;
        border-radius: 8px;
        border: 1px solid #ccc;
        font-size: 16px;
    }
    input[type=submit] {
        width: 100%;
        padding: 12px;
        background-color: #007BFF;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    input[type=submit]:hover {
        background-color: #0056b3;
    }
    .result {
        margin-top: 20px;
        background: #e8f5e9;
        padding: 20px;
        border-radius: 10px;
        color: #2e7d32;
    }
    a {
        display: inline-block;
        margin-top: 15px;
        color: #007BFF;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
</style>
"""


math_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Math Calculator</title>
    """    + base_styles + """
</head>
<body>
    <div class="card">
        <h1>🔢 Square & Cube Calculator</h1>
        <form method="GET">
            <input type="number" name="number" step="any" placeholder="Enter a number" required>
            <input type="submit" value="Calculate">
        </form>

        {% if result %}
        <div class="result">
            <p><strong>Number:</strong> {{ result.number }}</p>
            <p><strong>Square:</strong> {{ result.square }}</p>
            <p><strong>Cube:</strong> {{ result.cube }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""


@app.route('/', methods=['GET'])
def calculate():
    number = request.args.get('number')
    result = None
    if number:
        try:
            num = float(number)
            result = {
                'number': num,
                'square': round(num ** 2, 2),
                'cube': round(num ** 3, 2)
            }
        except ValueError:
            result = {'error': 'Invalid number'}
    return render_template_string(math_html, result=result)

if __name__ == '__main__':
    app.run(debug=True)
