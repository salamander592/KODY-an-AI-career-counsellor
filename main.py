import numpy as np
import pandas as pd
#import preprocessor as p
import counselor
from tensorflow.keras.models import load_model
import joblib
from pathlib import Path

def main():

    lem = WordNetLemmatizer()
    n=1
    def tokenizer(x):
        tokens = x.split()
        rep = re.compile('[%s]' % re.escape(string.punctuation))
        tokens = [rep.sub('', i) for i in tokens]
        tokens = [i for i in tokens if i.isalpha()]
        tokens = [lem.lemmatize(i.lower()) for i in tokens]
        tokens = [i.lower() for i in tokens if len(i) > 1]
        return tokens

    def no_stop_inp(tokenizer,df,c):
        no_stop = []
        x = df[c][0]
        tokens = tokenizer(x)
        no_stop.append(' '.join(tokens))
        df[c] = no_stop
        return df

    def inpenc(tok,df,c):
        t = tok
        x = x = [df[c][0]]
        enc = t.texts_to_sequences(x)
        padded = pad_sequences(enc, maxlen=16, padding='post')
        return padded

    def predinp(model,x):
        pred = np.argmax(model.predict(x))
        return pred

    def botp(df3,pred):
        l = df3.user[0].split()
        if len([i for i in l if i in words])==0 :
            pred = 1
        return pred

    def botop(df2,pred):
        x2 = df2.groupby('labels').get_group(pred).shape[0]
        idx1 = np.random.randint(0,x2)
        op = list(df2.groupby('labels').get_group(pred).bot)
        return op[idx1]

    def botans(df3):
        tok = joblib.load('tokenizer_t.pkl')
        word = joblib.load('words.pkl')
        df3 = no_stop_inp(tokenizer, df3, 'user')
        inp = inpenc(tok, df3, 'user')
        pred = predinp(model, inp)
        pred = botp(df3, pred)
        ans = botop(df2, pred)
        return ans

    def get_text():
        x = st.text_input("You : ")
        x=x.lower()
        xx = x[:13]
        if(xx =="start my test"):
            global flag
            flag=0
        input_text  = [x]
        df_input = pd.DataFrame(input_text,columns=['user'])
        return df_input

    #flag=1
    qvals = {"Select an Option": 0, "Strongly Agree": 5, "Agree": 4, "Neutral": 3, "Disagree": 2,
             "Strongly Disagree": 1}
    st.title("CounselBot")
    banner=Image.open("img/21.png")
    st.image(banner, use_column_width=True)
    st.write("Hi! I'm CounselBot, your personal career counseling bot. Ask your queries in the text box below and hit enter. If and when you are ready to take our personality test, type \"start my test\" and you're good to go!")

    df3 = get_text()
    if (df3.loc[0, 'user']==""):
        ans = "Hi, I'm CounselBot. \nHow can I help you?"

    elif(flag==0):
        ans = "Sure, good luck!"
    else:
        ans = botans(df3)

    st.text_area("CounselBot:", value=ans, height=100, max_chars=None)

    if(flag==0):
        
        st.title("PERSONALITY TEST:")
        kr = st.selectbox("Would you like to begin with the test?", ["Select an Option", "Yes", "No"])
        if (kr == "Yes"):
            kr1 = st.selectbox("Select level of education",
                               ["Select an Option", "Grade 10", "Grade 12", "Undergraduate"])

            #####################################  GRADE 10  ###########################################

            if(kr1=="Grade 10"):
                lis = []
                if (kr == "Yes"):
                    st.header("Question 1")
                    st.write("I find writing programs for computer applications interesting")
                    n = imagify.imageify(n)
                    inp = st.selectbox("",
                                       ["Select an Option", "Strongly Agree", "Agree", "Neutral", "Disagree",
                                        "Strongly Disagree"],
                                       key='1')
                    if ((inp != "Select an Option")):
                        lis.append(qvals[inp])
                        st.header("Question 2")
                        st.write("I can understand mathematical problems with ease")
                        n = imagify.imageify(n)
                        inp2 = st.selectbox("", ["Select an Option", "Strongly Agree", "Agree", "Neutral", "Disagree",
                                                 "Strongly Disagree"], key='2')

                        if (inp2 != "Select an Option"):
                            lis.append(qvals[inp2])
                            st.header("Question 3")
                            st.write("Learning about the existence of individual chemical components is interesting")
                            n = imagify.imageify(n)
                            inp3 = st.selectbox("", ["Select an Option", "Strongly Agree", "Agree", "Neutral", "Disagree",
                                                     "Strongly Disagree"], key='3')
                            if (inp3 != "Select an Option"):
                                lis.append(qvals[inp3])
                                st.header("Question 4")
                                st.write("The way plants and animals thrive gets me curious")
                                n = imagify.imageify(n)
                                inp4 = st.selectbox("",
                                                    ["Select an Option", "Strongly Agree", "Agree", "Neutral", "Disagree",
                                                     "Strongly Disagree"], key='4')
                                if (inp4 != "Select an Option"):
                                    lis.append(qvals[inp4])
                                    st.header("Question 5")
                                    st.write("Studying about the way fundamental constituents of the universe interact with each other is fascinating")
                                    n = imagify.imageify(n)
                                    inp5 = st.selectbox("",
                                                        ["Select an Option", "Strongly Agree", "Agree", "Neutral",
                                                         "Disagree",
                                                         "Strongly Disagree"], key='5')
                                    if (inp5 != "Select an Option"):
                                        lis.append(qvals[inp5])
                                        st.header("Question 6")
                                        st.write(
                                            "Accounting and business management is my cup of tea")
                                        n = imagify.imageify(n)
                                        inp6 = st.selectbox("",
                                                            ["Select an Option", "Strongly Agree", "Agree", "Neutral",
                                                             "Disagree",
                                                             "Strongly Disagree"], key='6')
                                        if (inp6 != "Select an Option"):
                                            lis.append(qvals[inp6])
                                            st.header("Question 7")
                                            st.write(
                                                "I would like to know more about human behaviour, relations and patterns of thinking")
                                            n = imagify.imageify(n)
                                            inp7 = st.selectbox("",
                                                                ["Select an Option", "Strongly Agree", "Agree", "Neutral",
                                                                 "Disagree",
                                                                 "Strongly Disagree"], key='7')
                                            if (inp7 != "Select an Option"):
                                                lis.append(qvals[inp7])
                                                st.header("Question 8")
                                                st.write(
                                                    "I find the need to be aware of stories from the past.")
                                                n = imagify.imageify(n)
                                                inp8 = st.selectbox("",
                                                                    ["Select an Option", "Strongly Agree", "Agree",
                                                                     "Neutral",
                                                                     "Disagree",
                                                                     "Strongly Disagree"], key='8')
                                                if (inp8 != "Select an Option"):
                                                    lis.append(qvals[inp8])
                                                    st.header("Question 9")
                                                    st.write(
                                                        "I see myself as a sportsperson/professional trainer")
                                                    n = imagify.imageify(n)
                                                    inp9 = st.selectbox("",
                                                                        ["Select an Option", "Strongly Agree", "Agree",
                                                                         "Neutral",
                                                                         "Disagree",
                                                                         "Strongly Disagree"], key='9')
                                                    if (inp9 != "Select an Option"):
                                                        lis.append(qvals[inp9])
                                                        st.header("Question 10")
                                                        st.write(
                                                            "I enjoy creating works of art")
                                                        n = imagify.imageify(n)
                                                        inp10 = st.selectbox("",
                                                                             ["Select an Option", "Strongly Agree", "Agree",
                                                                              "Neutral",
                                                                              "Disagree",
                                                                              "Strongly Disagree"], key='10')
                                                        if (inp10 != "Select an Option"):
                                                            lis.append(qvals[inp10])
                                                            st.success("Test Completed")
                                                            #st.write(lis)
                                                            st.title("RESULTS:")
                                                            df = pd.read_csv(r"Subjects.csv")

                                                            input_list = lis

                                                            subjects = {1: "Computers",
                                                                        2: "Mathematics",
                                                                        3: "Chemistry",
                                                                        4: "Biology",
                                                                        5: "Physics",
                                                                        6: "Commerce",
                                                                        7: "Psychology",
                                                                        8: "History",
                                                                        9: "Physical Education",
                                                                        10: "Design"}

                                                            def output(listofanswers):
                                                                class my_dictionary(dict):
                                                                    def __init__(self):
                                                                        self = dict()

                                                                    def add(self, key, value):
                                                                        self[key] = value

                                                                ques = my_dictionary()

                                                                for i in range(0, 10):
                                                                    ques.add(i, input_list[i])

                                                                all_scores = []

                                                                for i in range(9):
                                                                    all_scores.append(ques[i] / 5)

                                                                li = []

                                                                for i in range(len(all_scores)):
                                                                    li.append([all_scores[i], i])
                                                                li.sort(reverse=True)
                                                                sort_index = []
                                                                for x in li:
                                                                    sort_index.append(x[1] + 1)
                                                                all_scores.sort(reverse=True)

                                                                a = sort_index[0:5]
                                                                b = all_scores[0:5]
                                                                s = sum(b)
                                                                d = list(map(lambda x: x * (100 / s), b))

                                                                return a, d

                                                            l, data = output(input_list)

                                                            out = []
                                                            for i in range(0, 5):
                                                                n = l[i]
                                                                c = subjects[n]
                                                                out.append(c)

                                                            output_file("pie.html")

                                                            graph = figure(title="Recommended subjects", height=500,
                                                                           width=500)
                                                            radians = [math.radians((percent / 100) * 360) for percent
                                                                       in data]

                                                            start_angle = [math.radians(0)]
                                                            prev = start_angle[0]
                                                            for i in radians[:-1]:
                                                                start_angle.append(i + prev)
                                                                prev = i + prev

                                                            end_angle = start_angle[1:] + [math.radians(0)]

                                                            x = 0
                                                            y = 0

                                                            radius = 0.8

                                                            color = Greens[len(out)]
                                                            graph.xgrid.visible = False
                                                            graph.ygrid.visible = False
                                                            graph.xaxis.visible = False
                                                            graph.yaxis.visible = False

                                                            for i in range(len(out)):
                                                                graph.wedge(x, y, radius,
                                                                            start_angle=start_angle[i],
                                                                            end_angle=end_angle[i],
                                                                            color=color[i],
                                                                            legend_label=out[i] + "-" + str(
                                                          
                                                           

                                                            def Convert(string):
                                                                li = list(string.split(","))
                                                                li = list(map(float, li))
                                                                return li

                                                            x = ['2000', '2005', '2010', '2015', '2020']
                                                            y = []
                                                            for i in range(0, 5):
                                                                t = Convert(df['trends'][int(l[i]) - 1])
                                                                y.append(t)
                                                            output_file("line.html")
                                                         


                                                            for i in range(0, 5):
                                                                st.subheader(subjects[int(l[i])])
                                                                xl=(df['contacts'][int(l[i]) - 1]).split(",")
                                                                for k in xl:
                                                                    ml=list(k.split(","))
                                                                    for kk in ml:
                                                                        st.write(kk,sep="\n")




if __name__=="__main__":
    main()