
from audioop import add
from turtle import color
import streamlit as st

import pandas as pd
import numpy as np
import os



st.title("Nikko Tour Expense 2022")
st.sidebar.markdown("## Tour Member Info")
st.sidebar.text("name of the tour members")
members = st.sidebar.text_input('write down the names with a space')
members = members.lstrip()
members = members.rstrip()
members = members.split(" ")

st.sidebar.markdown('### members list')
df = pd.DataFrame(members,columns=['names'],index=np.arange(1,len(members)+1))
st.sidebar.table(df)
st.sidebar.markdown(members)

group_num = st.sidebar.number_input('how many groups you want?',min_value=1,step=1)
group_num = int(group_num)
groups = []
group_dict ={}
for i in range(group_num):
    gr_name = st.sidebar.text_input('group{}: name of the group'.format(i+1),key=i)
    gr_members = st.sidebar.multiselect('group members',members,key=i)
    group_dict[gr_name]=gr_members
st.sidebar.markdown(group_dict)

groups_or_names = list(group_dict.keys())
groups_or_names.extend(members)
# print(groups_or_names)




col1,col2,col3,col4,col5 = st.columns(5)
tname = col1.selectbox('name',members)
tmoney = col2.number_input('money',step=1)
tgr_or_name = col3.multiselect('groups or names',groups_or_names)
tcomment = col4.text_area('free space')
tadd = col5.button('ADD')
delLine = col5.number_input('which line you want to remove?',step=1)
tremove =  col5.button('remove a line')
ht = tname+' '+str(tmoney)+' '+','.join(tgr_or_name)+ ' #####>'+tcomment
st.markdown('**single command:**')
st.markdown('`'+ht+'`')

st.markdown('##### হিসাবের খাতা:')
if tadd == True:
    with open('check.txt','a') as f:
        f.writelines(ht+'\n')

if tremove == True:
    with open('check.txt','r') as f:
        data = f.readlines()
    data.pop(delLine)
    data_str = ''.join(data)
    with open('check.txt','w') as f:
        f.writelines(data_str)


if os.path.exists('check.txt'):
    with open('check.txt','r') as f:
        data = f.readlines()
        st.write(data)

############### math pandas ###############

ex_dict = {}
for i in members:
    ex_dict[i]=None

st.write(ex_dict)