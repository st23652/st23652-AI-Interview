from django.core.exceptions import BadRequest, SuspiciousOperation

class InvalidSessionKey(SuspiciousOperation): ...
class SuspiciousSession(SuspiciousOperation): ...
class SessionInterrupted(BadRequest): ...
