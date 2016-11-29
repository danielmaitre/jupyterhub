import ldap3

server = ldap3.Server("mds.ad.dur.ac.uk", use_ssl=False)

def find(user):
    conn=ldap3.Connection(server,auto_bind=True)
    res=conn.search("OU=People,DC=mds,DC=ad,DC=dur,DC=ac,DC=uk","(cn={0})".format(user))
    ent=conn.entries.pop()
    dn=ent.entry_get_dn()
    return dn

for u in ["fqnq45",'dph0sjc','dph0zz9']:
    print find(u)
