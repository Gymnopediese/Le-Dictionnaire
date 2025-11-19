from upload_post import UploadPostClient
api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImxlZGlzdHJpYnV0ZXVyZGVqdWxpZXR0ZUBnbWFpbC5jb20iLCJleHAiOjQ5MTYzODQ1MjQsImp0aSI6ImI4MjY5ZDAyLTMyZGQtNDdmYS05OTk3LWE2ZmY1OGZkMDI1ZiJ9.8e6-cAEBDqpjjXN_DeuH2CoAsjJ4abRweynAhU4RsMw"

client = UploadPostClient(api_key=api_key)
response = client.upload_video(
    video_path="out.mp4",
    title="Bonjour Internet !",
    description="Comment ca vas ?",
    user="LeDistributeurDeJuliette",
    platforms=["youtube", "instagram"]
)

# curl \
# -H 'Authorization: Apikey eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImxlZGlzdHJpYnV0ZXVyZGVqdWxpZXR0ZUBnbWFpbC5jb20iLCJleHAiOjQ5MTYzODQ1MjQsImp0aSI6ImI4MjY5ZDAyLTMyZGQtNDdmYS05OTk3LWE2ZmY1OGZkMDI1ZiJ9.8e6-cAEBDqpjjXN_DeuH2CoAsjJ4abRweynAhU4RsMw' \
# -F 'video=@./out.mp4' \
# -F 'title="Bonjour Internet !"' \
# -F 'user="LeDistributeurDeJuliette"' \
# -F 'platform[]=instagram' \
# -F 'platform[]=youtube' \
# -X POST https://api.upload-post.com/api/upload