from plug.error import VerificationError

class PlaceholderError(VerificationError):
    fqdn = 'dread_snarfle.error.PlaceholderError'
    status_code = 400
