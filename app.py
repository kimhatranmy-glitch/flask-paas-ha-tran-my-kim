import os # Đặt ở dòng đầu tiên
from flask import Flask
import datetime, platform

app = Flask(__name__)

visit_count = 0 # Biến đếm lưu trong RAM của container

@app.route("/")
def home():
    return f"<h1>Ung dung Flask tren PaaS - phien ban 2!</h1>"

@app.route("/api/counter")
def counter():
    global visit_count
    visit_count += 1
    return {
        "so_lan_truy_cap": visit_count,
        "ghi_chu": "So nay se MAT khi container khoi dong lai!"
    }

@app.route("/api/info")
def info():
    ten_sinh_vien = os.environ.get("STUDENT_NAME", "Chua dat bien moi truong")
    return {
        "sinh_vien": ten_sinh_vien,
        "nguon_du_lieu": "Environment Variable tren Render, KHONG hardcode trong code"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)