Task = input("Enter your task: ")
priority = input ("What is the Priority? (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        if time_bound == "yes":
            print(f"Remainder: {Task} is a high priority task that requires immediate attention today! ")
        else:
            print(f"Note: {Task} is a high priority task. Consider completing it when you have free time.")
    
    case 'medium':
        if time_bound == "yes":
            print(f"Remainder: {Task} is a medium priority task that requires immediate attention today! ")
        else:
            print(f"Note: {Task} is a medium priority task. Consider completing it when you have free time.")
    
    case 'low':
        if time_bound == "yes":
            print(f"Remainder: {Task} is a low priority task that requires immediate attention today! ")
        else:
            print(f"Note: {Task} is a low priority task. Consider completing it when you have free time.")
    