from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import csv
import time
import datetime

url = 'https://web.whatsapp.com/send?phone=91'


# =========================================== Whatsapp Web Classes ====================================================
invalid_text_class_name='_2Nr6U'
textfield_class_name='_13NKt'
send_button_class_name='_4sWnG'
# ================================================================================================================

# =========================================== Reading from CSV File ====================================================
filename = "Contact.csv"
  
# initializing the titles and rows list
fields = []
rows = []
  
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
  
    # # get total number of rows
    # print("Total no. of rows: %d"%(csvreader.line_num))
print(rows)  
# printing the field names
# print('Field names are:' + ', '.join(field for field in fields))

# ================================================================================================================


# =========================================== Opening Chromes ====================================================
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=D:\\Scrapping\\whatsapp_blast\\chrome_user')
print('Launching Browser...')
browser = webdriver.Chrome(options=options)

# ================================================================================================================
index=0
total_contacts=len(rows)
successfully_sent=0
unsuccessful_in_sending=0
time_snapshot1=time.time()

for row in rows:


# =========================================== Editable params ====================================================
# name = 'Zeel Shah'
# mob = '9328548450'
    name = row[0]
    mob = row[1]
    print(name,mob)
    # ================================================================================================================

    link = url + mob
    msg = f'''Hello {name}!
    Hope you are doing well.

    Mood Indigo, IIT Bombay is back again with its 51st edition. We are very excited to tell you that pre-registrations for the College Connect Program(CCP) have started! This is your chance to become a member of the Indigo Squad and learn valuable skills.

    Pre-register now and invite your friends with your referral link. Top 10 members with the highest number of referrals will get internships and coupons.
    LINK for registration:https://my.moodi.org
    See you at Mood Indigo 2020!
    Thanks and regards,
    Team Mood Indigo 2020
    '''

    # options = webdriver.ChromeOptions()
    # options.add_argument('user-data-dir=D:\\Scrapping\\whatsapp_blast\\chrome_user')
    # print('Launching Browser...')
    # browser = webdriver.Chrome(options=options)

    browser.get(link)

    # sleep(15)
    while True:
        option_bar = browser.find_elements_by_class_name(textfield_class_name)
        print('into infi loop')
        if(len(option_bar)!=0):
            break
        else:
            sleep(5)



    # textbox=error[1]
    # text_box=None
    i=0
    status_code = 'Not yet started'
    err_flag=0
    new_user=True
    phone_number_exist='No'

    # Error Flags
    # 1 = Number do not exist
    # while False:
    while True:
        if new_user:
            
            # Check if phone number exist
            number_valid=browser.find_elements_by_class_name(invalid_text_class_name)
            if(len(number_valid)!=0):
                # print("What is inside the number_valid")
                # print(number_valid)
                status_code='Number do not exist'
                err_flag=1
                new_user=False
                print('Breaking from loop')
                unsuccessful_in_sending=unsuccessful_in_sending+1
                break
            else:
                # Cool, We can move on
                status_code='Number Exist'
                phone_number_exist='Yes'
                new_user=False
                continue
                # break

        error = browser.find_elements_by_class_name(textfield_class_name)
        text_box = error
        # print((error))
        if len(error) == 0:
            text_box = browser.find_elements_by_class_name('selectable-text')
            i=i+1
            if i==5:
                print('breaking because cant find the error')
                status_code='Error in Msg sending'
                unsuccessful_in_sending=unsuccessful_in_sending+1
                break
                
        if len(text_box) != 0:
            text_box = text_box[1]
            clicks = msg.split('\n')
            for click in clicks:
                text_box.send_keys(click)
                text_box.send_keys(Keys.SHIFT, Keys.ENTER)

            sleep(2)
            send_button = browser.find_element_by_class_name(send_button_class_name)
            send_button.click()
            status_code='Message sent successfully!'
            successfully_sent=successfully_sent+1
            break
    # print('Done for', name, mob)
    print(rows[index])
    rows[index].append(status_code)
    rows[index].append(err_flag)
    rows[index].append(phone_number_exist)
    index=index+1
    sleep(2)
print(rows)
browser.close()
fields.append('Status_Code')
fields.append('Err_Flag')
fields.append('phone_number_exist')
with open('waStatus.csv', 'w',newline='') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)      
    write.writerow(fields)
    write.writerows(rows)

time_elapsed=time_snapshot1 - time.time()

with open('session_logs.txt','a') as logs:
    logs.write('\n \n ====================================== \n \n')
    
    logs.write(f'======  Log Time : {datetime.datetime.now()} =====\n \n')

    logs.write(f'Total Contacts {total_contacts} \n')
    logs.write(f'successfully_sent {successfully_sent} \n')
    logs.write(f'unsuccessful_in_sending {unsuccessful_in_sending} \n')
    logs.write(f'time_taken {time_elapsed} \n')
    
    logs.write('\n \n ======================================')

