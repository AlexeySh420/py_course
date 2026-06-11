import requests as req

nasa_api = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
nas_api_key = "DEMO_KEY"

param = {"api_key":nas_api_key, "earth_date":"2020-07-01"}
nasa_resp = req.get(nasa_api, params=param)

print(nasa_resp.status_code)
print(nasa_resp.json())

photos = nasa_resp.json()["photos"]

with open("links.txt", "w") as fs:
    for photo in photos:
        fs.write(photo['img_src']+"\n")

with open("links.txt", "r") as fs:
    img_urls = fs.readlines()

for number, url in enumerate(img_urls):
    url = url.strip()
    response = req.get(url)

    with open(f"nasa_{number}.JPG", "wb") as img_file:
        img_file.write(response.content)

    print(f"Image {number} successfully downloaded")

print("all good")