```python
import random

# List of questions
questions = [
    "One good thing that happened to me today",
    "Something good that I saw someone do",
    "Today I had fun when",
    "Something that I accomplished today",
    "Something funny that happened today",
    "Someone I was thankful for today",
    "Today I smiled when",
    "Something about today I'll always remember",
    "Today I was proud of myself because",
    "Something interesting that happened today",
    "Something that made me think",
    "Something I let myself off for today",
    "Something that I liked about myself today",
    "Something thoughtful I did today",
    "My favourite part of today",
    "Something new I did today",
    "Something I was happy about today",
    "I am grateful for",
    "Something I did for someone else today",
    "Something I did well today",
    "Today I learned",
    
]

# Ensure there are enough questions to pick 3 for each day of the week
if len(questions) < 21:
    raise ValueError("Not enough questions to pick a unique set of 3 for each day of the week.")

# Shuffle the questions once
random.shuffle(questions)

# Allocate questions for each day of the week
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
schedule = {}
for i, day in enumerate(days_of_the_week):
    # Pick 3 unique questions for each day
    schedule[day] = questions[i*3:(i+1)*3]

# Print the schedule as a markdown table compatible with Obsidian
print("| Day of the Week | Question 1 | Question 2 | Question 3 |")
print("| --------------- | ----------- | ----------- | ----------- |")
for day, daily_questions in schedule.items():
    print(f"| {day} | {daily_questions[0]} | {daily_questions[1]} | {daily_questions[2]} |")
    print("| | | | |")  # Empty row for answers
```