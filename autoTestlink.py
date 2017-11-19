#! /usr/bin/python
"""
Testlink API Sample Python 2.x Client implementation
"""
import xmlrpclib


class TestlinkAPIClient:
    SERVER_URL = "<testlink url>"

    def __init__(self, devKey):
        self.server = xmlrpclib.Server(self.SERVER_URL)
        self.devKey = devKey

    def getInfo(self):
        return self.server.tl.about()

    def getProjects(self):
        data = {"devKey": self.devKey}
        return self.server.tl.getProjects(data)

    def getProjectTestPlans(self, testplanid):
        data = {'devKey': self.devKey, 'testprojectid  ': int(testplanid)}
        return self.server.tl.getProjectTestPlans(data)

    def GetTestPlanByName(self, testplanname, testprojectname):
        data = {'devKey': self.devKey, 'testplanname': testplanname, 'testprojectname': testprojectname}
        return self.server.tl.getTestPlanByName(data)

    def getTestCaseIDByName(self, testcasename):
        data = {"devKey": self.devKey, "testcasename": testcasename}
        return self.server.tl.getTestCaseIDByName(data)

    def getTestCase(self, tcextid):
        data = {}
        data["devKey"] = self.devKey
        data["testcaseexternalid"] = tcextid
        return self.server.tl.getTestCase(data)

    def getBuildsForTestPlan(self, tplainid):
        data = {}
        data["devKey"] = self.devKey
        data["testplanid"] = tplainid
        return self.server.tl.getBuildsForTestPlan(data)

    def reportTCResult(self, tpid, tcid, status, bid, notes):
        data = {}
        data["devKey"] = self.devKey
        data["testcaseid"] = tcid
        data["testplanid"] = tpid
        data["status"] = status
        data["buildid"] = bid
        data["notes"] = notes
        # Parameter will control if results ca be overwritten
        data["overwrite"] = 1
        # data["platformid"] = pid
        #print self.server.tl.getLastExecutionResult(data)
        return self.server.tl.reportTCResult(data)

