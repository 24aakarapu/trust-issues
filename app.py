from flask import Flask, request, make_response

app = Flask(__name__)

FLAG = "flag{client_side_trust_is_dangerous}"

@app.route("/")
def home():
    return """
    <style>
        body {
            background-color: #ffe6f2;
            font-family: Arial, sans-serif;
        }
    </style>

    <h2>Trust Issues 💔</h2>
    <p>This site keeps track of relationship status using cookies.</p>
    <p>Start here: <a href="/login">/login</a></p>
    <p>Then try accessing: <a href="/vault">/vault</a></p>
    """

@app.route("/login")
def login():
    resp = make_response("""
        <style>
            body {
                background-color: #ffe6f2;
                font-family: Arial, sans-serif;
            }
        </style>

        <h3>Status Saved</h3>
        <p>Your relationship status has been set.</p>
        <p>Try visiting the <a href="/vault">vault</a>.</p>
    """)
    # storing trust on the client is probably a bad idea
    resp.set_cookie("status", "basic")
    return resp

@app.route("/vault")
def vault():
    user_status = request.cookies.get("status", "basic")

    if user_status == "verified":
        return f"""
        <style>
            body {{
                background-color: #ffe6f2;
                font-family: Arial, sans-serif;
            }}
        </style>

        <h3>Secret Vault ❤️‍🔥</h3>
        <p>This account is marked as trusted.</p>
        <p><b>{FLAG}</b></p>
        """

    return """
        <style>
            body {
                background-color: #ffe6f2;
                font-family: Arial, sans-serif;
            }
        </style>

        <h3>Access Denied</h3>
        <p>You’re not trusted enough to view this page.</p>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5001)


