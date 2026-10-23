# Python-internship-project2

# Project 02: Number Guessing Game & Word Counter

## About
A menu-driven Python project containing a number guessing game
and a text-file word frequency counter.

## Features
- Random number between 1 and 100
- Seven valid guessing attempts
- Hints for guesses that are too high or too low
- Score and best score tracking during the session
- Reads UTF-8 text files safely
- Counts total and unique words
- Displays the top 10 most frequent words
- Handles invalid input and missing files

## Scoring Rule
The player starts with 100 points and loses 10 points for each
incorrect valid guess. Invalid inputs and numbers outside the
range do not count as attempts. A correct guess on the seventh
attempt earns 10 points. Failure to guess earns 0 points.

## Requirements
Python 3.10 or newer. No external packages are required.

## How to Run
1. Keep project2.py and sample.txt in the same folder.
2. Open a terminal in that folder.
3. Run:

   python project2.py

4. Select option 1 to play or option 2 to count words.

## Word Counter
The program ignores letter case and removes standard punctuation.
Common words such as "the" and "and" may dominate the results.
