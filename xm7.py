import streamlit as st
from datetime import datetime, time

st.set_page_config(page_title='个人简历生成器',layout='wide')

st.title('个人简历生成器')
st.text('使用Streamlit创建您的个性化简历')
st.header('个人信息表单')


# 修复列宽参数警告
c1,c2 = st.columns([1,3])

with c1:
    st.markdown('***')
    user_name = st.text_input('姓名')
    user_position = st.text_input('职位')
    user_phone= st.text_input('电话')
    user_email= st.text_input('邮箱')
    user_data = st.date_input("选择一个日期", value=None)
    user_gender = st.radio('性别：',['男', '女', '其他'],horizontal=True)
    user_xueli = st.selectbox('学历：',['小学','初中','高中','大学','研究生','硕士','博士'])
    user_yynl = st.multiselect('语言能力：',['中文','英文','韩文','日文','俄语'])
    user_skill = st.multiselect('技能（可多选）：',['java','HTML/CSS','机器学习','Python','C++','小程序开学与应用'])
    user_age = st.slider('工作经验（年）', 0, 30, 4)
    values = st.slider('期望薪资范围（元）',10000, 80000, (15000, 30000))
    user_time = st.time_input("最佳联系时间：")
    user_resume = st.text_area('个人简历')
    user_img = st.file_uploader("上传个人照片", type=["jpg", "jpeg", "png"])
    


with c2:
    st.markdown('***')
    c21,c22 = st.columns([2,2])
    
    with c21:
        st.title(f'姓名：{user_name}')
        if user_img is not None:
            st.image(user_img, caption='个人照片', width=200)
        st.text(f'职位：{user_position}')
        st.text(f'电话：{user_phone}')
        st.text(f'邮箱：{user_email}')
        st.text(f"出生日期：{user_data}")
        

    with c22:
        st.text(f'性别：{user_gender}')
        st.text(f'学历：{user_xueli}')
        yynl_text = ', '.join(user_yynl) if user_yynl else '未填写'
        st.markdown('语言能力：' + yynl_text)
        st.markdown(f'工作经验：{user_age}年')
        st.markdown(f'期望薪资：{values[0]}-{values[1]}元')

    st.markdown('***')
    st.title('个人简历')
    st.markdown(f'{user_resume}')
    st.markdown('专业技能')
    skill_text = ', '.join(user_skill) if user_skill else '未填写'
    st.markdown(skill_text)
