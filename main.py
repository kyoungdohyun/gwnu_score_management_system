from Score_Management import Score_Management_System

if __name__ == "__main__":
    sms = Score_Management_System()
    sms.read("C:\\working\\openSource_lecture\\final_project\\gwnu_score_management_system\\score.csv")#경로 오류로 인하여 절대경로로 지정
    print(sms.sort("avg", "des"))
    sms.write("C:\\working\\openSource_lecture\\final_project\\gwnu_score_management_system\\result.csv", "avg", "des")
#경로 오류로 인하여 절대경로로 지정
