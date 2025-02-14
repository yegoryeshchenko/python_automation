from tests.gorest.rest_base import RestBase


class GorestCtrl(RestBase):

    def __init__(self, url='https://gorest.co.in/public/v2/'):
        self.url = url
        self.token = self.get_token()


    def get_token(self):
        # токен з будь-якого місця
        return '0266b8033d542115cb64bfed9d0d99b70a12df639a827aeff82c624776f5f48f'


    def get_users(self, status_code=200):
        """
        send request to get  /users/
        """

        url = f'{self.url}users/'

        return self._execute_request(method='get', url=url, status_code=status_code)


    def get_user(self, user_id, status_code=200):
        """
        send request to get  /users/{user_id}
        """

        url = f'{self.url}users/{user_id}/'

        return self._execute_request(method='get', url=url, status_code=status_code)


    def create_user(self, data, token=None, status_code=201):
        """
        send request to get  /users/
        """

        url = f'{self.url}users/'

        if token is None:
            headers = {'Authorization': f'Bearer {self.token}'}
        else:
            headers = {'Authorization': token}


        response =  self._execute_request(
            method='post', url=url, data=data, headers=headers,
                                     status_code=status_code)

        return response


    def update_user(self, user_id, status_code=200):
        """
        send request to get  /users/{user_id}/
        """

        url = f'{self.url}users/{user_id}/'

        return self._execute_request(method='patch', url=url, status_code=status_code)


    def delete_user(self, user_id, status_code=200):
        """
        send request to get  /users/{user_id}/
        """

        url = f'{self.url}users/{user_id}/'

        return self._execute_request(method='delete', url=url, status_code=status_code)
