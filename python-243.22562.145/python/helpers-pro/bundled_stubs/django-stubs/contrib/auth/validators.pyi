from django.core.validators import RegexValidator

class ASCIIUsernameValidator(RegexValidator): ...
class UnicodeUsernameValidator(RegexValidator): ...
