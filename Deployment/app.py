import streamlit as st
import pickle as pk
import pandas as pd
import numpy as np

# Thiết lập cấu hình trang
st.set_page_config(
    page_title="Ứng Dụng Dự Đoán Khoản Vay",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Sử dụng caching để tải mô hình và scaler một lần
@st.cache_resource
def load_model_and_scaler():
    # Đường dẫn đến tệp mô hình và scaler
    model_path = '/Users/admin/OneDrive - VNU-HCMUS/Desktop/Pattern Recognition/PRML2024_Midterm_Group18/Deployment/loan_classifier_model.pkl'
    scaler_path = '/Users/admin/OneDrive - VNU-HCMUS/Desktop/Pattern Recognition/PRML2024_Midterm_Group18/Deployment/scaler.pkl'
    try:
        # Tải scaler từ tệp pickle
        with open(scaler_path, 'rb') as file:
            scaler = pk.load(file)
        # Tải mô hình từ tệp pickle
        with open(model_path, 'rb') as file:
            model = pk.load(file)
        return model, scaler
    except FileNotFoundError as e:
        # Hiển thị lỗi nếu không tìm thấy tệp
        st.error(f"Lỗi khi tải mô hình hoặc scaler: {e}")
        st.stop()

# Tải mô hình và scaler đã huấn luyện
model, scaler = load_model_and_scaler()

# Hàm dự đoán
def prediction(model, scaler, input_data):
    """
    Hàm thực hiện dự đoán phê duyệt khoản vay.
    
    Parameters:
    - model: Mô hình đã huấn luyện.
    - scaler: Bộ chuẩn hóa dữ liệu.
    - input_data: Danh sách các đầu vào từ người dùng.
    
    Returns:
    - 'Accepted' nếu khoản vay được phê duyệt.
    - 'Rejected' nếu khoản vay bị từ chối.
    """
    # Chuẩn hóa dữ liệu đầu vào
    input_scaled = scaler.transform([input_data])
    # Thực hiện dự đoán
    pred = model.predict(input_scaled)
    return 'Được Chấp Thuận' if pred[0] == 1 else 'Bị Từ Chối'

# Giao diện web với Streamlit
def main():
    # Sidebar với tiêu đề và mô tả
    st.sidebar.title("💼 Ứng Dụng Dự Đoán Khoản Vay")
    st.sidebar.markdown(
        """
        Ứng dụng này dự đoán việc phê duyệt khoản vay dựa trên các thông tin tài chính bạn cung cấp.
        """
    )

    st.sidebar.markdown("### Nhập các thông tin sau:")

    # Các trường nhập liệu trong sidebar với nhãn bằng tiếng Việt
    funded_amnt = st.sidebar.number_input(
        "💵 Số Tiền Đã Cấp (funded_amnt)", 
        min_value=0.0, 
        step=1000.0, 
        format="%.2f",
        value=1000.0  # Giá trị mặc định có thể tùy chỉnh
    )
    total_rec_prncp = st.sidebar.number_input(
        "📈 Tổng Số Tiền Gốc Đã Nhận (total_rec_prncp)", 
        min_value=0.0, 
        step=1000.0, 
        format="%.2f",
        value=500.0
    )
    out_prncp = st.sidebar.number_input(
        "🔴 Số Tiền Gốc Còn Lại (out_prncp)", 
        min_value=0.0, 
        step=1000.0, 
        format="%.2f",
        value=0.0
    )
    out_prncp_inv = st.sidebar.number_input(
        "🔴 Số Tiền Gốc Còn Lại của Nhà Đầu Tư (out_prncp_inv)", 
        min_value=0.0, 
        step=1000.0, 
        format="%.2f",
        value=0.0
    )
    funded_amnt_inv = st.sidebar.number_input(
        "💰 Số Tiền Được Nhà Đầu Tư Cam Kết (funded_amnt_inv)", 
        min_value=0.0, 
        step=1000.0, 
        format="%.2f",
        value=0.0
    )
    total_pymnt_inv = st.sidebar.number_input(
        "💳 Tổng Số Tiền Thanh Toán Được Nhà Đầu Tư Nhận (total_pymnt_inv)", 
        min_value=0.0, 
        step=1000.0, 
        format="%.2f",
        value=0.0
    )
    total_rec_int = st.sidebar.number_input(
        "📊 Tổng Số Tiền Lãi Đã Nhận (total_rec_int)", 
        min_value=0.0, 
        step=100.0, 
        format="%.2f",
        value=100.0
    )
    recoveries = st.sidebar.number_input(
        "🔄 Khoản Thu Hồi Sau Khi Xóa Nợ (recoveries)", 
        min_value=0.0, 
        step=100.0, 
        format="%.2f",
        value=0.0
    )

    # Nút dự đoán
    if st.sidebar.button("🔮 Dự Đoán"):
        # Tạo danh sách các đầu vào từ người dùng
        user_input = [
            funded_amnt,
            total_rec_prncp,
            out_prncp,
            out_prncp_inv,
            funded_amnt_inv,
            total_pymnt_inv,
            total_rec_int,
            recoveries
        ]

        # Kiểm tra nếu có giá trị nào đó âm
        if any(val < 0 for val in user_input):
            st.sidebar.error("Các giá trị không thể âm. Vui lòng kiểm tra lại.")
        else:
            # Thực hiện dự đoán
            result = prediction(model, scaler, user_input)
            st.session_state['result'] = result

    # Nội dung chính của trang
    st.markdown(
        """
        <div style="background-color:#f0f8ff;padding:20px;border-radius:10px">
            <h1 style="color:#003366;text-align:center;">💰 Ứng Dụng Dự Đoán Khoản Vay</h1>
            <p style="color:#555555;text-align:center;">
                Dự đoán xem khoản vay của bạn có được phê duyệt hay không dựa trên các thông tin đã cung cấp.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Hiển thị kết quả dự đoán
    if 'result' in st.session_state:
        result = st.session_state['result']
        if result == 'Được Chấp Thuận':
            st.success(f'🎉 **Khoản vay của bạn đã được {result}**')
            st.balloons()
        else:
            st.error(f'❌ **Khoản vay của bạn {result}**')
            st.warning("Vui lòng kiểm tra lại thông tin hoặc liên hệ bộ phận hỗ trợ.")

    # Thêm footer vào trang
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f0f8ff;
            color: #555555;
            text-align: center;
            padding: 10px;
        }
        </style>
        <div class="footer">
            <p>© 2024 Ứng Dụng Dự Đoán Khoản Vay. Bảo lưu mọi quyền.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()

