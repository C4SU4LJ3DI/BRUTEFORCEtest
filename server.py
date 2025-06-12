from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    html = '''
    <form method="post">
      <input type="text" name="login" placeholder="Login">
      <input type="password" name="pass" placeholder="Hasło" minlength="5" maxlength="8">
      <input type="submit" value="Zaloguj">
    </form>
    {% if request.method == "POST" and request.form.get("login") == "Admin" and request.form.get("pass") == "test123" %}
    <p>Wyloguj</p>
    {% elif request.method == "POST" %}
    <p>Błąd logowania</p>
    {% endif %}
    '''
    return render_template_string(html)

if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")  # host=0.0.0.0 ważne w Codespaces!