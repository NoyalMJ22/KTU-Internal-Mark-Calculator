# 🎓 KTU Internal Mark Calculator

A clean and simple **Python desktop app** to calculate and visualize internal marks for students, based on KTU (Kerala Technological University) guidelines. Built using **Tkinter** for the GUI and **Matplotlib** for data visualization.

> � Made for teachers, tutors, and students to make internal mark calculations easy, quick, and organized.

## 🖥️ Features

✅ User-friendly GUI  
✅ Calculates internal marks based on:
- Tests (scaled to 25 marks)
- Assignments (scaled to 15 marks)
- Attendance (scaled to 10 marks)

✅ Visualize student marks using a **bar chart**  
✅ Save/load student records as `.json` files  
✅ Dark mode for better focus  
✅ Reset & real-time feedback  

## 📸 Screenshot

![Application Screenshot](https://github.com/user-attachments/assets/b5124eaa-10fc-4587-afcb-2b53257c0ba4)

## 🛠️ Tech Stack

| Component       | Technology Used |
|----------------|----------------|
| Language       | Python 3       |
| GUI Framework  | Tkinter        |
| Data Visualization | Matplotlib  |
| Data Storage   | JSON           |

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- pip package manager

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ktu-internal-mark-calculator.git
cd ktu-internal-mark-calculator
```
### 2. Install dependencies
```bash
pip install matplotlib
```
### 3. Run the application
```bash
python Internal.py
```
## 💡 How It Works

- Enter marks for two tests and two assignments.  
- Use the slider to set attendance percentage.  
- Click **Calculate** to get internal marks (out of 50).  
- Use **Save** to export student data as `.json`.  
- Use **Load** to import data from a saved file.  
- Click **Graph** to view all students' internal marks in a bar chart.

---

## 🔐 Internal Mark Breakdown

| Component      | Max Marks |
|----------------|-----------|
| Test Average   | 25        |
| Assignments    | 15        |
| Attendance     | 10        |
| **Total**      | **50**    |

> Attendance marks are automatically calculated based on percentage:

- **90%** attendance = **10 marks**  
- **75%** attendance = **7.5 marks**  
- **Below 50%** = proportionally less

---

## 🙋‍♂️ Who's This For?

- 🧑‍🏫 Teachers simplifying internal assessments  
- 👨‍🎓 Students checking their performance  
- 👨‍💻 Python beginners exploring:
  - GUI Development  
  - File Handling  
  - Data Visualization  

---

## ✅ To-Do / Improvements

- [ ] Export graph as PDF/image  
- [ ] Show average line in graph  
- [ ] Input validation for "out of" zero values  
- [ ] Refactor into a class-based architecture  

---

## 📜 License

This project is licensed under the **MIT License**.  
You’re free to use, modify, and distribute it for personal or academic purposes.

---

## 🤝 Contributing

Have suggestions or ideas? Contribute by:

1. Forking the repo  
2. Creating a new branch  
3. Submitting a pull request

---

## 🙌 Support

If you found this project helpful:

- ⭐ Star this repo  
- 📢 Share it with others  

Thanks for checking it out! 💙

