# 🌐 CLI Downloader Simulator

A simple command-line download simulator built with Python.

## 🤷‍♂️ Why I Created This Project

I created this project as a **Beta Project** 📽️, not because I needed to learn Python from scratch, but because I wanted to strengthen a different skill: **mathematical reasoning and computational logic.** 🧩

I already had experience working with Python, but I wanted to become better at translating mathematical problems into working code.

The idea was simple: simulate a file download using a given file size and internet speed, calculate the download progress, and display it through a terminal-based loading bar.

What started as a relatively simple simulation gradually became an exercise in understanding calculations, handling different scenarios, and figuring out how to translate an idea into actual Python logic.

I deliberately worked through the implementation myself, using ChatGPT just for hints & guidance when needed rather than following a step-by-step tutorial (becasue I want to make it challenging).

## 🤔 What Does It Do?

The program simulates a file download based on:

- 📁 File size.
- 🛜 Internet download speed.
- 📟 Download progress over time.

It converts the provided file size and internet speed into a common unit (Bytes), calculates how much data has been downloaded, and updates the terminal with a visual progress bar.

## 💻 Features

- 📁 Accepts file sizes in KB, MB, and GB.
- 🛜 Accepts internet speeds in bps, Kbps, Mbps, and Gbps. (It assumes constant interent speed in bits)
- 📟 Converts different units into Bytes for consistent calculations.
- 🧒 Validates user input and handles common invalid entries.
- 📥 Calculates downloaded data and remaining data.
- 📥 Calculates download progress as a percentage.
- 🔋 Displays a dynamically updating terminal progress bar.
- 🟢 Uses ANSI escape sequences for terminal output and colouring.

## ✏️ Concepts I Practised

The main focus wasn't learning individual Python syntax, but applying concepts together to solve a problem.

Some of the areas I worked on:

- 🔠 Mathematical reasoning and unit conversion.
- 🔢 Working with integers and floating-point numbers.
- 💡 Conditional logic and loops.
- 📋 Lists, indexing, and slicing.
- 🧩 String manipulation and formatting.
- ✅ Exception handling and input validation.
- 🟰 Percentage calculations.
- 🧩 Handling different download scenarios and edge cases.
- 📟 Updating terminal output dynamically.

## 🖥️ Technologies Used

- **Python 3**
- `time` — for simulating download intervals.
- ANSI escape sequences — for terminal formatting and colours.

No external Python packages are required.

## 🎛️ How to Run

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd CLI-Downloader-Simulator
   ```

3. Run the program:

   ```bash
   python3 main.py
   ```

4. Enter the requested file size and internet speed when prompted.

## 🖋️ What I Learned (Personal Experience)

The most valuable part of this project was not the final output, but the process of getting there.

I encountered situations where my initial calculations and assumptions didn't work as expected. Instead of immediately replacing them with ready-made solutions, I tried to understand why they failed and develop a better approach.

One example was the progress bar. My initial implementation assumed that the download percentage would increase by at least 1% in every iteration. That assumption wasn't always valid, especially when dealing with larger files and slower download speeds.

I eventually reconsidered the approach and used Python list slicing to update the progress bar based on the calculated percentage.

This project reinforced an important idea for me:

**Knowing a programming language is one thing. Being able to translate a problem into logical steps, calculations, and working code is another.**

And that was the entire point of building this project.

---

*This is a learning-focused project and a part of my Python Beta Projects — small experiments designed to strengthen specific programming and problem-solving skills before applying them to larger projects.*