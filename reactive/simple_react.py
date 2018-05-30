from charms.reactive import when, when_not, set_state

from charmhelpers.core.hookenv import status_set
from charmhelpers.core.hookenv import log

import charms.apt

@when_not('simple-react.installed')
def install_simple_react():
    # Do your setup here.
    #
    # If your charm has other dependencies before it can install,
    # add those as @when() clauses above., or as additional @when()
    # decorated handlers below
    #
    # See the following for information about reactive charms:
    #
    #  * https://jujucharms.com/docs/devel/developer-getting-started
    #  * https://github.com/juju-solutions/layer-basic#overview
    #
    print("I hope this is logged!")
    set_state('simple-react.installed')
    status_set("maintenance", " Im not Ready")
    log("Installation complete")


@when('apt.installed.git')
def foo_baar():
    status_set('active', "Git ready")
    #set_state('erik.flaggade')


#@when('erik.flaggade')
#@when_not('apt.installed.git')
#def eriksfunkltion():
#    log("Erik flaggade")
#    clear_flag('erik.flaggade')
