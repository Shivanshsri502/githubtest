def display(row, info, t):
  print("Timer: " + str(t) + '\n' + "Roll Number: " + info[1] + '\n' + "Name: " + info[0] + '\n')
  print("Press Ctrl+Alt+U to see the unattempted questions")
  print("Question" + row['ques_no'] + ": " + row['question'])
  print("Option " + '1' + ") " + row['option1'])
  print("Option " + '2' + ") " + row['option2'])
  print("Option " + '3' + ") " + row['option3'])
  print("Option " + '4' + ") " + row['option4'])
  print("\n")
  print("Credits if correct option: " + row['marks_correct_ans'])
  print("Negative Marking: " + row['marks_wrong_ans'])
  print("Is compulsory: " + row['compulsory'])