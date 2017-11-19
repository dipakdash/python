from autoTestlink import TestlinkAPIClient
import os
import glob

# Initialise and get instance of TestlinkAPIClient
# substitute your Dev Key Here
#devkey = "e65726f865af384473a90193750ee976" #Testlink User "dipakdash"
devkey = "23671fb06d06c9ccf6ff7ca1ed3b2b0e"  #Testlink User "script"
TestProject = "MWG 7.x"
TestPlan = "7.8.0_Regression_Test"
client = TestlinkAPIClient(devkey)
# Get the Test Plan ID
projectPlans_list = client.GetTestPlanByName(TestPlan, TestProject)
testplanID = int(projectPlans_list[0]['id'])
# This description is only for FIPS Automation. Change this for any other automation.

descriptionHeader = """Added by testlink auto-update python script

"""

descriptionStatic = """

CDASH report:
https://dart.dev.webwasher.com/cdash/viewTest.php?buildid=711469
https://dart.dev.webwasher.com/cdash/buildSummary.php?buildid=711469

How to start FIPS automation
============================
Setup needed
------------
External FIPS Mode MWG (installed on local ESX server)
External Non-FIPS Mode MWG (installed on local ESX server)
External Auth Server (installed on local ESX server)

If possible assign static IPs to MWG test systems.

Qiblade Setup
-------------
Let the qiblade setup bring up one MWG of IP 192.168.10.10
This is useful as the python script "findMWGVersion.py" will use this IP to do SSH and get the MWG version (part of "Script\LogWriter - LogFile_onstop_ProjectSuite" in FIPS test suite)

Alternatively you can use the other Non-FIPS mode MWG (Same version MWG and root password as "ssurfer") and enter the IP in "findMWGVersion.py" for this purpose. But don't check-in this script into SVN.

Important
---------
Get the IP of External MWG and enter this in "Windows Server 2008" Windows hosts file (where you want to run FIPS automation)
If you are using qiblade, then after the setup is brought up, add the IP of External MWG into the "Windows Server 2008"
By doing the above the mwg UI can be accessed as:
proxy_url_http = "http://mwg:4711/"
proxy_url_https = "https://mwg:4712/"

If I don't follow these steps, when I start automation, TestComplete does a successful MWG UI login but after that clicking any UI component fails (still don't know why).
Looks like when "https://<ip>:4712/" is used, TC fails to get the loaded webpage objects. May be something to do with the dotted IP address string in the object path.

NOTE:
There is a new pop up (as mentioned below) in UI which has been introduced this time with 7.8 build. This occurs when automation clicks on "Hardware Security Module". Clicking on this is not a part of this automation but happens somehow happens by default. Handle this in automation. For now I clicked on OK button manually and the automation continued successfully.
Title = Default Certificate Warning
Content = McAfee Web Gateway
          This is a default Certificate, we recomend that you create your own root certificate authority
          "OK" button
Got confirmation from Rajesh that this type of popup Window might appear at 5 different places in UI that deal with certificate. The title will be always same and the content might vary a bit with a OK button for sure. From automation point of view we can just click on "OK" button to proceed.
"""

# This information is already available inside file "TestCompleteLogFile_FIPS.mds.log". Just read it to extract that part for logging in testlink
def readTestCompleteLogFile():
    logFile = '\n'.join(glob.iglob(os.path.join(".", "TestCompleteLogFile_*")))
    dictMETA = {}
    strMETA = ""
    if logFile == "":
        return "\n***Test details are missing as TestCompleteLogFile NOT Found***\n"
        
    f = open(logFile)
    lines = f.readlines()
    f.close()
    
    for line in lines:
        if "META: Name=" in line:
            dictMETA["TestName"] = (line.split("=")[1]).strip()
        if "META: Deployment=" in line:
            dictMETA["Deployment"] = (line.split("=")[1]).strip()
        if "META: Tester=" in line:
            dictMETA["Tester"] = (line.split("=")[1]).strip()
        if "META: MWGVersion=" in line:
            dictMETA["Build Number"] = (line.split("=")[1]).strip()            
            
    #print dictMETA['TestName']
    #print dictMETA['Deployment']
    #print dictMETA['Tester']
    #print dictMETA['Build Number']
    
    for (k, v) in dictMETA.iteritems():
        temp = k + ": " + v + "\n"
        strMETA = strMETA + temp
    return strMETA

# Updates a single test execution result in Testlink
def updateTestlink(TestCaseNumber, status):
    #TestCaseNumber = "7.x-2293"
    TestCaseNumber = TestCaseNumber

    # Get the Test Case ID given the test name
    testcase_list = client.getTestCase(TestCaseNumber)
    testcaseid=testcase_list[0]['testcase_id']
    # Get the Builds for the above test Plan
    build_list = client.getBuildsForTestPlan(testplanID)
    # This outputs all the builds added for plans . To get the latest build we give -1 as the key.
    build_id = int(build_list[0]['id'])
    
    strMETA = readTestCompleteLogFile()
    description = descriptionHeader + strMETA + descriptionStatic
    
    # f for fail , p for pass
    result = client.reportTCResult(testplanID, testcaseid, status, build_id, description)
    print result


# Read the test run status from "results.txt" file and update testlink
def updateResults():
    f = open("results.txt")
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.strip()
        a = line.split("==>")
        TestCaseNumber = a[0]
        if a[1] == "PASS":
            status = "p"
        else:
            status = "f"
        updateTestlink(TestCaseNumber, status)
  
updateResults()


