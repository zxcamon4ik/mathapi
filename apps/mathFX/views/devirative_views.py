from django.http import JsonResponse
from ..models import DerivativeResult
from ..service import take_derivative


def calculate_derivative(request, const, func, sequence=None):
    try:
        if sequence is None:
            sequence = 1

        result = take_derivative(const, func, sequence)

        derivative_result = DerivativeResult(
            const=const,
            func=func,
            sequence=sequence,
            result=result
        )
        derivative_result.save()

        return JsonResponse({"Result": str(result)})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
