import time

print("Welcome Player! to the KBC Game Show!")
time.sleep(2)

print("Loading Questions...")
time.sleep(2)

print("Your starting amount is ₹0")
time.sleep(1)

starting_amount=0

print("Let's begin the game!")
time.sleep(2)

print("First Question On Your Screen...")
time.sleep(2)
questions= {"Q1. What is the capital of France?": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome", "C"],
            "Q2. What is the largest planet in our solar system?": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars", "B"],
            "Q3. What is the chemical symbol for gold?": ["A. Au", "B. Ag", "C. Fe", "D. Hg", "A"],
            "Q4. What is the currency of Japan?": ["A. Yen", "B. Dollar", "C. Euro", "D. Pound", "A"],
            "Q5. What is the largest ocean on Earth?": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean", "D"],
            "Q6. What is the highest mountain in the world?": ["A. Mount Everest", "B. K2", "C. Kanchenjunga", "D. Lhotse", "A"],
            "Q7. What is the smallest country in the world?": ["A. Monaco", "B. Vatican City", "C. Nauru", "D. Mumbai", "B"],
            "Q8. What is the largest desert in the world?": ["A. Sahara Desert", "B. Arabian Desert", "C. Gobi Desert", "D. Kalahari Desert", "A"],
            "Q9. What is the longest river in the world?": ["A. Nile", "B. Amazon River", "C. Yangtze River", "D. Mississippi River", "A"],
            "Q10. What is the most spoken language in the world?": ["A. English", "B. Mandarin Chinese", "C. Spanish", "D. Hindi", "B"]}

for question in questions:
    print(question)
    for option in questions[question][:-1]:
        print(option)
    answer = input("Please enter your answer (A, B, C, or D): ")
    if answer.upper() == questions[question][-1]:
        print("Checking your answer...")
        time.sleep(2) 

        starting_amount = starting_amount + 1000
        print("Correct Answer! You won ₹1000!")
        print(starting_amount)
    else:
        print("Incorrect Answer! Game Over!")
        print("Amount Won",starting_amount)
        break
else:
    print("Congratulations! You have answered all questions correctly!")
    print("Total Amount Won: ₹", starting_amount)

 
  
