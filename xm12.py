from ast import Div
from re import M
from this import d
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import pickle
from sklearn.ensemble import RandomForestRegressor

# 设置页面配置
st.set_page_config(
    page_title="学生成绩分析与预测系统",
    page_icon="📊",
    layout="wide"
)


def introduce_page():

    # 右边主内容区域
    st.title("📒学生成绩分析与预测系统")

    st.markdown('***')

    col11, col12 = st.columns(2)
    with col11:
        # 项目概述
        st.header("🗒️项目概述")
        st.write("本项目是一个基于streamit的学生成绩分析平台，通过数据可视化和机器学习技术，帮助教育工作省和学生深入了解学业表现，并预测期末考试成绩")

        # 主要特点
        st.subheader("✨主要特点")
        st.markdown("""
        - 📊**数据可视化**：直观展示学生成绩分布和趋势
        - 📚**智能预测**：基于历史数据预测学生未来成绩
        - 🧠**多维度分析**：从课程、时间、学生等多个维度进行分析
        - 💡**个性化建议**：根据分析结果提供个性化学习建议
        """)

    with col12:
        img_ua = [
            {'url':'img/1.png','text':'项目介绍'},
            {'url':'img/2.png','text':'专业数据分析'},
            {'url':'img/3.png','text':'专业数据分析'},
            {'url':'img/4.png','text':'专业数据分析'},
            {'url':'img/5.png','text':'专业数据分析'},
            {'url':'img/6.png','text':'成绩预测'},
        ]
        # 图片轮播展示区
        st.subheader("📷 项目截图展示")
        # 初始化 session_state 中的图片索引
        if "img_idx" not in st.session_state:
            st.session_state.img_idx = 0

        # 上一张/下一张按钮回调
        def next_img():
            st.session_state.img_idx = (st.session_state.img_idx + 1) % len(img_ua)

        def prev_img():
            st.session_state.img_idx = (st.session_state.img_idx - 1) % len(img_ua)

        # 当前图片信息
        current = img_ua[st.session_state.img_idx]
        img_path = current["url"]
        img_desc = current["text"]

        # 展示图片
        col_img, col_desc = st.columns([3, 1])
        with col_img:
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.warning(f"图片路径不存在：{img_path}")
        with col_desc:
            st.markdown(f"**{img_desc}**")
            st.markdown(f"第 {st.session_state.img_idx + 1} / {len(img_ua)} 张")

        # 上下一张按钮
        col_prev, _, col_next = st.columns([1, 3, 1])
        with col_prev:
            st.button("◀ 上一张", on_click=prev_img)
        with col_next:
            st.button("下一张 ▶", on_click=next_img)

    st.markdown('***')

    # 项目目标
    st.header("项目目标")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🎯 目标一")
        st.markdown("**分析影响因素**")
        st.markdown('''- 建立学生成绩数据库
- 实现数据的高效管理
- 支持多种数据导入格式  
            ''')

    with col2:
        st.markdown("### 📈 目标二")
        st.markdown("**可视化展示**")
        st.markdown('''- 开发成绩分析算法
- 实现多维度分析
- 生成可视化报告
            ''')

    with col3:
        st.markdown("### 🎓 目标三")
        st.markdown("**成绩预测**")
        st.markdown('''- 构建预测模型
- 提高预测准确性
- 提供个性化建议''')

    st.markdown('***')

    # 技术架构
    st.header("技术架构")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("**前端框架**")
        st.code("""Streamlit""")

    with col2:
        st.markdown("**数据处理**")
        st.code("""Pandas
Numpy""")

    with col3:
        st.markdown("**可视化**")
        st.code("""Plotly
Matplotlib""")

    with col4:
        st.markdown("**机器学习**")
        st.code("""Scikit-learn""")

    # 页脚
    st.markdown("---")
    st.markdown("© 2025 学生成绩分析与预测系统 | 技术支持：Streamlit团队 | 参与人员：PLY，SFY")

