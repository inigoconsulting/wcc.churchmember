from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import wcc.churchmember


WCC_CHURCHMEMBER = PloneWithPackageLayer(
    zcml_package=wcc.churchmember,
    zcml_filename='testing.zcml',
    gs_profile_id='wcc.churchmember:testing',
    name="WCC_CHURCHMEMBER")

WCC_CHURCHMEMBER_INTEGRATION = IntegrationTesting(
    bases=(WCC_CHURCHMEMBER, ),
    name="WCC_CHURCHMEMBER_INTEGRATION")

WCC_CHURCHMEMBER_FUNCTIONAL = FunctionalTesting(
    bases=(WCC_CHURCHMEMBER, ),
    name="WCC_CHURCHMEMBER_FUNCTIONAL")
