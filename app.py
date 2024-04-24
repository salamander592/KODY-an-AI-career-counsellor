#!/usr/bin/env python
# coding: utf-8

# In[3]:


from datetime import time
import time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

# loading in the model to predict on the data
pickle_in = open("C:\\Users\\aksha\\OneDrive\\Desktop\\aicscc.pkl", 'rb')
model = pickle.load(pickle_in)

def welcome():
    return 'welcome all'





# defining the function which will make the prediction using
# the data which the user inputs
def prediction(Web1, Cyber1, Web2, Insys1, SE1, DS1, ML1, Cyber2, Web3, SE2, ML2, Insys2, DS2, Web4, SE3, ML3, Insys3, Cyber3, DS3, Web5, SE4, ML4, Insys4, Cyber4, DS4, SE5, ML5, Insys5, DS5, Cyber5, Web6, SE6, ML6, Insys6, Cyber6, DS6):
    prediction = model.predict(
        [[Web1, Cyber1, Web2, Insys1, SE1, DS1, ML1, Cyber2, Web3, SE2, ML2, Insys2, DS2, Web4, SE3, ML3, Insys3, Cyber3, DS3, Web5, SE4, ML4, Insys4, Cyber4, DS4, SE5, ML5, Insys5, DS5, Cyber5, Web6, SE6, ML6, Insys6, Cyber6, DS6]])
    print(prediction)
    return prediction

#For the Purpose of Visual Graph
def data_score(Web1, Cyber1, Web2, Insys1, SE1, DS1, ML1, Cyber2, Web3, SE2, ML2, Insys2, DS2, Web4, SE3, ML3, Insys3, Cyber3, DS3, Web5, SE4, ML4, Insys4, Cyber4, DS4, SE5, ML5, Insys5, DS5, Cyber5, Web6, SE6, ML6, Insys6, Cyber6, DS6):

    #defining Ranking Criteria
    #Dynamic data from website for Ranking.
    RankML=1.2
    RankDS=1.0
    RankSE=0.8
    RankCyber=0.6
    RankWeb=0.4
    RankInsys=0.2


    #Calculating Total Marks of Each Field
    TmML = ML1 + ML2 + ML3 + ML4 + ML5 + ML6
    TmDS = DS1 + DS2 + DS3 + DS4 + DS5 + DS6
    TmSE = SE1 + SE2 + SE3 + SE4 + SE5 + SE6
    TmCyber = Cyber1 + Cyber2 + Cyber3 + Cyber4 + Cyber5 + Cyber6
    TmWeb = Web1 + Web2 + Web3 + Web4 + Web5 + Web6
    TmInsys = Insys1 + Insys2 + Insys3 + Insys4 + Insys5 + Insys6

    #calculating Data Score of Each Field by Adding ranking and total maarks
    DataScoreML = TmML + RankML
    DataScoreDS = TmDS + RankDS
    DataScoreSE = TmSE + RankSE
    DataScoreCyber = TmCyber + RankCyber
    DataScoreWeb = TmWeb + RankWeb
    DataScoreInsys = TmInsys + RankInsys

    return (DataScoreML, DataScoreDS, DataScoreSE, DataScoreCyber, DataScoreWeb, DataScoreInsys)


#For Calculating the Percentages for Graph Presentation
def calulate_percentage(mls, dss, ses, cys, webs, inss):
    totalscore=mls+dss+ses+cys+webs+inss

    persml=((mls/totalscore)*100)
    persds = ((dss / totalscore) * 100)
    perses = ((ses / totalscore) * 100)
    percys = ((cys / totalscore) * 100)
    persweb = ((webs / totalscore) * 100)
    persins = ((inss / totalscore) * 100)

    return (persml, persds, perses, percys, persweb, persins)

