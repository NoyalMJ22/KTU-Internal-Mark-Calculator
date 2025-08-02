from flask import Flask, render_template, request

app = Flask(__name__)

def convert_to_scale(mark, out_of, scale):
    """Convert marks to a specific scale"""
    if out_of <= 0:
        raise ValueError("Total marks must be greater than 0")
    return (mark / out_of) * scale

def get_attendance_marks(attendance_percent):
    """Calculate attendance marks based on percentage"""
    if attendance_percent >= 90:
        return 10.0
    elif attendance_percent >= 0:
        return round(attendance_percent / 10, 1)
    else:
        return 0

def validate_input(value, field_name, min_val=None, max_val=None):
    """Validate input values"""
    try:
        val = float(value)
        if min_val is not None and val < min_val:
            raise ValueError(f"{field_name} cannot be less than {min_val}")
        if max_val is not None and val > max_val:
            raise ValueError(f"{field_name} cannot be greater than {max_val}")
        return val
    except ValueError as e:
        if "cannot be" in str(e):
            raise e
        raise ValueError(f"Invalid {field_name}. Please enter a valid number.")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        # Get and validate student name
        name = request.form.get("name", "").strip()
        if not name:
            return render_template("index.html", result="Error: Student name is required")
        
        # Get and validate test marks
        t1 = validate_input(request.form.get("test1"), "Test 1 marks", 0)
        t1_total = validate_input(request.form.get("test1_total"), "Test 1 total marks", 0)
        t2 = validate_input(request.form.get("test2"), "Test 2 marks", 0)
        t2_total = validate_input(request.form.get("test2_total"), "Test 2 total marks", 0)
        
        # Get and validate assignment marks
        assign1 = validate_input(request.form.get("assignment1"), "Assignment 1 marks", 0)
        assign1_total = validate_input(request.form.get("assignment1_total"), "Assignment 1 total marks", 0)
        assign2 = validate_input(request.form.get("assignment2"), "Assignment 2 marks", 0)
        assign2_total = validate_input(request.form.get("assignment2_total"), "Assignment 2 total marks", 0)
        
        # Get and validate attendance
        attendance = validate_input(request.form.get("attendance"), "Attendance percentage", 0, 100)
        
        # Validate that marks don't exceed totals
        if t1 > t1_total:
            return render_template("index.html", result="Error: Test 1 marks cannot exceed total marks")
        if t2 > t2_total:
            return render_template("index.html", result="Error: Test 2 marks cannot exceed total marks")
        if assign1 > assign1_total:
            return render_template("index.html", result="Error: Assignment 1 marks cannot exceed total marks")
        if assign2 > assign2_total:
            return render_template("index.html", result="Error: Assignment 2 marks cannot exceed total marks")
        
        # Calculate scaled marks
        t1_scaled = convert_to_scale(t1, t1_total, 25)
        t2_scaled = convert_to_scale(t2, t2_total, 25)
        test_avg = (t1_scaled + t2_scaled) / 2
        
        assign1_scaled = convert_to_scale(assign1, assign1_total, 7.5)
        assign2_scaled = convert_to_scale(assign2, assign2_total, 7.5)
        assignment_total_scaled = assign1_scaled + assign2_scaled
        
        attendance_mark = get_attendance_marks(attendance)
        
        # Calculate final internal mark
        internal_total_real = test_avg + assignment_total_scaled + attendance_mark
        internal_total_rounded = round(internal_total_real)
        
        # Create detailed result
        result = f"""
        <strong>{name}'s Internal Mark: {internal_total_rounded}/50</strong><br><br>
        <strong>Breakdown:</strong><br>
        • Test Average: {test_avg:.1f}/25 (T1: {t1_scaled:.1f}, T2: {t2_scaled:.1f})<br>
        • Assignment Total: {assignment_total_scaled:.1f}/15 (A1: {assign1_scaled:.1f}, A2: {assign2_scaled:.1f})<br>
        • Attendance: {attendance_mark}/10 ({attendance}%)<br>
        • Raw Total: {internal_total_real:.1f}/50
        """
        
        return render_template("index.html", result=result)
        
    except ValueError as e:
        return render_template("index.html", result=f"Error: {str(e)}")
    except Exception as e:
        return render_template("index.html", result=f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    print("🚀 Starting KTU Internal Mark Calculator...")
    print("📱 Access the application at: http://localhost:5000")
    print("🌐 For network access: http://0.0.0.0:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=5000)

