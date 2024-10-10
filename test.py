from najva_api_client.najva import Najva
client = Najva()
client.apikey = "1cfa1a27-26ee-4af7-9097-8a130094bd49"
client.token = "a1cc832304bdfd173440a20806b72d97554f19c6"
str = client.send_to_all(title="Title",body="Some Description", url="https://google.com",
icon="https://www.ait-themes.club/wp-content/uploads/cache/images/2020/02/guestblog_featured/guestblog_featured-482918665.jpg",
image="https://www.ait-themes.club/wp-content/uploads/cache/images/2020/02/guestblog_featured/guestblog_featured-482918665.jpg",
onclick="open-link")

print(str)