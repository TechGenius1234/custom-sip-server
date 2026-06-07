from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)
db_instance = None

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>SIP Server Admin</title>
    <style>
        body { font-family: sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .form-group { margin-bottom: 10px; }
    </style>
</head>
<body>
    <h1>SIP Server Administration</h1>
    <h2>Users</h2>
    <table>
        <tr><th>Extension</th><th>Name</th><th>Password</th></tr>
        {% for user in users %}
        <tr><td>{{ user.extension }}</td><td>{{ user.name }}</td><td>{{ user.password }}</td></tr>
        {% endfor %}
    </table>
    
    <h2>Add User</h2>
    <form action="/add_user" method="post">
        <div class="form-group">
            <label>Extension:</label><input type="text" name="extension">
        </div>
        <div class="form-group">
            <label>Name:</label><input type="text" name="name">
        </div>
        <div class="form-group">
            <label>Password:</label><input type="password" name="password">
        </div>
        <button type="submit">Add User</button>
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, users=db_instance.data['users'])

@app.route('/add_user', methods=['POST'])
def add_user():
    ext = request.form.get('extension')
    name = request.form.get('name')
    pwd = request.form.get('password')
    if ext and name and pwd:
        db_instance.add_user(ext, pwd, name)
    return "User added! <a href='/'>Go back</a>"

def run_web_admin(db, port=8080):
    global db_instance
    db_instance = db
    app.run(host='0.0.0.0', port=port)
