from django.dispatch import Signal

user_sign_in = Signal(providing_args=["user", "request"])
user_registered = Signal(providing_args=["user", "request"])
user_sign_out = Signal(providing_args=["user", "request"])
