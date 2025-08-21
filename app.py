from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.get("/")
def home():
    return render_template_string("""
      <h1>Mini Flask App</h1>
      <p>ลองคำนวณ BMI ด้านล่างนี้</p>
      <form method="post" action="/bmi">
        <input name="w" placeholder="น้ำหนัก (กก.)" required>
        <input name="h" placeholder="ส่วนสูง (ซม.)" required>
        <button type="submit">คำนวณ</button>
      </form>
    """)

@app.post("/bmi")
def bmi():
    try:
        w = float(request.form["w"])
        h = float(request.form["h"]) / 100.0
        bmi = w / (h*h)
        return render_template_string("<h2>BMI = {{bmi:.2f}}</h2><a href='/'>กลับ</a>", bmi=bmi)
    except Exception as e:
        return f"Error: {e}", 400
