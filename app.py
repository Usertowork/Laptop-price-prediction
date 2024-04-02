import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('pipe_laptop.pkl', 'rb'))
#dt = pickle.load(open('dataset_laptop_final.pkl', 'rb'))

try:
    with open('dataset_laptop_final.pkl', 'rb') as file:
        dt = pickle.load(file)
except Exception as e:
    print("An error occurred while loading the pickle file:", e)

st.title("Laptop Price Predictor ")

#brandpi
company = st.selectbox('Brand', dt['Company'].unique())

#Type of laptop
type = st.selectbox('Type of Laptop ', dt['TypeName'].unique())

#Size of Screen
Screen_size = st.number_input('Screen Size')

#RAM
ram = st.selectbox('RAM(in GB)', dt['Ram'].unique())

#OPS
# opsys = st.selectbox('Operating System', st['OpSys'].unique())
opsys = st.selectbox('Operating System', ['macOS', 'No OS', 'Windows 10', 'Mac OS X', 'Linux', 'Windows 10 S', 'Chrome OS', 'Windows 7'])

# Weight
weight = st.number_input('Weight of the laptop ')

#TouchScreen
touch = st.selectbox('TouchScreen', ['Yes', 'No'])

#IPS
ips = st.selectbox('IPS', ['Yes', 'No'])

# Cpu brand
cpu_brand = st.selectbox("CPU Brand", dt['Cpu brand'].unique())

# Gpu brand
gpu_brand = st.selectbox("GPU Brand", dt['Gpu Brand'].unique())

#HDD
hdd = st.selectbox('HDD(in GB)', dt['HDD'].unique())

#SSD
ssd = st.selectbox('SSD(in GB)', dt['SSD'].unique())

#Display type
disp_4k = st.selectbox('4K Display', ['Yes', 'No'])
disp_full_HD = st.selectbox('Full HD display', ['Yes', 'No'])
disp_Quad_HD = st.selectbox('Quad HD display', ['Yes', 'No'])

#Resolution
resolution = st.selectbox('Resolution ', ['1366x768', '1600x900', '1920x1080', '2560x1600', '2560x1440', '3860x2160', '3200x1800', '2880x1800'])

if st.button('Predict Price'):
    ppi = None
    if touch == 'Yes':
        touch = 1
    else:
        touch = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    if disp_4k == 'Yes':
        disp_4k = 1
    else:
        disp_4k = 0

    if disp_full_HD == 'Yes':
        disp_full_HD = 1
    else:
        disp_full_HD = 0

    if disp_Quad_HD == 'Yes':
        disp_Quad_HD = 1
    else:
        disp_Quad_HD = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2)**0.5)/Screen_size

    query = np.array([company, type, ram, opsys, weight, ips, touch, disp_4k, disp_full_HD, disp_Quad_HD, ppi, hdd, ssd, cpu_brand, gpu_brand])

    query = query.reshape(1, 15)

    st.title(int(np.exp(pipe.predict(query)[0])))

