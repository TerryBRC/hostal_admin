from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            # Obtener los grupos del usuario y sus permisos asociados
            grupos = user.groups.all()
            permisos = []
            for grupo in grupos:
                permisos_grupo = grupo.permissions.all()
                permisos.extend(list(permisos_grupo.values_list('name', flat=True)))
            
            return JsonResponse({'success': True, 'message': 'Inicio de sesión exitoso.', 'permisos': permisos})
        else:
            return JsonResponse({'success': False, 'message': 'Credenciales incorrectas. Por favor, intenta de nuevo.'}, status=401)

    return JsonResponse({'success': False, 'message': 'Método no permitido.'}, status=405)
