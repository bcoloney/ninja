
def searchAD(self,username,password):
  cnx = self._getLDAPConnectionAD()
  cnx.simple_bind_s("%s@host" % username, password)
  ret_attributes = "memberOf"
  base = AD_BASE
  scope = ldap.SCOPE_SUBTREE
  filter = 'sAMAccountname=%s' % username
