from django.http import JsonResponse
from ..service import integral, undefined_integral


def calculate_integral(request, const, func, n1, n2):
    try:
        result = integral(const, func, n1, n2)
        return JsonResponse({"Result": str(result)})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def calculate_undefined_integral(request, const, func):
    try:
        result = undefined_integral(const, func)
        return JsonResponse({"Result": str(result)})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=200)


