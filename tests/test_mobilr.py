# import pytest
# import requests
#
#
#
#
# @pytest.mark.parametrize("phone", ["+998900000000", "+998900000001", "+998900000002", "+998900000003", "+998900000004",
#                                    "+998900000005"])
# def test_login(phone):
#     """
#     TODO BU BACKDAN  ERROR BERDI
#     HALI TOGIRLASH GANI YOQ REDISDA MUAMO BOR EKAN
#
#
#     """
#     base_url_qa = "https://api.qa-yonda.uz"
#     response_sent_number = requests.post(f"{base_url_qa}/api/v1/mobile/users/auth/login/", json={"phone": phone})
#     assert response_sent_number.status_code == 200
#
#     response_confirm = requests.post(f"{base_url_qa}/api/v1/mobile/users/auth/login/confirm/", json={
#         "phone": phone,
#         "user_device": "AE3A.240806.043",
#         "otp": "123456",
#         "secret_code": response_sent_number.json()["results"]["secret_code"]
#     })
#
#     assert response_confirm.status_code == 200
#     test_url_call = ["/api/v1/mobile/locations/?location=41.3485567%2C69.2866483&per_page=20&page=1",
#                      "/api/v1/mobile/users/profile/",
#                      "/api/v1/mobile/locations/concise/?reason=payable&per_page=4&page=1&location=41.3485567%2C69.2866483"]
#     for url_call in test_url_call:
#         response = requests.get(f"{base_url_qa}{url_call}", json={},
#                                 headers={'Content-Type': 'application/json', 'Accept-Language': 'uz'},
#                                 cookies=response_confirm.cookies)
#         assert response.status_code == 200
