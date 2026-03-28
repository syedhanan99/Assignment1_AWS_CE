from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    return f"""
    <html>
    <head>
        <title>UniEvent</title>
        <style>
            body {{
                font-family: Arial;
                background: linear-gradient(135deg,#1e3c72,#2a5298);
                color: white;
                text-align: center;
                padding-top: 100px;
            }}

            .card {{
                background: rgba(0,0,0,0.4);
                padding: 40px;
                width: 500px;
                margin: auto;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0,0,0,0.3);
            }}

            h1 {{
                margin-bottom: 10px;
            }}

            p {{
                font-size: 18px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🎓 UniEvent App</h1>
            <p><b>Served from:</b> {hostname}</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
