p1="buy now"
p2="subscribe now"
p3="click this"
p4="make lots of money"

message=input("Enter the comment:")
if(message in p1 or message in  p2 or message in p3 or message in p4):
    print("This message is a spam")

else:
    print("This message is not a spam")
