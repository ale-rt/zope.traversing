##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################
"""

Revision information:
$Id: test_etc.py,v 1.5 2003/05/01 19:35:38 faassen Exp $
"""

from unittest import TestCase, main, makeSuite
from zope.testing.cleanup import CleanUp # Base class w registry cleanup

class Test(CleanUp, TestCase):

    def testApplicationControl(self):
        from zope.app.traversing.namespace import etc
        from zope.app.applicationcontrol.applicationcontrol \
             import applicationController, applicationControllerRoot

        self.assertEqual(
            etc('process', (), '++etc++process',
                applicationControllerRoot, None),
            applicationController)

    def testServices(self):
        from zope.app.traversing.namespace import etc
        class C:
            def getServiceManager(self): return 42

        self.assertEqual(etc('site', (), 'etc:site', C(), None), 42)



def test_suite():
    return makeSuite(Test)

if __name__=='__main__':
    main(defaultTest='test_suite')
