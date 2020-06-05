# poli_mail

Modeled after www.defund.org/nyc.

I've had a few friends who were worried about sending their email through a mass online portal. 
This auto-emailer is a small python script that retains all personal information to runtime; and deletes immediately after. 


- Currently the program supports gmail accounts and is intended to contact all council members in NYC. 
- please read and be sure you know what you are sending.


## The Email

provided by defund.org

"Dear New York City Council Members,

My name is [YOUR NAME] and I am a resident of [BOROUGH]. Last April, NYC Mayor Bill De Blasio proposed major budget cuts for the Fiscal Year 2021, especially to education and youth programs, while refusing to slash the NYPD budget by any significant margin.

I am emailing today to demand that you vote no on the Mayor’s FY21 proposed budget. Furthermore, I urge you to pressure the office of the mayor towards an ethical and equal reallocation of the NYC expense budget, away from NYPD and towards social services and education programs, effective at the beginning of FY21, July 1, 2020.

Governor Cuomo has doubled the presence of the NYPD on New York City streets. I am asking that city officials lobby the same amount of attention and effort towards finding sustainable, longterm change.

Thank you, [YOUR NAME] [YOUR ADDRESS] [YOUR EMAIL] [YOUR PHONE NUMBER]"


## How the program works

    git clone https://github.com/FinchMF/poli_mail.git

Navigate to the appropiate directory and run

    python poli_mail.py

In your terminal you will be prompted with a serious of questions. If you do not want to answer th questions, you can put N/A; but understand how the your answers are input into the email. 

If you wish to email the council memebers, it is important to legitmize your plea by making yourself transparent. 

Most importantly, if you do not put an email address, the email will not send. 



***********
### IMPORTANT

If you wish to use this program, besure to go visit https://support.google.com/accounts/answer/6010255?hl=en#:~:text=Turn%20off%20%22Less%20secure%20app,Allow%20less%20secure%20apps%20off.

Here you can enable the script to access your gmail account from your opperating system.


This program will run soley on your device and is no way connected to any third parties. The purpose of this program is to secure that no online portal is retaining any information about an individual when an individual is giving temporary access to their OS and or email account. Again, all information is only stored during runtime on your machine and is deleted after.

The body of the email will be located in
    
     NYC/defund_NYPD_{name}.txt

### Lastly
This repo will be updated to include more cities and more email server access in the coming days. 

Be Safe



