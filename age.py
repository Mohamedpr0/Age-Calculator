from datetime import datetime, timedelta

def calculate_age(birthdate):
    try:
       
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
        
      
        current_date = datetime.now()
        
        
        age = current_date - birthdate
        
   
        total_seconds = age.total_seconds()
        days = age.days
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
     
        return days, int(hours), int(minutes), int(seconds)
    
    except ValueError:
        print("Invalid date format. Please enter your birthdate in YYYY-MM-DD format.")
        return None

birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")


age = calculate_age(birthdate_input)


if age:
    days, hours, minutes, seconds = age
    print(f"Your age is {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")
