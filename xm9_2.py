import pandas as pd
import streamlit as st

st.set_page_config(page_title="销售仪表板", page_icon="📊", layout="wide")

def get_dataframe_from_excel():
    df = pd.read_excel('supermarket_sales.xlsx',
        sheet_name='销售数据',
        skiprows=1,
        index_col='订单号',
    )
    df['小时数'] = pd.to_datetime(df['时间'],format='%H:%M:%S').dt.hour
    return df

def add_sidebar_func(df):
    with st.sidebar:
        st.header("筛选选项:")
        city_unique = df['城市'].unique()
        city = st.multiselect(
            "选择城市:",
            options=city_unique,
            default=city_unique,
        )

        customer_type_unique = df['顾客类型'].unique()
        customer_type = st.multiselect(
            "选择客户类型:",
            options=customer_type_unique,
            default=customer_type_unique,
        )

        gender_unique = df['性别'].unique()
        gender = st.multiselect(
            "选择性别:",
            options=gender_unique,
            default=gender_unique,
        )

        df_selection = df.query(
            "城市 == @city & 顾客类型 == @customer_type & 性别 == @gender"
        )
        return df_selection

sale_df = get_dataframe_from_excel()
df_selection = add_sidebar_func(sale_df)

# 计算关键指标
total_sales = df_selection['总价'].sum()
avg_rating = df_selection['评分'].mean()
avg_order_value = df_selection['总价'].mean()

# 创建仪表盘布局
st.header("📊 销售仪表板")

# 关键指标卡片
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 总销售额:")
    st.markdown(f"**RMB ¥{total_sales:,.0f}**")
with col2:
    st.markdown("### 顾客评分的平均值:")
    st.markdown(f"**{avg_rating:.1f} {'👍️' * int(round(avg_rating))}**")
with col3:
    st.markdown("### 每单的平均销售额:")
    st.markdown(f"**RMB ¥{avg_order_value:,.2f}**")

# 图表并排显示
chart_col1, chart_col2 = st.columns(2)

# 按小时数划分的销售额
with chart_col1:
    st.markdown("### 按小时数划分的销售额")
    hourly_sales = df_selection.groupby('小时数')['总价'].sum().reset_index()
    st.bar_chart(hourly_sales.set_index('小时数'))

# 按产品类型划分的销售额
with chart_col2:
    st.markdown("### 按产品类型划分的销售额")
    product_sales = df_selection.groupby('产品类型')['总价'].sum().reset_index()
    st.bar_chart(product_sales.set_index('产品类型'))
