#Мигачев Арсений, 30 когорта - финальный проект, инженер по тестированию плюс
import sender_stand_request
import configuration
import data

def test_create_and_get_order():
    create_order_response = sender_stand_request.create_order()
    track_number = create_order_response.json()["track"]
    get_order_response = sender_stand_request.get_order_by_track(track_number) 
    assert get_order_response.status_code == 200, "Тест провален"
    if get_order_response.status_code == 200:
        print ("Тест пройден")
