import ldap3
import re
from jupyterhub.auth import Authenticator

from tornado import gen
from traitlets import Unicode, Int, Bool, Union, List


class LDAPAuthenticator(Authenticator):
    server_address = Unicode(
        config=True,
        help='Address of LDAP server to contact'
    )
    server_port = Int(
        config=True,
        help='Port on which to contact LDAP server',
    )

    def _server_port_default(self):
        if self.use_ssl:
            return 636  # default SSL port for LDAP
        else:
            return 389  # default plaintext port for LDAP

    use_ssl = Bool(
        True,
        config=True,
        help='Use SSL to encrypt connection to LDAP server'
    )

    bind_dn_template = Unicode(
        config=True,
        help="""
        Template from which to construct the full dn
        when authenticating to LDAP. {username} is replaced
        with the actual username.
        Example:
            uid={username},ou=people,dc=wikimedia,dc=org
        """
    )


    allowed_groups = List(
	config=True,
	help="List of LDAP Group DNs whose members are allowed access"
    )

    valid_username_regex = Unicode(
        r'^[a-z][.a-z0-9_-]*$',
        config=True,
        help="""Regex to use to validate usernames before sending to LDAP
        Also acts as a security measure to prevent LDAP injection. If you
        are customizing this, be careful to ensure that attempts to do LDAP
        injection are rejected by your customization
        """
    )

    @gen.coroutine
    def authenticate(self, handler, data):
        username = data['username']
        password = data['password']

        # Protect against invalid usernames as well as LDAP injection attacks
        if not re.match(self.valid_username_regex, username):
            self.log.warn('Invalid username')
            return None

        # No empty passwords!
        if password is None or password.strip() == '':
            self.log.warn('Empty password')
            return None

        userdn_ug = "cn={0},ou={1},ou=UG,ou=people,DC=mds,DC=ad,DC=dur,DC=ac,DC=uk".format(username,username[0:3])
        userdn_staff = "cn={0},ou={1},ou=Staff,ou=people,DC=mds,DC=ad,DC=dur,DC=ac,DC=uk".format(username,username[0:3])

        server = ldap3.Server(
            self.server_address,
            port=self.server_port,
            use_ssl=self.use_ssl
        )
        conn = ldap3.Connection(server, user=userdn_ug, password=password)

        if conn.bind():
            return username
        else:
            conn = ldap3.Connection(server, user=userdn_staff, password=password)
            if conn.bind():
                return username
            else:
                self.log.warn('Invalid password')
                return None
