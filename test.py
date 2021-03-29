import json

file_value = [1, 2, 3]
file_urls = []

for f in file_value:
    file_url = dict(url=f"https://hpdjango.herokuapp.com/media/{f}")
    file_urls.append(file_url)

print(file_urls)

# [
#     {
#         "url": "https://2.bp.blogspot.com/-aaYab7phjF4/Xa_TOXvC5hI/AAAAAAAAQME/2xf9AYY0450n-hAobHdEHRrYmPbcy0jsACLcBGAsYHQ/w914-h514-p-k-no-nu/suzy-beautiful-korean-girl-uhdpaper.com-4K-4.1423-wp.thumbnail.jpg"
#     },
#     {
#         "url": "https://dl.airtable.com/.attachments/9d020ee5ca79c9b527c030ced8d83bef/0d11df0c/KakaoTalk_20200527_084727449.png",
#     },
# ],
