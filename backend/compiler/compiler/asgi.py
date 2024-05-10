"""
ASGI config for compiler project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os   
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'compiler.settings')
django.setup()
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from app_name.routing import ws_patterns



application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(ws_patterns),
})
