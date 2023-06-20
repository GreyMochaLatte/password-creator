# password-creator
creates, stores, and updates passwords

It can create a new password for an account. It's saved as [account name]: [password] in a file called "Papa's Apple Pie Recipe.txt". The user can select a standard 30 random character long password or a custom password. The custom option asks for the length of the password and how many lowercase letters, uppercase letters, numbers, and symbols are needed. It will use up the four types of characters before returning to random characters to fill the rest of the length

It can recover a password by the account name.
It displays it as [account name]: [password]

It should be able to update a password. It should be able to find the password by account name, delete the old information, and replace it with a new password (standard or custom).
 

To-Do
- fix update to actually change the password for the selected account
- what to do if custom password length is less than sum of all minimum character types
- give it an UI
- store passwords on an online notebook website as well
  - have the program check if the txt file and website version match
    - ask user which to keep and update incorrect one
- change an individual character in a password or all passwords (i.e. change all 'S's to 'Z's) 
