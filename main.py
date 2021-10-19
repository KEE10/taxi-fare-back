from services import database

ERROR_405 = {
    "statusCode": 405,
    "error": {"code": "method_not_allowed", "message": "Method not allowed"},
}

ERROR_404 = {
    "statusCode": 404,
    "error": {"code": "path_not_found", "message": "Path not found"},
}

ERROR_500 = {
    "statusCode": 500,
    "error": {"code": "unknown_event", "message": "Unknown event"},
}


def handler(event):
        resource = event.get("resource") or ""
        method = event.get("httpMethod") or ""
        body = event.get("body") or {}
        query_params = event.get("queryStringParameters", {})
        path_params = event.get("pathParameters", {})
        print(
            f"Taxi API called with resource:{resource},"
            f" pathParameters: {path_params}, query params:{query_params}, body:{body}"
        )
        if resource.endswith("/rides"):
            if method == "GET":
                rides = database.fetch_all_rides()
                if rides:
                    response = {"statusCode": 200, "data": rides}
                else:
                    response = ERROR_500
            else:
                response = ERROR_405
        else:
            response = ERROR_404

        print(f"Taxi Rides function response: {response}")
        return response
