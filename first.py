import streamlit as st    # 导入Streamlit并用st代表它


st.title("伞兵一号申请起飞")
st.text("HELLO WORLD!")

# 第一个标题展示元素，有工具提示
st.title("第二章文本类数据展示",help="标签提示")

# 第二个章节文本展示元素，无工具提示
st.header("这是一个章节展示元素")

# 第三个子章节文本展示元素，无工具提示
st.subheader("这是一个子章节展示元素")

# 第四个普通文本展示元素，无工具提示
st.text("这是普通文本展示元素")


python_code='''print("Hello Word！")
a=1
b=2
print(a+b)
'''

#普通文本展示
st.text(python_code)

#淡灰色文本注释文本
st.caption("这是一段Python代码")
#python代码块展示
st.caption(python_code, unsafe_allow_html=True)
st.code(python_code)