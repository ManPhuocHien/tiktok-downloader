import streamlit as st
import requests

st.set_page_config(page_title="Tải video TikTok không watermark", layout="centered")

st.title("📥 Tải video TikTok không watermark")
st.write("Nhập link video TikTok để tải về máy với chất lượng cao nhất và không dính logo!")

video_url = st.text_input("🔗 Nhập link TikTok:")

import yt_dlp

def get_download_link(video_url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',  # Chọn chất lượng video tốt nhất
            'outtmpl': '%(id)s.%(ext)s',  # Đặt tên file video
            'quiet': False,  # Hiển thị thông báo chi tiết
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)  # Không tải về mà chỉ lấy thông tin
            video_url = info_dict['url']  # Lấy link video

        return video_url

    except Exception as e:
        return None
        
if st.button("🚀 Tải video"):
    if video_url:
        st.info("⏳ Đang xử lý, vui lòng chờ...")
        link = get_download_link(video_url)
        if link:
            st.success("✅ Link video không watermark đã sẵn sàng!")
            st.markdown(f"[👉 Nhấn để tải video](%s)" % link)
            st.video(link)
        else:
            st.error("❌ Không lấy được link video. Hãy kiểm tra lại link TikTok.")
