import requests
import logging


logger = logging.getLogger('RestBase')

class RestBase:


    @staticmethod
    def _execute_request(method, url, params=None, data=None, json=None, headers=None, files=None,
                         cookies=None, status_code=None):


        response = getattr(requests, method)(url=url, params=params, data=data,
                           json=json, headers=headers, files=files, cookies=cookies)

        logger.info(f'request was sent to {method} {url} with params {params}'
                    f'\nResponse has status code {response.status_code}')


        # logger.info(f'response  {response.json()}')

        if status_code is not None:
            assert response.status_code == status_code, (f'Expected status code {status_code}, '
                                                         f'but actual is {response.status_code}')

        return response

        # request_attr =  = getattr(requests, method)
        # if method == 'get' => requests.get
        # if method == 'post' => requests.post
        # if method == 'delete' => requests.delete


        # if method == 'get':
        #     requests.get(url=url, params=params, data=data,
        #                    json=json, headers=headers, files=files)
        #
        # if method == 'post':
        #     requests.get(url=url, params=params, data=data,
        #                    json=json, headers=headers, files=files)
        #
        # if method == 'put':
        #     requests.get(url=url, params=params, data=data,
        #                    json=json, headers=headers, files=files)