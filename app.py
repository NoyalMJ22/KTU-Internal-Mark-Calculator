from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

def convert_to_scale(mark, out_of, scale):
    return (mark / out_of) * scale

def get_attendance_marks(attendance_percent):
    if attendance_percent >= 90:
        return 10.0
    elif attendance_percent >= 0:
        return round(attendance_percent / 10, 1)
    else:
        return 0

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        data = request.json

        name = data["name"]
        t1 = float(data["test1"])
        t1_total = float(data["test1_total"])
        t2 = float(data["test2"])
        t2_total = float(data["test2_total"])
        assign1 = float(data["assignment1"])
        assign1_total = float(data["assignment1_total"])
        assign2 = float(data["assignment2"])
        assign2_total = float(data["assignment2_total"])
        attendance = float(data["attendance"])

        t1_scaled = convert_to_scale(t1, t1_total, 25)
        t2_scaled = convert_to_scale(t2, t2_total, 25)
        test_avg = (t1_scaled + t2_scaled) / 2

        assign1_scaled = convert_to_scale(assign1, assign1_total, 7.5)
        assign2_scaled = convert_to_scale(assign2, assign2_total, 7.5)
        assignment_total_scaled = assign1_scaled + assign2_scaled

        attendance_mark = get_attendance_marks(attendance)

        internal_total_real = test_avg + assignment_total_scaled + attendance_mark
        internal_total_rounded = round(internal_total_real)

        return jsonify({
            "status": "success",
            "result": f"{name}'s Internal Mark: {internal_total_rounded}/50",
            "mark": internal_total_rounded
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
