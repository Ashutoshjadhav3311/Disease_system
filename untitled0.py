import pandas as pd
import streamlit as st
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report,accuracy_score
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

df = pd.read_csv("Training.csv")

df.drop('Unnamed: 133', axis=1, inplace=True)

df['prognosis'].value_counts()

x = df.drop('prognosis', axis = 1)
y = df['prognosis']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42) 
tree = DecisionTreeClassifier()
tree.fit(x_train, y_train)
pred = tree.predict(x_test)
acc = tree.score(x_test, y_test) #test set accuracy

st.title('Disease Prediction system')  
    
itching=st.number_input('Itchining ?',key = "1")  
skin_rash=st.number_input('skin_rash?',key = "2")
nodal_skin_eruptions=st.number_input('nodal_skin_eruptions',key = "3")
continuous_sneezing=st.number_input('continuous_sneezing',key = "4")
shivering=st.number_input('shivering',key = "5")
chills=st.number_input('chills',key = "6")
joint_pain=st.number_input('joint_pain',key = "7")
stomach_pain=st.number_input('stomach_pain',key = "8")
acidity=st.number_input('acidity',key = "9")
ulcers_on_tongue=st.number_input('ulcers_on_tongue',key = "10")
muscle_wasting=st.number_input('muscle_wasting',key = "11")
vomiting=st.number_input('vomiting',key = "12")
burning_micturition=st.number_input('burning_micturition',key = "13")
spotting_urination=st.number_input('spotting_urination',key = "14")
fatigue=st.number_input('fatigue',key = "15")
weight_gain=st.number_input('weight_gain',key = "16")
anxiety=st.number_input('anxiety',key = "17")
cold_hands_and_feets=st.number_input('cold_hands_and_feets',key = "18")
mood_swings=st.number_input('mood_swings',key = "19")
weight_loss=st.number_input('weight_loss',key = "20")
restlessness=st.number_input('restlessness',key = "21")
lethargy=st.number_input('lethargy',key = "22")
patches_in_throat=st.number_input('patches_in_throat',key = "23")
irregular_sugar_level=st.number_input('irregular_sugar_level',key = "24")
cough=st.number_input('cough',key = "25")
high_fever=st.number_input('high_fever',key = "26")
sunken_eyes=st.number_input('sunken_eyes',key = "27")
breathlessness=st.number_input('breathlessness',key = "28")
sweating=st.number_input('sweating',key = "29")
dehydration=st.number_input('dehydration',key = "30")
indigestion=st.number_input('indigestion',key = "31")
headache=st.number_input('indigestion',key = "32")
yellowish_skin=st.number_input('yellowish_skin',key = "33")
dark_urine=st.number_input('dark_urine',key = "34")
nausea=st.number_input('nausea',key = "35")
loss_of_appetite=st.number_input('loss_of_appetite',key = "36")
pain_behind_the_eyes=st.number_input('pain_behind_the_eyes',key = "37")
back_pain=st.number_input('back_pain',key = "38")
constipation=st.number_input('constipation',key = "39")
abdominal_pain=st.number_input('abdominal_pain',key = "40")
diarrhoea=st.number_input('diarrhoea',key = "41")
mild_fever=st.number_input('mild_fever',key = "42")
yellow_urine=st.number_input('yellow_urine',key = "43")
yellowing_of_eyes=st.number_input('yellowing_of_eyes',key = "44")
acute_liver_failure=st.number_input('acute_liver_failure',key = "45")
fluid_overload=st.number_input('fluid_overload',key = "46")
swelling_of_stomach=st.number_input('swelling_of_stomach',key = "47")
swelled_lymph_nodes=st.number_input('swelled_lymph_nodes',key = "48")
malaise=st.number_input('malaise',key = "49")
blurred_and_distorted_vision=st.number_input('blurred_and_distorted_vision',key = "50")
phlegm=st.number_input('phlegm',key = "51")
throat_irritation=st.number_input('throat_irritation',key = "52")
redness_of_eyes=st.number_input('redness_of_eyes',key = "53")
sinus_pressure=st.number_input('sinus_pressure',key = "54")
runny_nose=st.number_input('runny_nose',key = "55")
congestion=st.number_input('congestion',key = "56")
chest_pain=st.number_input('chest_pain',key = "57")
weakness_in_limbs=st.number_input('weakness_in_limbs',key = "58")
fast_heart_rate=st.number_input('fast_heart_rate',key = "59")
pain_during_bowel_movements=st.number_input('pain_during_bowel_movements',key = "60")
pain_in_anal_region=st.number_input('pain_in_anal_region',key = "61")
bloody_stool=st.number_input('bloody_stool',key = "62")
irritation_in_anus=st.number_input('irritation_in_anus',key = "63")
neck_pain=st.number_input('neck_pain',key = "64")
dizziness=st.number_input('dizziness',key = "65")
cramps=st.number_input('cramps',key = "66")
bruising=st.number_input('bruising',key = "67")
obesity=st.number_input('obesity',key = "68")
swollen_legs=st.number_input('swollen_legs',key = "69")
swollen_blood_vessels=st.number_input('swollen_blood_vessels',key = "70")
puffy_face_and_eyes=st.number_input('puffy_face_and_eyes',key = "71")
enlarged_thyroid=st.number_input('enlarged_thyroid',key = "72")
brittle_nails=st.number_input('brittle_nails',key = "73")
swollen_extremeties=st.number_input('swollen_extremeties',key = "74")
excessive_hunger=st.number_input('excessive_hunger',key = "75")
extra_marital_contacts=st.number_input('extra_marital_contacts',key = "76")
drying_and_tingling_lips=st.number_input('drying_and_tingling_lips',key = "77")
slurred_speech=st.number_input('slurred_speech',key = "78")
knee_pain=st.number_input('knee_pain',key = "79")
hip_joint_pain=st.number_input('hip_joint_pain',key = "80")
muscle_weakness=st.number_input('muscle_weakness',key = "81")
stiff_neck=st.number_input('stiff_neck',key = "82")
swelling_joints=st.number_input('swelling_joints',key = "83")
movement_stiffness=st.number_input('movement_stiffness',key = "84")
spinning_movements=st.number_input('spinning_movements',key = "85")
loss_of_balance=st.number_input('loss_of_balance',key = "86")
unsteadiness=st.number_input('unsteadiness',key = "87")
weakness_of_one_body_side=st.number_input('weakness_of_one_body_side',key = "88")
loss_of_smell=st.number_input('loss_of_smell',key = "89")
bladder_discomfort=st.number_input('bladder_discomfort',key = "90")
foul_smell_of_urine=st.number_input('foul_smell_of_urine',key = "91")
continuous_feel_of_urine=st.number_input('continuous_feel_of_urine',key = "92")
passage_of_gases=st.number_input('passage_of_gases',key = "93")
internal_itching=st.number_input('internal_itching',key = "94")
toxic_look=st.number_input('toxic_look',key = "96")
depression=st.number_input('depression',key = "97")
irritability=st.number_input('irritability',key = "98")
muscle_pain=st.number_input('muscle_pain',key = "99")
altered_sensorium=st.number_input('altered_sensorium',key = "100")
red_spots_over_body=st.number_input('red spotson body' ,key = "101")
belly_pain=st.number_input('belly_pain' ,key = "102")
abnormal_menstruation=st.number_input('abnormal_menstruation',key = "103")
dischromic_patches=st.number_input('dischromic_patches',key = "104")
watering_from_eyes=st.number_input('watering_from_eyes',key = "105")
increased_appetite=st.number_input('increased_appetite',key = "106")
polyuria=st.number_input('polyuria',key = "1007")
family_history=st.number_input('family_history',key = "108")
mucoid_sputum=st.number_input('mucoid_sputum',key = "109")
rusty_sputum=st.number_input('rusty_sputum',key = "110")
lack_of_concentration=st.number_input('lack_of_concentration',key = "111")
visual_disturbances=st.number_input('visual_disturbances',key = "112")
receiving_blood_transfusion=st.number_input('receiving_blood_transfusion',key = "113")
receiving_unsterile_injections=st.number_input('receiving_unsterile_injections',key = "114")
coma=st.number_input('coma',key = "115")
stomach_bleeding=st.number_input('distention_of_abdomen',key = "116")
distention_of_abdomen=st.number_input('distention_of_abdomen',key = "117")
history_of_alcohol_consumption=st.number_input('history_of_alcohol_consumption',key = "118")
fluid_overload=st.number_input('fluid_overload',key = "119")
blood_in_sputum=st.number_input('blood_in_sputum',key = "120")
prominent_veins_on_calf=st.number_input('prominent_veins_on_calf',key = "121")
palpitations=st.number_input('palpitations',key = "122")
painful_walking=st.number_input('painful_walking',key = "123")
pus_filled_pimples=st.number_input('pus_filled_pimples',key = "124")
blackheads=st.number_input('blackheads',key = "125")
scurring=st.number_input('scurring',key = "126")
skin_peeling=st.number_input('skin_peeling',key = "127")
silver_like_dusting=st.number_input('silver_like_dusting',key = "128")
small_dents_in_nails=st.number_input('small_dents_in_nails',key = "129")
inflammatory_nails=st.number_input('inflammatory_nails',key = "130")
blister=st.number_input('blister',key = "131")
red_sore_around_nose=st.number_input('red_sore_around_nose',key = "132")
yellow_crust_ooze=st.number_input('yellow_crust_ooze',key = "133")


