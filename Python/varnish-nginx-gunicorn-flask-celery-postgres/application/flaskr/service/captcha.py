import random, base64

from flask import session
from captcha.image import ImageCaptcha


class Captcha:
    def generate_captcha(name):
        captcha = ImageCaptcha(
            height=60,
            width=160
        )
        value = str(
            random.randrange(10000, 99999)
        )
        data = captcha.generate(value)
        base64_captcha = f'data:image/png;base64, {base64.b64encode(data.getvalue()).decode("ascii")}'
        session[f'captcha_{name}'] = value

        return base64_captcha

    def verify(name, value):
        val = session.get(f'captcha_{name}', None)
        if name in session:
            session.pop(name)

        return val and val == value
