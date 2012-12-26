
def searchAD(self, username, password):
    """
    A simple method to search ActiveDirectory

    param: username
    param: password
    """
    cnx = self._getLDAPConnectionAD()
    cnx.simple_bind_s("%s@host" % username, password)
    ret_attributes = "memberOf"
    base = AD_BASE
    scope = ldap.SCOPE_SUBTREE
    myfilter = 'sAMAccountname=%s' % username
