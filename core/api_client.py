import requests
import json
from typing import Optional, Dict, Any
from config.settings import settings
from core.logger import log


class APIClient:
    """Клиент для работы с API"""

    def __init__(self, base_url: str = None):
        self.base_url = base_url or settings.BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    def _log_request(self, method: str, url: str, data: Any = None, params: Any = None):
        """Логирование запроса"""
        log.info(f"{method} {url}")
        if params:
            log.debug(f"Params: {params}")
        if data:
            log.debug(f"Data: {json.dumps(data, indent=2, ensure_ascii=False)}")

    def _log_response(self, response: requests.Response):
        """Логирование ответа"""
        log.info(f"Response: {response.status_code}")
        try:
            if response.text:
                log.debug(f"Body: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        except:
            log.debug(f"Body: {response.text}")

    def _request(self, method: str, endpoint: str, data: Any = None,
                 params: Any = None, headers: Optional[Dict] = None) -> requests.Response:
        """Универсальный метод для отправки запросов"""
        url = f"{self.base_url}{endpoint}"
        self._log_request(method, url, data, params)

        # Объединяем заголовки
        if headers:
            self.session.headers.update(headers)

        response = self.session.request(
            method=method,
            url=url,
            json=data,
            params=params,
            timeout=settings.REQUEST_TIMEOUT
        )

        self._log_response(response)

        # Проверяем статус-код
        if response.status_code >= 400:
            log.error(f"Error response: {response.status_code} - {response.text}")

        return response

    def get(self, endpoint: str, params: Any = None, headers: Optional[Dict] = None) -> requests.Response:
        """GET запрос"""
        return self._request('GET', endpoint, params=params, headers=headers)

    def post(self, endpoint: str, data: Any = None, headers: Optional[Dict] = None) -> requests.Response:
        """POST запрос"""
        return self._request('POST', endpoint, data=data, headers=headers)

    def put(self, endpoint: str, data: Any = None, headers: Optional[Dict] = None) -> requests.Response:
        """PUT запрос"""
        return self._request('PUT', endpoint, data=data, headers=headers)

    def delete(self, endpoint: str, headers: Optional[Dict] = None) -> requests.Response:
        """DELETE запрос"""
        return self._request('DELETE', endpoint, headers=headers)

    def patch(self, endpoint: str, data: Any = None, headers: Optional[Dict] = None) -> requests.Response:
        """PATCH запрос"""
        return self._request('PATCH', endpoint, data=data, headers=headers)