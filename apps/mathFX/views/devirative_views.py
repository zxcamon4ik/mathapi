from ..service import take_derivative
from django.http import JsonResponse


def calculate_derivative(request, const, func, sequence=None):
    if sequence is None:
        sequence = 1
    try:
        result = take_derivative(const, func, sequence)
        return JsonResponse({"Result": str(result)})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=200)
