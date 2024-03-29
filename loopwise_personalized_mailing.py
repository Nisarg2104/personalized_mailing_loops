import smtplib,webbrowser
def getmail():

    services=['gmail','hotmail','yahoo','ymail','mail.yahoo', 'outlook','pilani.bits-pilani']
    while True:
        user_mail=(input("Enter your mail address")).lower()
        if "@" in user_mail and (".com" in user_mail or ".ac.in" in user_mail):
            sym_pos=user_mail.find("@")
            if ".com" in user_mail:
                domain_pos=user_mail.find(".com")
            else:
                domain_pos=user_mail.find(".ac.in")
            service_provider=user_mail[sym_pos+1:domain_pos]
            if service_provider not in services:
                print("We only provide services for:",end=' ')
                for i in services:
                    print(f"{i}")
                continue

            break
        else:
            print("Please enter a valid email.")
            continue
    return user_mail, service_provider


def set_smtp_domain(service_provider):
    if service_provider == 'gmail' or service_provider=='pilani.bits-pilani.ac.in':
        return 'smtp.gmail.com'
    elif service_provider=='yahoo' or service_provider=='ymail':
        return 'smtp.mail.yahoo.com'
    elif service_provider=='outlook' or service_provider=='hotmail':
        return 'smtp-mail.outlook.com'


user_mail,service_provider=getmail()
print(f"{user_mail},{service_provider},{set_smtp_domain(service_provider)}")

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.ehlo()
connection.starttls()
names=['Naveen Jain', 'Dmitry Itskov','Azim Premji','Kunal Bahl','Ashish Hemrajani']
emailid={'Naveen Jain':'naveen@intelius.com', 'Dmitry Itskov':'info@2045.com','Azim Premji':'azim.premji@wipro.com','Kunal Bahl':'kunal.bahl@snapdeal.com','Ashish Hemrajani':'ashish@bookmyshow.com'}
message={'Naveen Jain':'I have read about your idea of mining on the moon and I personally feel that all the students will find it really fascinating and interesting if you discuss it with them. ', 'Dmitry Itskov':'I have read about your initiative 2045 and I personally feel that all the students will find it really fascinating and interesting if you discuss it with them.','Kunal Bahl':'The story of your journey with snapdeal was very interesing and inspiring for me. I personally feel that all the students will find it really fascinating and interesting if you discuss it with them.','Ashish Hemrajani':'I personally feel that the story of your journey with bookmyshow will very interesing and inspiring for the students if you discuss it with them.','Azim Premji':'The story of your journey with wipro was very interesing and inspiring for me. I personally feel that all the students will find it really fascinating and interesting if you discuss it with them.' }

connection.login('nisargvora2104@gmail.com','8673033088')
for i in names:
  connection.sendmail('nisargvora2104@gmail.com','nisargvora2104@gmail.com', f'Subject: Invitation to give an online talk \n\n Dear {i} sir,\nGreetings of the day!\nI am a student of Birla Institute of Technology and Science (BITS) Pilani, India, which is one of the leading universities in India and a member of BITS Embryo. Embryo is a forum for live, online, interactive talks to augment the on-campus education of the students at BITS.\n\nThe idea of entrepreneurship and startups has become very popular these days. With growing popularity of such ideas it becomes very important that youngsters get the right guidance for their first venture. \n\nSir, you have achieved great  success in the field and popular among the students. your vast experience and ideas can be very valuable for young students who consider entrepreneurship a viable option. {message[i]} Hence, I would like to invite you for an online talk and share your experience among the students who consider you as their idol.\n\nThe audience will mainly consist of Science, Maths and Engineering students all interested in this topic. The talk will be of 40-45 minutes followed by a small question-answer session and will be conducted through video conferencing. All you need is an internet connection to get going. \n\nPlease let us know if you could devote some time to this lecture. We are looking forward to having a positive response from you.\nThank You')
  print()
connection.quit()
