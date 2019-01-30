import datetime
name=input("What's your name?")
today=str(datetime.datetime.today().strftime('%Y-%m-%d'))
print("Hello,"+name+"! today is "+today)
