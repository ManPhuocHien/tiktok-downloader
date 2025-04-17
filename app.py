import streamlit as st
import requests

st.set_page_config(page_title="Tải video TikTok không watermark", layout="centered")

st.title("📥 Tải video TikTok không watermark")
st.write("Nhập link video TikTok để tải về máy với chất lượng cao nhất và không dính logo!")

video_url = st.text_input("🔗 Nhập link TikTok:")

def get_download_link(video_url):
    try:
        # API ssstik.io
        api_url = f"https://api.ssstik.io/convert?url={video_url}"
        res = requests.get(api_url)
        
        if res.status_code == 200:
            # Lấy link video không watermark
            video_url = res.json()["url"]
            return video_url
        else:
            return None
    except:
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
