ticket_data = {    'Ticket_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Customer_Name': [ 'Ravi', 'Meera', 'Sam', 'Anu', 'Rakesh',
                       'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'
    ],   
 'Issue_Description': [
        ' Internet not working!!! ',
        'slow response, very poor service ',
        'GREAT support! issue resolved.',
        ' okay... need help ',
        'not BAD but slow',
        'Excellent guidance, Very Helpful!',
        'good support and good behaviour!',
        'Poor handling of technical issue',
        'Satisfied. Could be better.',
        'Good service... quick response.'

    ],  
  'Priority': ['High', 'Low', 'High', 'Medium', 'Low',
               'High', 'Medium', 'High', 'Low', 'Medium']}
print(ticket_data)
def display_tickets(ticket_data):
    for i in range(len(ticket_data['Ticket_No'])):
       print("Ticket_no:", ticket_data["Ticket_No"][i])
       print("Customer Name:", ticket_data["Customer_Name"][i])
       print("Issue_Description:", ticket_data["Issue_Description"][i])
       print("Priority:", ticket_data["Priority"][i])
       print("-" * 60)
    
display_tickets(ticket_data)
 

# Add new tickets
ticket_count = int(input("Enter the number of tickets required: "))
new_ticket=[]
for _ in range(ticket_count):
    new_Ticket_No = len(ticket_data['Ticket_No']) + 1
    new_Customer_Name = input("Enter name: ")
    new_Issue_Description = input("Enter issue: ")
    new_Priority = input("Enter priority (High/Low/Medium): ").capitalize()

    while new_Priority not in ["High", "Low", "Medium"]:
         print("Invalid priority. Ticket not added.")
         new_Priority = input("Enter priority (High/Low/Medium): ").capitalize()
    
    ticket_data['Ticket_No'].append(new_Ticket_No)
    ticket_data['Customer_Name'].append(new_Customer_Name)
    ticket_data['Issue_Description'].append(new_Issue_Description)
    ticket_data['Priority'].append(new_Priority)
    print(f"Ticket {new_Ticket_No} added successfully!")
    

print("\nUpdated Ticket Data:")
for i in range(len(ticket_data['Ticket_No'])):
    print("Ticket_no:", ticket_data["Ticket_No"][i])
    print("Customer Name:", ticket_data["Customer_Name"][i])
    print("Issue_Description:", ticket_data["Issue_Description"][i])
    print("Priority:", ticket_data["Priority"][i])
    print("-" * 60)
  


# Cleaning issue description
def clean_issue_description(text):
    text =text.replace("!","")
    text =text.replace(".","")
    text =text.replace("?","")
    text =text.replace("-","")
    text = text.strip()
    text = text.replace("%ok%", "okay")
    text = text.replace("%u%", "you")
    text = " ".join(text.split())
    text = text.lower()   
    return text

ticket_data["Issue_Description"] = [
    clean_issue_description(i) for i in ticket_data["Issue_Description"]
]
print("\nCleaned ticket_data with cleaned Issue_Description")
display_tickets(ticket_data)

# Function to count tickets containing a given word
def count_tickets_with_word(word):
    count = 0
    for i in ticket_data["Issue_Description"]:
        if word.lower() in i.lower(): 
            count += 1
    return count

print("Number of tickets containing 'poor':", count_tickets_with_word("poor"))
print("Number of tickets containing 'good':", count_tickets_with_word("good"))
print("Number of tickets containing 'slow':", count_tickets_with_word("slow"))
print("Number of tickets containing 'excellent':", count_tickets_with_word("excellent"))
print("*"*60)

#Final cleaned ticket
print("{")
last_key =list(ticket_data.keys())[-1]
for key, value in ticket_data.items():
    if key == last_key:
         print(f'"{key}": {value}')
    else:    
         print(f'"{key}": {value},')
print("}")

print("-"*60)
# Priority Analysis
high_count=0
medium_count=0
low_count=0
for i in ticket_data['Priority']:
    if i=="High":
        high_count= high_count+1
    elif i =="Medium":
        medium_count= medium_count+1
    else :
        low_count= low_count+1
print("Number of High Priority tickets : ",high_count)
print("Number of Medium Priority tickets : ",medium_count)
print("Number of Low Priority tickets : ",low_count)
print("*"*60)
    
#Ticket with longest issue description
max_count = 0
max_index = 0

for i in range(len(ticket_data['Issue_Description'])):
    words=ticket_data['Issue_Description'][i].split()
    word_count = len(words)
    if word_count>max_count:
        max_count = word_count
        max_index=i
        
print("Ticket_No :", ticket_data['Ticket_No'][max_index])
print("Customer_Name :", ticket_data['Customer_Name'][max_index])
print("Issue_Description :", ticket_data['Issue_Description'][max_index])
print("Word_count :", max_count)
print("*"*60)


unique_words = set()   # empty set to store unique words
for ticket in range(len(ticket_data["Issue_Description"])):
    words =ticket_data["Issue_Description"][ticket].split()
    for w in words:
        unique_words.add(w.lower())   


sorted_words = sorted(unique_words)

print("Count of unique words:", len(sorted_words))
print("Unique word list:", sorted_words)











        
       
   