def data_analysis_page():
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    
    # 获取当前文件所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, 'student_data_adjusted_rounded.csv')
    # 读取数据
    df = pd.read_csv(data_path)
    
    # 1. 使用表格展示各专业每周平均学时、期中考试平均分和期末考试平均分
    st.title("📊 专业数据分析")
    st.header("1. 各专业男女性别比例")

    # 创建两列布局：左侧图表，右侧数据表格
    col21, col22 = st.columns(2)
    
    with col21:
        # 2. 使用双层柱状图展示每个专业的男女性别比例
        # 按专业和性别分组计数
        gender_counts = df.groupby(['专业', '性别']).size().unstack(fill_value=0)
        # 创建柱状图
        fig, ax = plt.subplots(figsize=(16, 9))
        gender_counts.plot(kind='bar', stacked=False, ax=ax, color=['#1f77b4', '#ff7f0e'])
        ax.set_xlabel('专业')
        ax.set_ylabel('人数')
        ax.set_title('各专业男女性别比例', loc='left')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
        
    with col22:
        st.subheader("性别比例数据")
        st.dataframe(gender_counts.T,width=1000)

    #第二部分
    st.header("2. 各专业学习指标对比")
    # 按专业分组计算平均值
    major_stats = df.groupby('专业').agg({
        '每周学习时长（小时）': 'mean',
        '期中考试分数': 'mean',
        '期末考试分数': 'mean'
    }).reset_index()
    # 重命名列名
    major_stats.columns = ['专业', '每周平均学时', '期中考试平均分', '期末考试平均分']

    col_21, col_22 = st.columns(2)

    with col_21:
        # 创建组合图表：左侧柱状图展示平均学习时间，右侧折线图展示成绩
        fig, ax1 = plt.subplots(figsize=(16, 9))
        
        # 绘制平均学习时间柱状图（左侧Y轴）
        bar_width = 0.8
        bars = ax1.bar(major_stats['专业'], major_stats['每周平均学时'], color='#87CEFA', width=bar_width)
        ax1.set_xlabel('专业')
        ax1.set_ylabel('平均学习时间（小时）', color='#000000')
        ax1.tick_params(axis='y', labelcolor='#000000')
        
        # 创建右侧Y轴用于绘制成绩折线图
        ax2 = ax1.twinx()
        
        # 绘制期中考试和期末考试成绩折线图（右侧Y轴）
        line1, = ax2.plot(major_stats['专业'], major_stats['期中考试平均分'], color='#FFA500', marker='o', label='平均期中成绩',)
        line2, = ax2.plot(major_stats['专业'], major_stats['期末考试平均分'], color='#008000', marker='o', label='平均期末成绩',)
        ax2.set_ylabel('平均分数', color='#000000')
        ax2.tick_params(axis='y', labelcolor='#000000')
        
        # 设置图表标题
        ax1.set_title('各专业平均学习时间与成绩对比')
        
        # 创建一个代理艺术家来表示平均学习时间柱状图
        from matplotlib.patches import Rectangle
        bar_proxy = Rectangle((0, 0), 1, 1, color='#87CEFA', label='平均学习时间')
        
        # 设置图例：将其放在图表的左上角
        ax1.legend(handles=[bar_proxy, line1, line2], 
                  labels=['平均学习时间', '平均期中成绩', '平均期末成绩'],
                  loc='upper left',
                  bbox_to_anchor=(0, 1.2),
                  frameon=False)
        # 设置X轴刻度旋转
        plt.xticks(rotation=45)
        # 调整布局
        plt.tight_layout()
        # 显示图表
        st.pyplot(fig)

    with col_22:
        # 显示详细数据表格
        st.subheader("详细数据")
        st.dataframe(major_stats, width=800)

    # 3. 各专业出勤率分析
    st.header("3. 各专业出勤率分析")
    # 按专业分组计算平均出勤率
    attendance_stats = df.groupby('专业')['上课出勤率'].mean().reset_index()
    
    # 创建两列布局：左侧图表，右侧排名表
    col_23, col_24 = st.columns(2)
    
    with col_23:
        # 创建柱状图
        fig, ax = plt.subplots(figsize=(16, 9))
        
        # 生成渐变色
        cmap = plt.cm.viridis
        norm = plt.Normalize(attendance_stats['上课出勤率'].min(), attendance_stats['上课出勤率'].max())
        colors = [cmap(norm(val)) for val in attendance_stats['上课出勤率']]
        
        # 绘制柱状图
        bars = ax.bar(attendance_stats['专业'], attendance_stats['上课出勤率'], color=colors)
        
        # 添加百分比标签
        for bar, val in zip(bars, attendance_stats['上课出勤率']):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{val:.1f}%', 
                    ha='center', va='bottom', color='white', fontweight='bold')
        
        # 设置图表属性
        ax.set_xlabel('专业',)
        ax.set_ylabel('出勤率 (%)')
        ax.set_title('各专业出勤率对比',loc='left')
        plt.xticks(rotation=45)
        
        # 添加颜色渐变图例
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
        sm.set_array([])
        cbar = fig.colorbar(sm, ax=ax, orientation='vertical', pad=0.02)
        cbar.set_label('出勤率 (%)')
        
        plt.tight_layout()
        st.pyplot(fig)
    
    with col_24:
        # 显示排名表
        st.subheader("出勤率排名")
        # 排序出勤率数据
        attendance_sorted = attendance_stats.sort_values('上课出勤率', ascending=False).reset_index(drop=True)
        # 重新排列列顺序
        attendance_sorted = attendance_sorted[[ '专业', '上课出勤率']]
        # 显示数据框
        st.dataframe(attendance_sorted, width=800)

    # 4. 大数据管理专业专项分析
    st.header("4. 大数据管理专业专项分析")
    # 筛选大数据管理专业
    big_data_major = df[df['专业'] == '大数据管理']
    
    # 计算各项指标
    avg_attendance = big_data_major['上课出勤率'].mean()
    avg_final_score = big_data_major['期末考试分数'].mean()
    pass_rate = (big_data_major['期末考试分数'] >= 60).mean() * 100
    avg_study_time = big_data_major['每周学习时长（小时）'].mean()
    
    # 创建四列布局展示四个指标
    col_41, col_42, col_43, col_44 = st.columns(4)
    
    with col_41:
        st.markdown("**平均出勤率**")   
        st.markdown(f"## {avg_attendance:.1f}%")
    
    with col_42:
        st.markdown("**平均期末成绩**")   
        st.markdown(f"## {avg_final_score:.1f}分")
    
    with col_43:
        st.markdown("**及格率**")   
        st.markdown(f"## {pass_rate:.1f}%")
    
    with col_44:
        st.markdown("**平均学习时间**")   
        st.markdown(f"## {avg_study_time:.1f}小时")
     
    fig, ax = plt.subplots(figsize=(12, 6), facecolor='#000000')

    # 绘制直方图
    n, bins, patches = ax.hist(big_data_major['期末考试分数'], bins=15, color='#4CAF50', alpha=0.8)
    
    # 设置坐标轴颜色为白色
    ax.spines['bottom'].set_color('#ffffff')
    ax.spines['top'].set_color('#ffffff')
    ax.spines['left'].set_color('#ffffff')
    ax.spines['right'].set_color('#ffffff')
    
    # 设置坐标轴标签和刻度颜色为白色
    ax.set_xlabel('期末考试分数', color='#ffffff', fontsize=12)
    ax.set_ylabel('人数', color='#ffffff', fontsize=12)
    ax.tick_params(axis='x', colors='#ffffff')
    ax.tick_params(axis='y', colors='#ffffff')
    
    # 设置标题颜色为白色
    ax.set_title('大数据管理专业期末考试成绩分布', color='#ffffff', fontsize=14, loc='center')
    
    plt.tight_layout()
    st.pyplot(fig)

