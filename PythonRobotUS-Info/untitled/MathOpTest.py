#a=10
#b=20
from robot.api import logger
import json

class MyContinuableError(RuntimeError):
    ROBOT_CONTINUE_ON_FAILURE = True

class MathOpTest:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.result=0
        self.excepted=''

    def math_op_query(self,result):
        #for i in range(1,11,1):
        print result
        self.excepted=int(result)
        self.result=int(result)
        logger.console('in query%s'%self.excepted)
        return self.result

    #def result_should_contain(self,excepted1):
    def result_validate(self,excepted1):
        excepted1=int(excepted1)
        #b=int(b)
        #c=int(c)
        #c=b+c
        print excepted1
        if self.excepted == excepted1:
            print self.result
            #logger.console('added numb=%d'%b)
            return self.excepted
            #raise AssertionError ("False")
            #raise AssertionError
            # return True
        else:
            print "---False----"
            a = "False"
            logger.console('Hello, console!')
            raise AssertionError("Test Fail")
			#raise AssertionError("Test Fail123....")
            #raise AssertionError ('%s',%a)
            return False

    def createGNFDict(self,name,desc,fpcsList):
        return{'name':name,'description':desc,'fpcs':[fpcsList]}

    def deleteFpcFromExistingGnf(self,baseURL,gnfList):

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
            gnfDict=self.createGNFDict(item1[0],item1[1],item1[2])
            gnfDictList.append(gnfDict)'''

        item1 = [x for x in gnfList]
        gnfDict=self.createGNFDict(item1[0],item1[1],item1[2])
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
        return inJson



#class_ins = MathOpTest()
#result1= class_ins.math_op_query(10-9)
#excepted1=class_ins.result_should_contain(2)
#print excepted1

