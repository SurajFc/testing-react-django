from .test_setup import TestSetup

class TestViews(TestSetup):
    def test_userprofile_without_data(self):
        print("Test case 1")
        resp = self.client.post(self.user_profile)
        print("Test Result 1:", "Ok" if resp.status_code == 400 else "Failed", "\n")
        self.assertEqual(resp.status_code, 400)

    def test_userprofile_with_data(self):
        print("Test case 2")
        resp = self.client.post(self.user_profile, self.data)
        print("Test Result 2:", "Ok" if resp.status_code == 201 else "Failed", "\n")
        self.assertEqual(resp.status_code, 201)

    def test_userprofile_with_response(self):
        print("Test case 3")
        resp = self.client.post(self.user_profile, self.data)
        response = resp.json()
        print("Test Result 3:", "Ok" if response["data"]["id"] == 1 else "Failed", "\n")
        self.assertEqual(response["data"]["id"], 1)

    def test_userprofile_with_response_status(self):
        print("Test case 4")
        resp = self.client.post(self.user_profile, self.data)
        response = resp.json()
        print("Test Result 4:", "Ok" if response["success"] is True else "Failed", "\n")
        self.assertEqual(response["success"], True)

    def test_userprofile_with_update(self):
        print("Test case 5")
        resp = self.client.post(self.user_profile, self.data)
        response = resp.json()
        id = response['data']['id']

        data_update = {
            "name": "test",
            "email": "test@12.com",
            "bio": "hello"
        }
        resp = self.client.patch(f"{self.user_profile}?id={id}", data_update)
        print("Test Result 5:", "Ok" if resp.status_code == 200 else "Failed", "\n")
        self.assertEqual(resp.status_code, 200)

    def test_userprofile_with_update_without_passing_query_params(self):
        print("Test case 6")
        data_update = {
            "name": "test",
            "email": "test@12.com",
            "bio": "hello"
        }
        resp = self.client.patch(f"{self.user_profile}?", data_update)
        print("Test Result 6:", "Ok" if resp.status_code == 400 else "Failed", "\n")
        self.assertEqual(resp.status_code, 400)


    # def test_userprofile_delete(self):
    #     print("Test case 7 - Delete")
    #     # Creating a user profile to delete
    #     resp_create = self.client.post(self.user_profile, self.data)
    #     self.assertEqual(resp_create.status_code, 201)
    #     user_profile_id = resp_create.json()["data"]["id"]

    #     # Deleting the user profile
    #     resp_delete = self.client.delete(f"{self.user_profile}?id={user_profile_id}")

    #     print("Test Result 7 - Delete:", "Ok" if resp_delete.status_code == 204 else "Failed", "\n")
    #     self.assertEqual(resp_delete.status_code, 204)