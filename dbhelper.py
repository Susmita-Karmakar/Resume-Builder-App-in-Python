import mysql.connector

class DBhelper:
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(host='localhost',user='root',password='',database='resume_data')
            self.mycursor=self.conn.cursor()
            print("connected to DB")
        except Exception as e:
            print(e)

    def check_login(self,login_email,password):
        self.mycursor.execute("SELECT * FROM user WHERE login_email LIKE '{}' AND password LIKE '{}'".format(login_email, password))
        data = self.mycursor.fetchall()
        return data


    def insert_user(self,login_name,login_email,password):
        try:
            self.mycursor.execute("INSERT INTO user(user_id,login_name,login_email,password) VALUES(NULL,'{}','{}','{}')".format(login_name,login_email,password))
            self.conn.commit()
            # data=self.mycursor.fetchall()
            # if len(data)>2:
            #     return 1
        except Exception:
            return 0
        # except Exception as e:
        #     print(e)

    def contact(self,user_id,info):

        try:
            self.mycursor.execute("UPDATE user SET name='{}',email='{}',contact_no={},linked='{}',github='{}' WHERE user_id={}".format(info[0],info[1],info[2],info[3],info[4],user_id))

            self.conn.commit()
            # data=self.mycursor.fetchall()
            # if len(data)>0:
            #     return 1
            # else:
            #     return 0
        except Exception as e:
            print(e)

    def educational(self,user_id,info):
        try:
            self.mycursor.execute("UPDATE user SET course='{}',institute='{}',score={},year='{}' WHERE user_id={}".format(info[0],info[1],info[2],info[3],user_id))
            self.conn.commit()

        except:
            return 0

    def educational2(self,user_id,info):
        try:
            self.mycursor.execute("UPDATE user SET course2='{}',institute2='{}',score2={},year2='{}' WHERE user_id={}".format(info[0],info[1],info[2],info[3],user_id))
            self.conn.commit()

        except:
            return 0

    def educational3(self,user_id,info):
        try:
            self.mycursor.execute("UPDATE user SET course3='{}',institute3='{}',score3={},year3='{}' WHERE user_id={}".format(info[0],info[1],info[2],info[3],user_id))
            self.conn.commit()

        except Exception as e:
            print (e)
            return 0


    def career_ob(self,user_id,career):
        try:
            self.mycursor.execute("UPDATE user SET career='{}' WHERE user_id={}".format(career,user_id))
            self.conn.commit()

        except:
            return 0

    def abt_skills(self,user_id,skills):
        try:
            self.mycursor.execute("UPDATE user SET skills='{}' WHERE user_id={}".format(skills,user_id))
            self.conn.commit()

        except:
            return 0

    def abt_projects(self,user_id,projects):
        try:
            self.mycursor.execute("UPDATE user SET projects='{}' WHERE user_id={}".format(projects, user_id))
            self.conn.commit()

        except:
            return 0

    def abt_languages(self,user_id,language):
        try:
            self.mycursor.execute("UPDATE user SET language='{}' WHERE user_id={}".format(language, user_id))
            self.conn.commit()

        except:
            return 0

    def abt_awards(self,user_id,awards):
        try:
            self.mycursor.execute("UPDATE user SET awards='{}' WHERE user_id={}".format(awards, user_id))
            self.conn.commit()

        except:
            return 0

    def abt_per_det(self,user_id,info):
        try:
            self.mycursor.execute(
                "UPDATE user SET father='{}',mother='{}',address='{}',dob={},hobby='{}' WHERE user_id={}".format(info[0],info[1],info[2],info[3],info[4],user_id))
            self.conn.commit()

        except:
            return 0

    def show(self,user_id):
        print("Hi")
        self.mycursor.execute("SELECT * FROM user WHERE user_id={}".format(user_id))
        cv=self.mycursor.fetchall()
        return cv

    def data_fetch(self,user_id):
        self.mycursor.execute("SELECT * FROM user WHERE user_id LIKE {}".format(user_id))
        data=self.mycursor.fetchall()
        return data[0]
