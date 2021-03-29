file_value = [1, 2, 3]
file_urls = []

for f in file_value:
    file_name = f
    file_url = f"'url':'https://hpdjango.herokuapp.com/media/{file_name}'"
    file_urls.append({file_url})

print(file_urls)