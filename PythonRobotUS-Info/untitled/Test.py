__author__ = 'admin'
import json

def deleteFpcFromExistingGnf(baseURL,gnfList):

    '''
	{
	"gnf": [
		{
		"name": "4",
		"description": "test02",
		"fpcs": [
			"5"
			]
		}
		]
	}

    '''

    gnfDictList=[]

    '''for item1 in gnfList:
        gnfDict=createGNFDict(item1[0],item1[1],item1[2])'''

    item1 = [x for x in gnfList]
    gnfDict=createGNFDict(item1[0],item1[1],item1[2])
    gnfDictList.append(gnfDict)

	#gnfDictList.append(gnfDict)
    addgnfDict={}
    addgnfDict['gnf']=gnfDictList
    #headers=vnfRest.createHeadersJSONReqForBNC()
    #url = baseURL + deleteFpc
    #print url
    inJson = json.loads(json.dumps(addgnfDict))
    print inJson
    #response=util.DoPutRequestAndRetryOnFailure(url.inJson,headers)
    #print response
    #return response
def createGNFDict(name,desc,fpcsList):
     return{'name':name,'description':desc,'fpcs':[fpcsList]}



GnfList=[3,02,5]
url1="http://123"
deleteFpcFromExistingGnf(url1,GnfList)