def predict_page():
    st.markdown("## 🎲期末成绩预测")
    st.markdown("***")
    st.markdown("根据输入的学习数据，预测期末成绩")
    
    # 获取当前文件所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, 'student_data_adjusted_rounded.csv')
    # 读取数据
    df = pd.read_csv(data_path)
    
    # 数据预处理：将性别和专业转换为数值型特征
    df_encoded = pd.get_dummies(df, columns=['性别', '专业'])
    
    # 定义特征和目标变量（用于获取特征列名）
    X = df_encoded.drop(['期末考试分数'], axis=1)
    
    # 加载预训练模型
    model_path = os.path.join(current_dir, 'student_data_adjusted_rounded.pkl')
    with open(model_path, 'rb') as f:
        model = pickle.load(f)     
    
    # 用户输入表单
    st.markdown("### 请输入学生信息")
    
    # 创建表单容器
    with st.form("prediction_form"):
        col3_1, co3_2 = st.columns(2)
        
        with col3_1:
            student_id = st.text_input("学号")
            gender = st.selectbox("性别", options=['男', '女'])
            major = st.selectbox("专业", options=df['专业'].unique())
            
        with co3_2:
            weekly_study_time = st.slider('每周学习时长（小时）',0.00, 40.00)

            attendance_rate = st.slider('上课出勤率',0.0, 1.0)

            midterm_score = st.slider('期中考试分数',0.00, 100.00)
            
            homework_completion = st.slider('作业完成率',0.0, 1.0)
        
        # 提交按钮
        submit_button = st.form_submit_button("开始预测")
    
    if submit_button:
        # 输入验证
        if not student_id:
            st.error("请输入学号")
            return
        
        try:
            student_id_int = int(student_id)
        except ValueError:
            st.error("请输入有效的学号数字")
            return
        
        # 处理用户输入
        # 创建用户输入的特征向量
        user_input = {
            '学号': student_id_int,  # 使用验证后的学号整数
            '每周学习时长（小时）': weekly_study_time,
            '上课出勤率': attendance_rate,
            '期中考试分数': midterm_score,
            '作业完成率': homework_completion
        }
        
        # 处理性别
        for gender_col in X.columns:
            if gender_col.startswith('性别_'):
                user_input[gender_col] = 1 if gender_col == f'性别_{gender}' else 0
        
        # 处理专业
        for major_col in X.columns:
            if major_col.startswith('专业_'):
                user_input[major_col] = 1 if major_col == f'专业_{major}' else 0
        
        # 转换为DataFrame
        user_df = pd.DataFrame([user_input], columns=X.columns)
        
        # 进行预测
        prediction = model.predict(user_df)
        predicted_score = prediction[0]
        
        # 显示预测结果
        st.markdown("### 📊预测结果")

        st.markdown(f"**预测的期末成绩：** {predicted_score:.2f}")
        
        # 显示进度条
        st.progress(min(predicted_score / 100, 1.0))
        # 根据预测结果显示不同的图片
        if predicted_score >= 60:
            st.markdown("## 🎉 恭喜！预测您的期末考试将及格！")
            # 使用emoji作为图片替代，实际应用中可以替换为真实图片
            st.markdown("<div style='font-size: 100px;'>🎊</div>", unsafe_allow_html=True)
        else:
            st.markdown("## 💪 加油！再努力一下就能及格了！")
            # 使用emoji作为图片替代，实际应用中可以替换为真实图片
            st.markdown("<div style='font-size: 100px;'>📚</div>", unsafe_allow_html=True)

 # 左边导航栏
nav = st.sidebar.radio("导航", ["项目介绍", "专业数据分析", "成绩预测"])

if nav == "项目介绍":
    introduce_page()
elif nav == "专业数据分析":
    data_analysis_page()
elif nav == "成绩预测":
    predict_page()