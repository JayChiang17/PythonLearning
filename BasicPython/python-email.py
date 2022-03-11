# -*- coding:UTF-8 -*-
def email_sender():
    import email.message
    msg = email.message.EmailMessage()
    msg["Frome"] = "q0988138683@gmail.com"
    msg["To"] = "chiang.mengchieh@gmail.com"
    msg["Subject"] = "測試"
    #寄送純文字內容
    # msg.set_content("testing...")
    #寄送比較多的內容(HTML語法)
    # <h3> ----> 標題文字
    msg.add_alternative("<h3>TEST<h3>測試內容",subtype = "html")

    #連線到SMTP Server, 驗證寄件人身份並發送郵件
    import smtplib
    #到網路上搜尋 gmail server 或是 yahoo stmp server 等等..
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    #密碼是由gmail 應用程式密碼產生的一次性亂碼
    server.login("q0988138683@gmail.com","qymvusiokmurpcvq")
    server.send_message(msg)
    server.close()

email_sender()
