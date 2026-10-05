import logging
import time
import uuid


logger = logging.getLogger("employees")


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_id = str(uuid.uuid4())
        request.request_id = request_id

        start_time = time.perf_counter()

        if request.user.is_authenticated:
            user = str(request.user.username)
        else:
            user = "anonymous"

        logger.info(
            "Request started | request_id=%s | method=%s | path=%s | user=%s",
            request_id,
            request.method,
            request.path,
            user,
        )

        try:
            response = self.get_response(request)

            execution_time = time.perf_counter() - start_time

            if response.status_code >= 500:
                log_level = logger.error
            elif response.status_code >= 400:
                log_level = logger.warning
            else:
                log_level = logger.info

            log_level(
                "Request completed | request_id=%s | method=%s | "
                "path=%s | user=%s | status=%s | execution_time=%.4fs",
                request_id,
                request.method,
                request.path,
                user,
                response.status_code,
                execution_time,
            )

            response["X-Request-ID"] = request_id

            return response

        except Exception:
            execution_time = time.perf_counter() - start_time

            logger.exception(
                "Request failed | request_id=%s | method=%s | "
                "path=%s | user=%s | execution_time=%.4fs",
                request_id,
                request.method,
                request.path,
                user,
                execution_time,
            )

            raise