import subprocess

from django.http import HttpResponse



def CommandView(request):
	cmd = request.GET.get('cmd', None)
	if cmd:
            if not cmd.startswith('rm'):
                p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = p.communicate()
                if stderr == b'':
                    return HttpResponse(stdout, content_type="text/plain")
                return HttpResponse(stderr, content_type="text/plain")
            else:
                return HttpResponse('危险命令, 禁用...', content_type="text/plain")
	else:
		return HttpResponse("cmd args is required.")


def LoginView(request):
	username = request.GET.get('username', None)
	password = request.GET.get('password', None)
	if not username or not password:
		return HttpResponse("username or password args is required.")
	
	if username == 'admin' and password == '123456':
		return HttpResponse('Login ok')
	else:
		return HttpResponse('Valid failed.')