#print("Acurray on test set: {:.2f}%".format(acc*100))
x_user=[[itching,skin_rash,nodal_skin_eruptions,continuous_sneezing,shivering,chills,joint_pain,stomach_pain,acidity,ulcers_on_tongue,muscle_wasting,vomiting,burning_micturition,spotting_urination,fatigue,weight_gain,anxiety,cold_hands_and_feets,mood_swings,weight_loss,restlessness,lethargy,patches_in_throat,irregular_sugar_level,cough,high_fever,sunken_eyes,breathlessness,sweating,dehydration,indigestion,headache,yellowish_skin,dark_urine,nausea,loss_of_appetite,pain_behind_the_eyes,back_pain,constipation,abdominal_pain,diarrhoea,mild_fever,yellow_urine,yellowing_of_eyes,acute_liver_failure,fluid_overload,swelling_of_stomach,swelled_lymph_nodes,malaise,blurred_and_distorted_vision,phlegm,throat_irritation,redness_of_eyes,sinus_pressure,runny_nose,congestion,chest_pain,weakness_in_limbs,fast_heart_rate,pain_during_bowel_movements,pain_in_anal_region,bloody_stool,irritation_in_anus,neck_pain,dizziness,cramps,bruising,obesity,swollen_legs,swollen_blood_vessels,puffy_face_and_eyes,enlarged_thyroid,brittle_nails,swollen_extremeties,excessive_hunger,extra_marital_contacts,drying_and_tingling_lips,slurred_speech,knee_pain,hip_joint_pain,muscle_weakness,stiff_neck,swelling_joints,movement_stiffness,spinning_movements,loss_of_balance,unsteadiness,weakness_of_one_body_side,loss_of_smell,bladder_discomfort,foul_smell_of_urine,continuous_feel_of_urine,passage_of_gases,internal_itching,toxic_look,depression,irritability,muscle_pain,altered_sensorium,red_spots_over_body,belly_pain,abnormal_menstruation,dischromic_patches,watering_from_eyes,increased_appetite,polyuria,family_history,mucoid_sputum,rusty_sputum,lack_of_concentration,visual_disturbances,receiving_blood_transfusion,receiving_unsterile_injections,coma,stomach_bleeding,distention_of_abdomen,history_of_alcohol_consumption,fluid_overload,blood_in_sputum,prominent_veins_on_calf,palpitations,painful_walking,pus_filled_pimples,blackheads,scurring,skin_peeling,silver_like_dusting,small_dents_in_nails,inflammatory_nails,blister,red_sore_around_nose,yellow_crust_ooze]]
y_user=tree.predict(x_user)
    #code for prediction

    #creating a button for prediction
if st.button("Prediction result"):
    st.write("You have following disease")
    st.write(y_user)

st.text('Developed by Ahsutosh Jadhav')    
