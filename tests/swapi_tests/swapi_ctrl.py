from tests.gorest.rest_base import RestBase


class SwapiCtrl(RestBase):

    def __init__(self, url='https://www.swapi.tech/api/'):
        self.url = url


    def get_person(self, user_id, status_code=200):
        """
        send request to get  /api/people/{user_id}/
        """

        url = f'{self.url}people/{user_id}/'  # url = self.url + 'people/' + str(user_id) + '/'

        return self._execute_request(method='get', url=url, status_code=status_code)


    def get_people(self, params=None, status_code=200):
        """
        send request to get  /api/people/
        """

        url = f'{self.url}people/'

        return self._execute_request(method='get', url=url, params=params, status_code=status_code)