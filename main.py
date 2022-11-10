from urls import urlpatterns

while True:
    inp_url = input("Введите адрес: ")

    found = False
    for url, view in urlpatterns:
        if url == inp_url:
            found = True
            try:
                view()
            except Exception as e:
                print(e)

    if not found:
        print("404: Url not found")