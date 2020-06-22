from Score_Management import Score_Management_System

if __name__ == "__main__":
    sms = Score_Management_System()
    sms.read("score.csv")
    print(sms.sort("avg", "des"))
    sms.write("result.csv", "avg", "des")

