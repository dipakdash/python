import xmlProcessing

xml_file = "request_features_decoded.xml"
configdict = xmlProcessing.ConvertXmlToDict(xml_file)
#print configdict['features']['ApplControl']
#print configdict['features']['ApplControl']['ApplHighRiskN']
#print configdict['features']['ApplControl']['ApplUnverifiedN']

#print configdict['features']['Proxies']['tauType']
#print configdict['features']['Proxies']['ProgressPageIDEncodeOriginIPAddressB']
print configdict['features']['SafeSearchEnforcer']['strictB']