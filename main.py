"""
home - 
Author: Alwin
Date:   2024/5/21
"""
import streamlit as st
import time

# 页面输出，可输出各种类型
st.write('Hello World!')

def mock_login(user,pwd):
    '''
    模拟登录,返回bool值
    :param user:登录用户名
    :param pwd: 登录密码
    :return: Bool
    '''
    time.sleep(4)
    return user == 'alwin' and pwd == '123'

user_name= st.text_input('请输入登录用户名：','alwin')
pass_word = st.text_input("请输入密码：",'123456')

if st.button('Login'):
    # 执行当前代码块的时候增加一个等待效果
    st.spinner('loading...')
    rst = mock_login(user_name,pass_word)
    # 简写if else
    tmp = '登录成功' if rst else '登录失败：用户名或密码错误'
    st.write(tmp)

# 嵌入streamlit官网首页视频
st.video('https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/hero-video.mp4')
# 嵌入图片
st.image('https://www.baidu.com/img/bd_logo1.png')