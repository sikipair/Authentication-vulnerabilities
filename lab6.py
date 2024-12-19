print("##########The following are the usernames:##########")
for i in range(150):
    if i % 3:
        print("carlos")
    else:
        print("wiener")

print("##########The following are the passwords:##########")
with open('password.txt', 'r') as f:
    lines = f.readlines()

i = 0
for pwd in lines:
    if i % 3:
        print(pwd.strip('\n'))  # Strip the newline character
    else:
        print("peter")
        print(pwd.strip('\n'))  # Corrected from pwd.string to pwd.strip
        i = i+1
    i = i+1  # Increment the counter
