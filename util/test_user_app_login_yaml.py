import yaml


class TestUserAppLoginYaml:
    def test_user_app_login_yaml(self):
        data = {
            "user_app_login": {
                "method": "post",
                "url": "/user/userLogin/userAppLogin",
                "data": {
                    "body": {"mobile": "19520409998", "validateCode": "8888", "inviter_user_id": ""}

                },
                "header": {'Content-Type': 'application/json;charset=UTF-8'
                           }
            },
            'test_user_app_login_python_file': {
                "method": "post",
                "url": "/user/userLogin/userAppLogin",
                "data": {
                    "body": {"mobile": "19520409", "validateCode": "8888", "inviter_user_id": ""}

                },
                "header": {'Content-Type': 'application/json;charset=UTF-8'
                           }
            },
            'test_user_app_login_password_file': {
                "method": "post",
                "url": "/user/userLogin/userAppLogin",
                "data": {
                    "body": {"mobile": "19520409998", "validateCode": "8868", "inviter_user_id": ""}

                },
                "header": {'Content-Type': 'application/json;charset=UTF-8'
                           }
            }
        }
        with open('../data/user_app_login.yml', 'w') as f:
            yaml.safe_dump(stream=f, data=data)