# this is the main function in which we define our webpage
def main():
    st.set_page_config(
        page_title="AICSCC",
        page_icon="https://cdn-icons-png.flaticon.com/512/1589/1589592.png",
        layout="wide",
    )

    # giving the webpage a title
    st.title("AICSCC")

    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    # Render the h1 block, contained in a frame of size 200x200.

    nav = st.sidebar.selectbox("Navigation", ["Home", "Recommendation", "About"])

    page_bg_img = '''
    <style>
    .design{
    background-image: url("https://media.istockphoto.com/photos/office-conference-room-meeting-digital-enterpreneur-presents-for-picture-id1360337466?b=1&k=20&m=1360337466&s=170667a&w=0&h=3l8otkwjLa3Chjw4V6wFVZjeM7CGqw_sK_XzDDEIJ24=");
    background-size: cover;
    }
    .layer {
    background-color: rgb(15 60 163 / 70%);
    position: absolute;
    left: 0;
    width: 100%;
    height: 98%;
    padding: 100px 0;

}

.stButton{
text-align:center;
padding-top: 40px;
}
.stButton button{
border: 2px solid;
}
    </style>
    '''

    html_temp = """ 
    <br>
    <div class="design" style ="background-color:cyan; height:320px;">
    <div class="layer">
    <h2 style ="color:white;text-align:center;">Get Best Career Recommendation 
        <br>From Expert AI Counsellor </h2>
                <h5 style ="color:white;text-align:center;">We Match the Right People with Right Field </h5>
    </div>
    </div>
    """

    bottom_page_bg_img = '''
        <style>
      
        .designed{
        height:240px;
        width:100%;
        background-image: url("https://www.simpleimageresizer.com/_uploads/photos/bcbce26c/front_1_780x175.png");
        background-size: cover;
        }
        
        @media screen and (max-width: 480px) {
  .designed {
    display: none;
  }
        </style>
        '''


    bottom_html_temp = """ 
    <div class="designed">
    </div>
<br>
    """

    about = """ 
        <div class="paragraph">
        <h4>Artificial Intelligence based Computer Science Career Counsellor</h4>
        <p>AI based Computer Science Career Counsellor recommends a most suitable field for
further studies to Computer Science graduates. AICSCC also displays all the fields
in a visual graph with percentage of chances of success. AICSCC provides free of cost career counselling facility to computer science graduates. 

AICSCC is an intelligent machine learning model trained on a specified dataset, embedded in a streamlit web app. User interacts with it's easy to use web interface. It asks user to answer some questions. On the basis of user's answers, AICSCC recommends a most suitable field for study to user by using the supervised machine learning techniques. AICSCC also recommends a visual graph with chances of success in all fields of computer science.</p>
        </div>
    <br>
        """

    about = """ 
            <div class="paragraph">
            <h4>Artificial Intelligence based Computer Science Career Counsellor</h4>
            <p>AI based Computer Science Career Counsellor recommends a most suitable field for
    further studies to Computer Science graduates. AICSCC also displays all the fields
    in a visual graph with percentage of chances of success. AICSCC provides free of cost career counselling facility to computer science graduates. 

    AICSCC is an intelligent machine learning model trained on a specified dataset, embedded in a streamlit web app. User interacts with it's easy to use web interface. It asks user to answer some questions. On the basis of user's answers, AICSCC recommends a most suitable field for study to user by using the supervised machine learning techniques. AICSCC also recommends a visual graph with chances of success in all fields of computer science.</p>
            </div>
        <br>
            """



    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown(html_temp, unsafe_allow_html=True)
    if st.button('Lets Get Started'):
        nav="Recommendation"
    st.markdown(bottom_page_bg_img, unsafe_allow_html=True)
    st.markdown(bottom_html_temp, unsafe_allow_html=True)
    st.info('Please Enable Recommendation Mode from Navigation for Recommendation')

    if nav == "Recommendation":
        # the following lines create text boxes in which the user can enter
        # the data required to make the prediction
        ques1 = st.radio("1) Do you know HTML, CSS, JavaScript, PHP and database?", ('Yes, I know all', 'I know HTML, CSS, JavaScript and database', 'I know PHP and database', 'No, I don’t know'))
        if ques1 == 'No, I don’t know':
            Web1 = 0
        else:
            Web1 = 1
        ques2 = st.radio("2) How much do you know about malware attacks and security algorithms?", ('Full understanding', 'Little understanding', 'Just know basics', 'Just hear about it'))
        if ques2 == 'Full understanding' or ques2 == 'Little understanding':
            Cyber1 = 1
        else:
            Cyber1 = 0
        ques3 = st.radio("3) How efficiently you can work with SQL database platform?", ('Full understanding', 'Little understanding', 'Just know basics', 'Just hear about it'))
        if ques3 == 'Full understanding' or ques3 == 'Little understanding':
            Web2 = 1
        else:
            Web2 = 0

        ques4 = st.radio("4) A function of process step of data processing is", ('Retrieval', 'Update', 'Protect', 'Index'))
        if ques4 == 'Retrieval':
            Insys1 = 1
        else:
            Insys1 = 0

        ques5 = st.radio("5) What is the full form of the “COCOMO” model?", ('Cost Constructive Estimation Model', 'Constructive Cost Estimation Model', 'Constructive Case Estimation Model', 'Constructive Cost Estimating Model'))
        if ques5 == 'Constructive Cost Estimation Model':
            SE1 = 1
        else:
            SE1 = 0
        ques6 = st.radio("6) What kind of distance metric(s) are suitable for categorical variables to find the closest neighbors?", ('Euclidean distance', 'Manhattan distance', 'Minkowski distance', 'Hamming distance'))
        if ques6 == 'Hamming distance':
            DS1 = 1
        else:
            DS1 = 0



        ques7 = st.radio("7) What is the disadvantage of decision trees?", ('Factor Analysis', 'Decision trees and robust of outliers', 'Decision trees and prone to be overfit', 'All of the above'))
        if ques7 == 'Decision trees and prone to be overfit':
            ML1 = 0
        else:
            ML1 = 1
        ques8 = st.radio("8) To protect the computer system against the hacker and different kind of viruses, one must always keep _________ on in the computer system.", ('Antivirus', 'Firewall', 'VLC player', 'Script'))
        if ques8 == 'Firewall':
            Cyber2 = 1
        else:
            Cyber2 = 0
        ques9 = st.radio("9) When trying to access a URL, the following message is displayed on the browser: Server; Error 403.What could be the reason for the message?", ('The requested HTML file is not available', 'The path to the interpreter of the script file is invalid', 'The first line of the output from the script is not a valid HTTP header', 'The requested HTML file or CGI script has insufficient permission'))
        if ques9 == 'The requested HTML file or CGI script has insufficient permission':
            Web3 = 1
        else:
            Web3 = 0

        ques10 = st.radio("10) Would you like to collect requirements from potential clients and stakeholders both?", ('Yes, I like it', 'Yes, I can', 'I feel uncomfortable during communication', 'No, I don’t like it'))
        if ques10 == 'Yes, I like it' or ques10 == 'Yes, I can':
            SE2 = 1
        else:
            SE2 = 0

        ques11 = st.radio("11) You love to work on Data modeling and evaluation?", ('Yes, I like it', 'Yes, I do it in my free time', 'I rarely do it', 'No, I don’t like it'))
        if ques11 == 'Yes, I like it' or ques11 == 'Yes, I do it in my free time':
            ML2 = 1
        else:
            ML2 = 0

        ques12 = st.radio("12) Are you interested in management of resources and people using information system?", ('Yes, I like it', 'Yes, I do it in my free time', 'I rarely do it', 'No, I don’t like it'))
        if ques12 == 'Yes, I like it' or ques11 == 'Yes, I do it in my free time':
            Insys2 = 1
        else:
            Insys2 = 0
        ques13 = st.radio("13) Do you like to find insights from data for prediction and recommendation?", ('Yes, I like it', 'Yes, I do it in my free time', 'I rarely do it', 'No, I don’t like it'))
        if ques13 == 'Yes, I like it' or ques11 == 'Yes, I do it in my free time':
            DS2 = 1
        else:
            DS2 = 0




        ques14 = st.radio("14) What is the correct HTML for referring to an external style sheet?", ('<style src="mystyle.css">', '<stylesheet>mystyle.css', '<link rel="stylesheet" type="text/css" href="mystyle.css">', 'None of these'))
        if ques14 == '<link rel="stylesheet" type="text/css" href="mystyle.css">':
            Web4 = 0
        else:
            Web4 = 1
        ques15 = st.radio("15) According to an IBM research, “31% of projects are abandoned before they are completed, 53% exceed their cost projections by an average of 189 percent, and 94 projects are restarted for every 100 projects.” What is the significance of these figures? ", ('Lack of software ethics and understanding', 'Management issues in the company', 'Lack of adequate training', 'All of the mentioned'))
        if ques15 == 'Lack of adequate training':
            SE3 = 1
        else:
            SE3 = 0
        ques16 = st.radio("16) Which of the followings are most widely used metrics and tools to assess a classification model?", ('Confusion Matrix', 'Cost-sensitive accuracy', 'Area under the ROC curve', 'All of the above'))
        if ques16 == 'All of the above':
            ML3 = 1
        else:
            ML3 = 0

        ques17 = st.radio("17) The system conversion technique of totally removing the existing system and immediately implementing the new system is called", ('Parallel run', 'Phased conversion', 'Crash conversion', 'Pilot conversion'))
        if ques17 == 'Crash conversion':
            Insys3 = 1
        else:
            Insys3 = 0

        ques18 = st.radio("18) In Wi-Fi Security, which of the following protocol is more used?", ('WPA', 'WPA2', 'WPS', 'Both A and C'))
        if ques18 == 'WPA2':
            Cyber3 = 1
        else:
            Cyber3 = 0
        ques19 = st.radio("19) What will be the output of the following code?"
                          "import numpy as np"
                          "my_array = np.arange(6).reshape(2,3)"
                          "result = np.trace(my_array)"
                          "print(result)", ('2', '4', '6', '8'))
        if ques19 == '4':
            DS3 = 1
        else:
            DS3 = 0




        ques20 = st.radio("20) In JavaScript, _________ is an object of the target language data type that encloses an object of the source language.", ('a wrapper', 'a link', 'a cursor', 'a form'))
        if ques20 == 'a wrapper':
            Web5 = 0
        else:
            Web5 = 1
        ques21 = st.radio("21) Which of the following is not a project factor that should be considered when planning the structure of software developing teams? ", ('The rigidity of the delivery date', 'The degree of sociability required for the project', 'High frustration caused by personal, business, or technological factors that causes friction among team members', 'The difficulty of the problem to be solved'))
        if ques21 == 'The degree of sociability required for the project':
            SE4 = 1
        else:
            SE4 = 0
        ques22 = st.radio("22) ................... algorithms enable the computers to learn from data, and even improve themselves, without being explicitly programmed.", ('Deep Learning', 'Machine Learning', 'Artificial Intelligence', 'All of the Above'))
        if ques22 == 'Machine Learning':
            ML4 = 1
        else:
            ML4 = 0

        ques23 = st.radio("23) The document listing all procedure and regulations that generally govern an organizations is the", ('Administrative policy manual', 'Personal policy book', 'Procedures log', 'Organization manual'))
        if ques23 == 'Organization manual':
            Insys4 = 1
        else:
            Insys4 = 0

        ques24 = st.radio("24) Which one of the following principles states that sometimes it is become more desirable to rescored the details of intrusion that to adopt more efficient measure to avoid it?", ('Least common mechanism', 'Compromise recording', 'Psychological acceptability', 'Work factor'))
        if ques24 == 'Compromise recording':
            Cyber4 = 1
        else:
            Cyber4 = 0
        ques25 = st.radio("25) In which of the following situations, you should NOT prefer Keras over TensorFlow?", ('When you want to quickly build a prototype using neural networks.', 'When you want to implement simple neural networks in your initial learning phase.', 'When you are doing critical and intensive research in any field.', 'When you want to create simple tutorials for your students and friends.'))
        if ques25 == 'When you are doing critical and intensive research in any field.':
            DS4 = 1
        else:
            DS4 = 0




        ques26 = st.radio("26) Do you have keen observation to test the quality of software?", ('Yes, I have', 'I have, but not sure', 'I don’t know', 'No, I haven’t'))
        if ques26 == 'Yes, I have':
            SE5 = 0
        else:
            SE5 = 1
        ques27 = st.radio("27) Do you like to process images, audios and videos for various tasks?", ('Yes, I like it', 'Yes, I do it in my free time', 'I rarely do it', 'No, I don’t like it'))
        if ques27 == 'Yes, I like it' or ques2 == 'Yes, I do it in my free time':
            ML5 = 1
        else:
            ML5 = 0
        ques28 = st.radio("28) Do you understand technically business and information technology both? ", ('Yes, I understand both', 'Little business, good information technology', 'Little information technology, good business', 'No, I don’t understand'))
        if ques28 == 'Yes, I understand both':
            Insys5 = 1
        else:
            Insys5 = 0

        ques29 = st.radio("29) Do you like to find insights from data for prediction and recommendation?", ('Yes, I like it', 'Yes, I do it in my free time', 'I rarely do it', 'No, I don’t like it'))
        if ques29 == 'Yes, I like it' or ques29 == 'Yes, I do it in my free time':
            DS5 = 1
        else:
            DS5 = 0

        ques30 = st.radio("30) Are you curious about digital forensics and intrusion detection?", ('Yes, I like it', 'Yes, I am keen about it after watching their magic in movies', 'I hear it just now', 'No, I don’t like it'))
        if ques30 == 'Yes, I like it':
            Cyber5 = 1
        else:
            Cyber5 = 0





        ques31 = st.radio("31) Which CSS property can provide to add an effect when changing from one style to another,without using Flash animations or javascript? ", ('Associations', 'Transitions', 'Transistor', 'None of the above'))
        if ques31 == 'Transitions':
            Web6 = 0
        else:
            Web6 = 1
        ques32 = st.radio("32) _________ is a software development life cycle model that is chosen if the development team has less experience on similar projects.", ('Iterative Enhancement Model', 'RAD', 'Spiral', 'Waterfall'))
        if ques32 == 'Spiral':
            SE6 = 1
        else:
            SE6 = 0
        ques33 = st.radio("33) Real-Time decisions, Game AI, Learning Tasks, Skill acquisition, and Robot Navigation are applications of ............. ", ('Reinforcement Learning', 'Supervised learning: Classification', 'Unsupervised learning: Regression', 'None of the above'))
        if ques33 == 'Reinforcement Learning':
            ML6 = 1
        else:
            ML6 = 0

        ques34 = st.radio("34) The main purpose of the system investigation phase is to produce a", ('Design report', 'Requirement report', 'Feasibility report', 'None of the above'))
        if ques34 == 'Feasibility report':
            Insys6 = 1
        else:
            Insys6 = 0

        ques35 = st.radio("35) Which type of the following malware does not replicate or clone them self's through infection? ", ('Rootkits', 'Trojans', 'Worms', 'Viruses'))
        if ques35 == 'Trojans':
            Cyber6 = 1
        else:
            Cyber6 = 0
        ques36 = st.radio("36) Which of the following is FALSE about Correlation and Covariance?", ('A zero correlation does not necessarily imply independence between variables.', 'Correlation and covariance values are the same.', 'The covariance and correlation are always the same sign.', 'Correlation is the standardized version of Covariance.'))
        if ques36 == 'Correlation and covariance values are the same.':
            DS6 = 1
        else:
            DS6 = 0



        result = ""

        # the below line ensures that when the button called 'Predict' is clicked,
        # the prediction function defined above is called to make the prediction
        # and store it in the variable result
        if st.button("Get Recommendation"):
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.03)
                progress.progress(i + 1)
            st.balloons()
            result = prediction(Web1, Cyber1, Web2, Insys1, SE1, DS1, ML1, Cyber2, Web3, SE2, ML2, Insys2, DS2, Web4, SE3, ML3, Insys3, Cyber3, DS3, Web5, SE4, ML4, Insys4, Cyber4, DS4, SE5, ML5, Insys5, DS5, Cyber5, Web6, SE6, ML6, Insys6, Cyber6, DS6)
            career_name = str()
            if result == 0:  # Above we have converted the field names into numerical form, so that we can apply the machine learning model easily. Now we have to again change the numerical values into names of field so that we can print it when required.
                career_name = 'Cyber Security'
            elif result == 1:
                career_name = 'Data Science'
            elif result == 2:
                career_name = 'Information System'
            elif result == 3:
                career_name = 'Machine Learning'
            elif result == 4:
                career_name = 'Software Engineering'
            else:
                career_name = 'Web Development'

            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            ds=0
            cy=0
            ml=0
            se=0
            web=0
            insy=0
            if career_name =='Cyber Security':
                cy=0.1
            elif career_name=='Data Science':
                ds=0.1
            elif career_name=='Information System':
                insy=0.1
            elif career_name=='Machine Learning':
                ml=0.1
            elif career_name=='Software Engineering':
                se=0.1
            else:
                web=0.1
            labels = 'Cyber Security', 'Data Science', 'Web Development', 'Machine Learning', 'Information System', 'Software Engineering'
            [mls, dss, ses, cys, webs, inss]=data_score(Web1, Cyber1, Web2, Insys1, SE1, DS1, ML1, Cyber2, Web3, SE2, ML2, Insys2, DS2, Web4, SE3, ML3, Insys3, Cyber3, DS3, Web5, SE4, ML4, Insys4, Cyber4, DS4, SE5, ML5, Insys5, DS5, Cyber5, Web6, SE6, ML6, Insys6, Cyber6, DS6)

            [persml, persds, persse, perscys, persweb, persins]=calulate_percentage(mls, dss, ses, cys, webs, inss)
            sizes = [perscys, persds, persweb, persml, persins, persse]
            explode = (cy, ds, insy, ml, se, web)  # only "explode" the 2nd slice (i.e. 'Hogs')




            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            st.pyplot(fig1)


    #Verifying the Recommendation Engine Recommendations

            highest_field_name=""
            highest_field_score = max(sizes)
            if (highest_field_score==perscys):
                highest_field_name='Cyber Security'
            elif (highest_field_score==persse):
                highest_field_name='Software Engineering'
            elif (highest_field_score==persds):
                highest_field_name='Data Science'
            elif (highest_field_score == persml):
                highest_field_name = 'Machine Learning'
            elif (highest_field_score == persins):
                highest_field_name = 'Information System'
            else:
                highest_field_name = 'Web Development'

            sizes.remove(highest_field_score)

            second_highest_field_name=""
            second_highest_field_score=max(sizes)

            if (second_highest_field_score==perscys):
                second_highest_field_name='Cyber Security'
            elif (second_highest_field_score==persse):
                second_highest_field_name='Software Engineering'
            elif (second_highest_field_score==persds):
                second_highest_field_name='Data Science'
            elif (second_highest_field_score == persml):
                second_highest_field_name = 'Machine Learning'
            elif (second_highest_field_score == persins):
                second_highest_field_name = 'Information System'
            elif (second_highest_field_score==persweb):
                second_highest_field_name = 'Web Development'





            reommendation_ok=False
            if(career_name==highest_field_name or career_name==second_highest_field_name):
                reommendation_ok=True
            else:
                career_name=highest_field_name
            st.balloons()

            st.success('We Recommend You To Choose {}'.format(career_name))
            st.balloons()


    if nav == "About":
        st.markdown(about, unsafe_allow_html=True)


if __name__ == '__main__':
    main()


# In[4]:





# In[ ]:




